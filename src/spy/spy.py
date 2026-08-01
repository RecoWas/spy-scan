import socket
import ipaddress
import psutil
import typer
import os
from rich.console import Console
from .function import arp_scan, port_scan
from .ui import showdevices, label, showports
app = typer.Typer()
console = Console()

@app.command(name="arpspy")
def arp(
        target: str = typer.Argument(..., help="Target IP or CIDR , e.g. 192.168.100.1/24 "), 
        spoofip: str = typer.Option(None, "--spoofip", help="IP address to spoof")
):
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(f"[red]{label}[/red]")
    try:
        ipaddress.ip_network(target, strict=False)
    except ValueError:
        console.print("[red]✕[/red] Invalid format. Use an IP address or CIDR : 192.168.100.1 or 192.168.100.1/24")
        raise typer.Exit(1)
    with console.status("[bold green]Scanning Network..."):
        if spoofip:
                try:
                    ipaddress.ip_network(spoofip, strict=True)
                except ValueError:
                    console.print("[red]✕[/red] Invalid Spoofed IP. Use an IP address to spoof : 192.168.100.5")
                devices = arp_scan(target, spoofip)
        else:
            devices = arp_scan(target, spoofip=None)
    showdevices(devices, spoofip)

@app.command(name="portspy")
def portspy(
    target: str = typer.Argument(..., help="Target IP address : 192.168.100.34")
):
    os.system('cls' if os.name == 'nt' else 'clear')
    console.print(f"[red]{label}[/red]")
    try:
        ipaddress.ip_network(target, strict=True)
    except ValueError:
        console.print("[red]✕[/red] Invalid format. Use an IP address  : 192.168.100.1")
        raise typer.Exit(1)
    with console.status("[bold green]Scanning Ports..."):
        ports = port_scan(target)
    showports(ports)
if __name__ == "__main__":
    app()





#    def autosubnet():
 #       try:
  #          s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   #         s.settimeout(1.0)
    #        s.connect(("8.8.8.8", 80))
     #       localip = s.getsockname()[0]
      #      s.close()
#
 #           for _, addrs in psutil.net_if_addrs().items():
  #              for addr in addrs:
   #                 if addr.family == socket.AF_INET and addr.address == localip:
    #                    netmask = addr.netmask
     #                   return str(ipaddress.IPv4Network(f"{localip}/{netmask}", strict=False))
      #      return None
       # except Exception:
        #    return None


