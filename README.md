<p align="center">
  <img src="banner.png" alt="banner" width="100%">
  <br>
  <span style="font-size: 2em; font-weight: 900;">SPY Network Scanner</span><br><br>
  
  <img src="https://img.shields.io/badge/VERSION-1.0.0-green.svg" alt="version">
  <img src="https://img.shields.io/badge/MAINTAINED-Yes-blue.svg" alt="maintained">
  <img src="https://img.shields.io/badge/WRITTEN_IN-Python-blueviolet.svg" alt="python">
  <br>
  <img src="https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C-lightgrey.svg" alt="platform">
  <img src="https://img.shields.io/badge/python-3.10%2B-blue.svg" alt="version">
</p>

# 👁️ SPY 
> note: This project is developed by me to improve my python skills and understand network. It does nothing related to spying.
> Please use this only on networks that you have permission on. I assume no liability for misuse.

> A lightweight, high-performance CLI utility for local subnet ARP enumeration and socket inspection.
---

## ❗ Note
*   **This is a project where i try to improve my python skills. If you find any bugs or have suggestions, Please report!**
*   **Will add other commands/functions in the future**
*   **Multiple Scan Types, Other kind of tools and etc. will be added**

---

## ⚡ Features

*   **Fast ARP Scanning:** Rapidly discovers live hosts across local subnets using raw packet injection via Scapy.
*   **Spoofing Ability:** It can spoof the IP while looking for alive hosts. But remember, this does not make you untracable.

---
## ℹ️ Commands
```bash

*  spy arpspy 192.168.100.1/24 or 192.168.100.1 (optional : --spoofip 192.168.100.55)
*  spy portspy 192.168.100.1
```
---

## 🛠️ Prerequisites

Before installing, ensure your system meets the operational requirements for raw socket communication:

*   **Python:** Version 3.10 or higher.
*   **Package Manager:** [`uv`](https://github.com/astral-sh/uv) installed globally.
*   **Windows Drivers:** **Npcap** must be installed (bundled with Wireshark or Nmap).
*   **Permissions:** Requires elevated system privileges due to low-level packet manipulation.

---

## 🚀 Installation

Clone the repository and register the global CLI executable or just download the Spy folder:

```bash
git clone https://github.com/RecoWas/spy-scan
cd spy-scan
pip install --editable .
```

## 💻 Usage for Windows (Admin required)
```bash
spy arpspy
spy portspy
```

## 🐧 Usage for Linux (Sudo required)
```bash
sudo ~/.local/bin/spy arp 192.168.1.1/24
```

## ❔ Contact
* **Discord - wasthatrec**
* **Email - maqakv@proton.me**
