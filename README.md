# 🕵️‍♂️ ARP Spoofing & DNS Sniffer

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

A professional Man-in-the-Middle (MITM) tool built with Python and Scapy. This tool intercepts local network traffic by poisoning ARP tables and analyzes DNS queries in real-time.



## 🛠 Project Structure
- **`main.py`**: The entry point of the application.
- **`core/`**: Contains logic for spoofing and packet sniffing.
- **`requirements.txt`**: Lists necessary libraries.

## ⚙️ Configuration
Make sure to enable IP forwarding on your Linux machine before starting:
```bash
sudo sysctl -w net.ipv4.ip_forward=1
