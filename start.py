import os
import subprocess
import time

def run_command(command, shell=True):
    process = subprocess.Popen(command, shell=shell)
    return process

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    frontend_port = int(os.environ.get("FRONTEND_PORT", 5500))

    # Start the backend server
    server_process = run_command(f"python server/server.py --port {port}")

    # Start a simple HTTP server for the frontend
    frontend_process = run_command(f"cd UI && python -m http.server {frontend_port}")

    print(f"Backend is running on port {port}")
    print(f"Frontend is running on port {frontend_port}")
    print("Application is running. Press CTRL+C to stop.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping the application...")
        server_process.terminate()
        frontend_process.terminate()