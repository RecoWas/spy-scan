import ipaddress
import socket
import psutil
import sys
from rich.console import Console
from scapy.all import *
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor 

console = Console()
wnports = {
    80: "HTTP",
    430: "HTTPS",
    3389: "RDP",
    8080: "HTTP-Alt",
    4444: "Metasploit/Backdoor",
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    445: "SMB",
    1025: "Unassigned"

}

def arp_scan(target, spoofip):
    
    broadcast = "FF:FF:FF:FF:FF:FF"
    ether_packet = Ether(dst=broadcast)
    if spoofip:
        arp_packet = ARP(op=1, pdst=target, psrc=spoofip)
    else:
            arp_packet = ARP(op=1, pdst=target)
    finalpacket = ether_packet / arp_packet
    devices = []
    try:
        ifacee = conf.route.route(target)[0]
    except Exception:
        return devices

    alive, _ = srp(finalpacket, timeout=3, verbose=False, iface=ifacee)
    for _, received in alive:
        replytime = datetime.fromtimestamp(received.time).strftime("%H:%M:%S")
        devices.append({"IP": received.psrc, "MAC": received.hwsrc, "TIME": replytime})
    return devices

def check_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2.0)
    result = s.connect_ex((target, port))
    s.close()

    return port, result == 0 

def port_scan(target):
    results = []

    with ThreadPoolExecutor(max_workers=len(wnports)) as executor:
        futures = [executor.submit(check_port, target, port) for port in wnports]

        for future in futures:
            port, is_open = future.result()
            
            state = "Open" if is_open else "Closed"
            results.append({"port": str(port), "state": state})

    return results


if __name__ == "__main__":
    console.print("[red]✕ Error: Do not run this script directly with Python.[/red]")
    console.print("Execute it using the installed command: [bold cyan]spy[/bold cyan]")
    sys.exit(1)
