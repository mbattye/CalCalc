from flask import Flask, send_from_directory
import subprocess
import os

app = Flask(__name__)

@app.route('/calcalc')
def calcalc():
    return send_from_directory('streamlit_static', 'index.html')

@app.route('/calcalc/<path:path>')
def serve_static(path):
    return send_from_directory('streamlit_static', path)

if __name__ == "__main__":
    if not os.path.exists('streamlit_static'):
        subprocess.run(["streamlit", "run", "main.py", "--browser.serverAddress", "0.0.0.0", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false", "--server.port", "8501"])
    app.run(host='0.0.0.0', port=8080)