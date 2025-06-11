# loadscope_cli.py

from rich.console import Console
from rich.table import Table
from time import sleep
from utils import get_system_metrics

console = Console()

try:
    while True:
        console.clear()
        metrics = get_system_metrics()

        table = Table(title="LoadScope - CLI Monitor")

        table.add_column("Metric", style="bold cyan")
        table.add_column("Value", style="bold green")

        table.add_row("CPU Usage (%)", f"{metrics['cpu_percent']:.2f}")
        table.add_row("Memory Usage (%)", f"{metrics['memory']:.2f}")
        table.add_row("Disk Usage (%)", f"{metrics['disk']:.2f}")
        table.add_row("Load Average (1m, 5m, 15m)", f"{metrics['load_avg']}")

        console.print(table)
        sleep(2)

except KeyboardInterrupt:
    console.print("\n[bold red]Stopped by user[/bold red]")

