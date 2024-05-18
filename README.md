# Proyecto de Monitorización de Recursos del Sistema

Este proyecto consiste en un sistema de monitorización de recursos de un equipo, utilizando Python, Flask y MySQL. El sistema consta de un servidor que recibe datos del cliente, un cliente que envía información del sistema, y una aplicación web para visualizar los datos.

## Contenido del Proyecto

1. **Server.py**: Servidor que escucha conexiones de clientes, recibe datos y los guarda en una base de datos MySQL.
2. **Client.py**: Cliente que recopila datos del sistema (CPU, memoria, disco, red, etc.) y los envía al servidor.
3. **app.py**: Aplicación web Flask que muestra los datos almacenados en la base de datos y verifica la conexión con el cliente.
4. **index.html**: Página HTML para visualizar los datos de la base de datos y el estado de la conexión.
5. **requirements.txt**: Lista de dependencias necesarias para ejecutar el proyecto.

## Requisitos

- Python 3.7+
- MySQL
- Las dependencias listadas en `requirements.txt`

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura la base de datos MySQL:
   - Crea una base de datos llamada `mibd`.
   - Crea una tabla `datos` con la siguiente estructura:
     ```sql
     CREATE TABLE datos (
         date DATETIME,
         cpu VARCHAR(10),
         cores INT,
         memory VARCHAR(10),
         memory_total VARCHAR(10),
         disk VARCHAR(10),
         disk_total VARCHAR(10),
         net_sent VARCHAR(10),
         net_recv VARCHAR(10),
         ip_address VARCHAR(15),
         mac_address VARCHAR(17)
     );
     ```

4. Configura las credenciales de la base de datos en los archivos `Server.py` y `app.py`.

## Ejecución

### Servidor

Ejecuta el servidor:
```bash
python Server.py
```

### Cliente

Ejecuta el cliente:
```bash
python Client.py
```

### Aplicación Web

Ejecuta la aplicación web:
```bash
python app.py
```

Abre un navegador web y ve a `http://localhost:3000` para ver la aplicación.

## Estructura del Proyecto

- **Server.py**: 
  - Inicia un servidor que escucha en un puerto específico.
  - Recibe datos de múltiples clientes y los almacena en la base de datos MySQL.

- **Client.py**:
  - Recopila datos del sistema utilizando `psutil`.
  - Envía los datos al servidor cada 5 segundos.

- **app.py**:
  - Proporciona una interfaz web para visualizar los datos.
  - Incluye rutas para obtener los datos más recientes y verificar el estado de la conexión.

- **index.html**:
  - Utiliza Bootstrap para la interfaz.
  - Muestra los datos en una tabla y actualiza la tabla cada 2.5 segundos.
  - Verifica la conexión con el cliente cada 5 segundos.

## Notas Adicionales

- Asegúrate de cambiar las credenciales de la base de datos y las configuraciones del servidor según tu entorno.
- Este proyecto asume que el cliente y el servidor están en la misma red. Ajusta las direcciones IP según sea necesario.

## Créditos

Este proyecto fue desarrollado como una herramienta de monitorización básica para entornos locales, demostrando cómo se pueden usar Python, Flask y MySQL para construir aplicaciones de red y visualización de datos.

## Licencia

Este proyecto está bajo la licencia MIT. Para más información, consulta el archivo LICENSE.