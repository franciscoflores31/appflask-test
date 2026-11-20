# appflask-test

Página web sencilla en Flask servida detrás de Nginx, con Podman.

## Uso

```bash
podman-compose up -d --build
```

Abrir http://localhost:8080

- `app/`: aplicación Flask (Gunicorn, puerto 5000 interno)
- `nginx/`: proxy inverso, expuesto en el puerto 8080
- `/health`: endpoint de salud
