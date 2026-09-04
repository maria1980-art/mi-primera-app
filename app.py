from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola desde mi primer contenedor Docker con base de datos!'

@app.route('/db')
def db():
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'db'),
            database=os.getenv('DB_NAME', 'mibasededatos'),
            user=os.getenv('DB_USER', 'maria'),
            password=os.getenv('DB_PASSWORD', 'password123')
        )
        return '✅ Conexión a base de datos exitosa!'
    except Exception as e:
        return f'❌ Error: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
