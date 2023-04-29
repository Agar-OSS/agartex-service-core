# Caddy gateway config

Combine microservices into one API described in [Swagger](../swagger.yaml).

Automatically converts `RSESSID` to `X-User-Id` for protected routes to simplify authentication step.

List of unprotected routes:
* POST `/users`
* POST `/sessions`
