import socket
import psutil
import uuid
import time

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))

    def send_data(self):
        while True:
            data = self.capture_data()
            self.client.send(str(data).encode())
            time.sleep(5)

    def capture_data(self):
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        cpu = f"{psutil.cpu_percent(interval=1)}%"
        cores = psutil.cpu_count(logical=False)
        memory = f"{psutil.virtual_memory().percent}%"
        memory_total = f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB"
        disk = f"{round(psutil.disk_usage('/').percent, 2)}%"
        disk_total = f"{round(psutil.disk_usage('/').total / (1024**3), 2)} GB"
        net = psutil.net_io_counters()
        net_sent = f"{round(net.bytes_sent / (1024**2), 2)} MB"
        net_recv = f"{round(net.bytes_recv / (1024**2), 2)} MB"
        ip_address = socket.gethostbyname(socket.gethostname())
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

        data = {
            'date': date,
            'cpu': cpu,
            'cores': cores,
            'memory': memory,
            'memory_total': memory_total,
            'disk': disk,
            'disk_total': disk_total,
            'net_sent': net_sent,
            'net_recv': net_recv,
            'ip_address': ip_address,
            'mac_address': mac_address
        }
        return data

if __name__ == '__main__':
    client = Client('192.168.53.125', 8080)
    client.send_data()