import socket
import json
import mysql.connector


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.host, self.port))
        self.server.listen(5)
        print(f"Escuchando en {self.host}:{self.port}")

    def start(self):
        while True:
            client_socket, client_address = self.server.accept()
            print(f"Conexión de {client_address}")
            client_handler = ClientHandler(client_socket)
            client_handler.start()
            print(f"Cliente {client_address} desconectado")

class ClientHandler:
    def __init__(self, client_socket):
        self.client_socket = client_socket
        self.database = Database()  # Instanciar la clase Database

    def start(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if not data:
                    break
                data = data.decode()
                print("Datos recibidos del cliente:")
                #volver a convertir el string en un diccionario
                data = data.replace("'", '"')
                data = json.loads(data)
                print('recibido')
                # Insertar los datos recibidos en la base de datos
                self.database.insert_data(data)
            except Exception as e:
                print(f"Error: {e}")
                break
        self.client_socket.close()

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost', # Cambiar por la dirección de su servidor de base de datos
            user='root', # Cambiar por su usuario
            password='password', # Cambiar por la contraseña de su usuario
            database='mibd' # Cambiar por el nombre de la base de datos
        )

    def insert_data(self, data):
        cursor = self.connection.cursor()
        query = "INSERT INTO datos (date, cpu, cores, memory, memory_total, disk, disk_total, net_sent, net_recv, ip_address, mac_address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (data['date'], data['cpu'], data['cores'], data['memory'], data['memory_total'], data['disk'], data['disk_total'], data['net_sent'], data['net_recv'], data['ip_address'], data['mac_address'])
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()


if __name__ == '__main__':
    host = socket.gethostbyname(socket.gethostname())
    server = Server(host, 8080)
    server.start()
