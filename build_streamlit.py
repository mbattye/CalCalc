import subprocess
import os

if __name__ == "__main__":
    if not os.path.exists('streamlit_static'):
        subprocess.run(["streamlit", "run", "main.py", "--browser.serverAddress", "0.0.0.0", "--server.enableCORS", "false", "--server.enableXsrfProtection", "false", "--server.port", "8501"])