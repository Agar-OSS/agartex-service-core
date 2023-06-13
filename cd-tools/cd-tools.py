from flask import Flask, request, Response
import logging
from threading import Thread
from queue import Queue
import os

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
DOCKER_PASSWORD = None

def deploy(name: str):
    logging.info(f'Re-deploy {name}')
    os.system(f'''
docker login -u cd-tools -p {DOCKER_PASSWORD} agaross.azurecr.io
docker compose pull {name}
docker compose up -d {name}
    ''')

deployQueue = Queue()

def worker():
    while True:
        deploy(deployQueue.get())
        deployQueue.task_done()

@app.route('/', methods=['POST'])
def release():
    data = request.json
    logging.debug(data)

    if data['action'] == 'ping':
        return Response('OK', status=200)

    if data['action'] == 'push':
        service = data['target']['repository']
        name = service.split('/')[-1]

        logging.info(f'Enqueue {name} deployment')
        deployQueue.put(name)

        return Response('Accepted', status=202)

    return Response('Bad request', status=400)

if __name__ == '__main__':
    DOCKER_PASSWORD = os.environ['DOCKER_PASSWORD']
    
    # Start system
    os.system(f'''
docker login -u cd-tools -p {DOCKER_PASSWORD} agaross.azurecr.io
docker compose build
docker compose pull
docker compose down
docker compose up -d
    ''')

    Thread(target=worker, daemon=True).start()
    app.run(host='0.0.0.0', port=9999)
