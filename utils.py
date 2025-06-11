# utils.py

import psutil

def get_system_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "load_avg": psutil.getloadavg() if hasattr(psutil, "getloadavg") else (0, 0, 0)
    }

