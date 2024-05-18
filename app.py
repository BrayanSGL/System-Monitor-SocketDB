from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost' # Cambiar por la dirección de su servidor de base de datos
app.config['MYSQL_USER'] = 'root' # Cambiar por su usuario
app.config['MYSQL_PASSWORD'] = 'passwors' # Cambiar por la contraseña de su usuario
app.config['MYSQL_DB'] = 'midb' # Cambiar por el nombre de la base de datos

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM datos
        ORDER BY date DESC
        LIMIT 10
    ''')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', users=data)

@app.route('/last_date')
def last_date():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT date FROM datos
        ORDER BY date DESC
        LIMIT 1
    ''')
    last_date = cur.fetchone()
    cur.close()
    return jsonify(last_date[0] if last_date else None)

@app.route('/actualizar_datos')
def actualizar_datos():
    cur = mysql.connection.cursor()
    cur.execute('''
        SELECT * FROM datos
        ORDER BY date DESC
        LIMIT 10
    ''')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=3000, debug=True)