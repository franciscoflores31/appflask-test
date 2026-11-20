from flask import Flask, render_template_string
import socket, datetime

app = Flask(__name__)

PAGE = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Flask + Nginx en Podman</title>
  <style>
    body { font-family: system-ui, sans-serif; background: #0f172a; color: #e2e8f0;
           display: grid; place-items: center; min-height: 100vh; margin: 0; }
    .card { background: #1e293b; padding: 2rem 3rem; border-radius: 12px; text-align: center; }
    h1 { color: #38bdf8; margin-top: 0; }
    code { color: #fbbf24; }
    hr { border: 0; border-top: 1px solid #334155; margin: 1.5rem 0; }
    table { margin: 0 auto; text-align: left; border-collapse: collapse; }
    th { color: #94a3b8; font-weight: 500; padding: .25rem 1rem .25rem 0; }
    td { padding: .25rem 0; }
  </style>
</head>
<body>
  <div class="card">
    <h1>¡Hola desde Flask!</h1>
    <p>Servido por <code>Nginx</code> → <code>Gunicorn/Flask</code> en Podman</p>
    <p>Contenedor: <code>{{ host }}</code></p>
    <p>Hora: <code>{{ now }}</code></p>
    <hr>
    <table>
      {% for k, v in equipo.items() %}
      <tr><th>{{ k }}</th><td>{{ v }}</td></tr>
      {% endfor %}
    </table>
  </div>
</body>
</html>"""

EQUIPO = {
    "Equipo": "Lenovo ThinkPad L16 Gen 2",
    "Procesador": "Intel Core Ultra 7 255H (16 hilos)",
    "Memoria": "32 GB RAM",
    "Almacenamiento": "SSD NVMe Samsung 1 TB",
    "Gráficos": "Intel Arc 140T (integrados)",
    "Sistema": "Manjaro Linux (KDE), kernel 6.18",
}

@app.route("/")
def index():
    return render_template_string(PAGE, host=socket.gethostname(), equipo=EQUIPO,
                                  now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

@app.route("/health")
def health():
    return {"status": "ok"}
