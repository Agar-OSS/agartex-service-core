# CD tools

Simple script allowing automatic service deployment on push to Container Registry.
Doesn't include checks or rollback mechanism.

Before start:
* Put Docker CR API token to `../secrets/DOCKER_PASSWORD`.
* Configure webhook to send events on `push` to port `9999`.

```
# Execute from root directory
chmod +x cd-tools/run-cd-tools.sh
./cd-tools/run-cd-tools.sh
```

Preferably run it in background (e.g. use `screen`)