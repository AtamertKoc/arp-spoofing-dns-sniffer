# 🕵️‍♂️ ARP-Spoofing & DNS-Sniffer

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tool](https://img.shields.io/badge/Security-Tool-red.svg)

A professional **Man-in-the-Middle (MITM)** tool developed in Python using the Scapy library. This tool automates bidirectional ARP poisoning and performs real-time DNS interception.



## 🚀 Key Features
- **Dual-Sided Poisoning:** Targets both the victim and the gateway simultaneously.
- **DNS Interception:** Captures and decodes DNS queries to monitor web traffic.
- **Multithreaded:** Runs spoofing and sniffing in parallel for a seamless connection.
- **Custom Terminal Output:** Features a personalized UI for better monitoring.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AtamertKoc/arp-spoofing-dns-sniffer.git
   cd arp-spoofing-dns-sniffer
2. **Install dependencies:**
   ```bash
   sudo pip3 install -r requirements.txt
3. **Enable IP Forwarding (Critical):**
   ```bash
   sudo sysctl -w net.ipv4.ip_forward=1
## 💻 Usage
**Run the script with root privileges:**
   ```bash 
   sudo python3 main.py
