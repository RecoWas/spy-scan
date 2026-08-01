from .function import wnports
import rich
import time
from rich.console import Console
from rich.table import Table

console = Console()
label = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⣄⠀⠰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⠀⠀⠀⠀⠀⠘⣆⠀⠀⠀⢸⡄⠀⢳⠀⠀⢀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⡄⠀⠀⢳⡄⠀⠀⠀⠀⠸⡆⡄⠀⠀⣿⠀⢸⡄⠀⠈⣇⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠙⢆⠀⠀⢿⡄⠀⠀⠀⠀⣧⢸⠀⠀⣿⠀⢸⡇⠀⠀⢸⠈⡆⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣹⣧⣌⣧⣀⣸⣇⢳⡄⠀⠀⣿⢘⡇⢀⣿⠀⣸⢱⡀⠀⢸⠀⣿⠀⠀⢸⡇⠀⢀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⡿⠿⣟⠉⠉⢹⡇⢹⠁⣿⡟⠙⣿⠲⢶⣿⣸⡃⣼⠃⣰⡏⣼⠇⢀⣿⠀⣿⠀⠀⣾⠃⠀⢸⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⡿⠟⢋⡁⠠⣄⠘⣷⡀⢸⣿⣸⣤⣿⡇⣰⡿⢠⣿⢣⡟⣽⢿⣶⣿⣴⡿⢀⣼⡏⣸⡏⠀⣸⡿⠀⢀⡏⠀⠀⡼⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠟⠉⢠⡀⠀⠙⣦⡘⣷⣘⣧⣿⣿⣿⣿⣿⣰⣿⣷⣿⣿⣿⣿⣿⣾⣿⣾⡿⣳⣿⣟⣴⡟⢀⣼⡿⡽⠀⡾⢠⠀⡼⠃⡼⠀⠀⣠⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⡿⠛⠁⠀⠀⢀⠙⣮⣷⣽⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣴⣿⢟⡼⣣⠞⣴⣣⡞⢁⡼⠃⢀⡴⠃⠀⣀⡄
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠀⠀⠀⠠⣄⠈⢷⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣟⣵⣾⡿⣋⣴⣟⣡⣶⠟⣁⣴⣾⣿⠇
⠀⠀⠀⠀⠀⠀⢀⣾⡿⠃⠀⠀⣄⠀⢳⣜⣷⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⠟⠁⠀
⠀⠀⠀⠀⠀⢠⣿⠏⠀⢀⠀⢦⡘⢦⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⢻⣿⣿⣿⠛⠻⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀⠀⠀
⠀⠀⠀⠀⣰⡿⠃⠀⠀⢈⢶⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡖⠒⠚⣿⣿⡿⠀⠀⠀⠀⠀⠀⠈⠉⠉⢛⣿⣿⣿⣿⣿⣿⡿⣿⣿⣯⣅⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⡿⠁⠀⠀⣀⠈⢳⣾⣿⣿⣿⣿⣿⠟⣻⣿⣿⠀⢈⣿⣿⣿⣿⣿⣿⣿⠯⠍⠀⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⡿⢶⣄⠉⠛⠇⠀⠀⠀⠀⠀⠀
⠀⠀⢠⡿⠁⠀⠀⠀⠈⣿⣿⣿⣿⣿⢿⣿⡿⠤⣨⣿⣿⣿⣼⣿⣿⣿⣿⣿⡿⠏⠀⠂⠈⠛⢿⣿⠃⠀⠀⠀⠀⠀⠀⣰⣿⣿⣟⣋⣉⣉⣉⠛⠻⢷⡌⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡾⠁⠀⠀⠀⣠⣾⣿⣿⣿⠟⠁⠘⣿⣶⡧⠖⢸⡿⣿⣿⣿⣿⡿⣿⣿⠗⠀⠀⠈⢿⣦⣾⡟⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡿⠯⢭⣍⡙⠓⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡼⠀⠀⠀⠀⣴⣿⣿⣿⠟⠀⠀⠀⠀⠹⣿⣥⢖⣠⣤⠟⠉⠛⠛⢻⠁⡀⠀⢀⣸⣷⣠⣿⡟⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣥⣤⣍⡛⠢⣄⠙⠳⣄⠉⢦⡀⠀⠀⠀⠀⠀⠀⠀
⠰⠁⠀⠀⢀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣾⣽⣷⣖⡆⢀⣠⣸⣤⣿⣆⣈⣿⣿⡿⠋⠀⠀⢀⣠⣾⣿⣿⣿⣿⣭⣛⠻⢶⡀⠉⠳⢌⠳⠀⠈⠳⡄⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣾⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⠿⣿⣶⣿⣿⣿⣿⣿⠿⠟⠉⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣟⠿⣦⡙⠄⠀⠀⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣾⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⡿⢿⣝⡻⣟⢮⢣⠀⠙⣆⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣾⡟⠁⠀⠀⢀⣠⣴⣶⣶⣶⠷⣷⣶⣶⣶⣶⣦⣤⣤⣤⣴⣶⣶⣶⣿⣿⣿⣿⣿⣿⡻⢿⣿⢶⣍⠻⣝⢷⣌⠻⣮⠋⢧⢧⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⠋⠀⢀⣴⡾⠟⠋⠉⢠⠏⢀⡞⢩⠞⢩⡟⣹⠟⣹⠏⣿⢻⣿⢹⡿⣿⢻⢿⢿⣿⣿⣿⣦⠙⣇⠘⢧⡈⢦⠙⢧⠈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠐⠃⠀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠈⢠⠏⠀⡞⢠⠃⠀⢿⠀⠋⠘⡇⢸⠇⡏⢸⢸⠀⠹⣇⢳⠙⣧⠘⠀⠀⢳⡘⠆⠈⣧⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠈⠀⠀⠀⠇⡼⠀⠀⠏⠼⠀⠀⢻⢸⠄⠘⡆⠀⠀⠀⡇⠀⠀⠸⡄⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠘⠀⠀⠃⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

def showdevices(devices, spoofip):
    if not devices:
        console.print("[red]No hosts found[/red]")
        return
    if spoofip:
        console.print(f"Current Spoofing IP : {spoofip}")
    table = Table(title="ARP Scan")
    table.add_column("IP Address", style="red")
    table.add_column("MAC Address", style="red")
    table.add_column("Time", style="white")

    for device in devices:
        table.add_row(device["IP"], device["MAC"], device["TIME"])

    console.print(table)


def showports(scanresult):
    table = Table(title="Port Scan")
    table.add_column("Open Ports", justify="left", style="green")
    table.add_column("Closed Ports", justify="center", style="red")
    table.add_column("Service", justify="right", style="white")

    for item in scanresult:
        port_num = int(item["port"])
        service = wnports.get(port_num, "Unknown")
        
        if item["state"] == "Open":
            table.add_row(item["port"], "", service)
        else:
            table.add_row("", item["port"], service)

    console.print(table)

if __name__ == "__main__":
    console.print("[red]✕ Error: Do not run this script directly with Python.[/red]")
    console.print("Execute it using the installed command: [bold cyan]spy[/bold cyan]")
    sys.exit(1)
