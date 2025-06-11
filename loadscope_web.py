# loadscope_web.py

from flask import Flask, render_template_string
from utils import get_system_metrics

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta http-equiv="refresh" content="2">
    <title>LoadScope Web Dashboard</title>
    <style>
      body { font-family: sans-serif; background: #121212; color: #00FF90; padding: 2rem; }
      .metric { font-size: 1.5rem; margin: 1rem 0; }
    </style>
  </head>
  <body>
    <h1>LoadScope Web Dashboard</h1>
    <div class="metric">CPU Usage: {{cpu}}%</div>
    <div class="metric">Memory Usage: {{mem}}%</div>
    <div class="metric">Disk Usage: {{disk}}%</div>
    <div class="metric">Load Avg: {{load}}</div>
  </body>
</html>
"""

@app.route("/")
def home():
    metrics = get_system_metrics()
    return render_template_string(
        HTML,
        cpu=metrics["cpu_percent"],
        mem=metrics["memory"],
        disk=metrics["disk"],
        load=metrics["load_avg"]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

