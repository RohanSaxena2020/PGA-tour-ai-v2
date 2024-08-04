import subprocess
import os
import argparse
import time

def run_command(command, shell=True):
    process = subprocess.Popen(command, shell=shell)
    return process

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=8000, help='Port for the backend server')
    parser.add_argument('--frontend-port', type=int, default=5500, help='Port for the frontend server')
    args = parser.parse_args()

    # Change to the project root directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Start the backend server
    server_process = run_command(f"python server/server.py --port {args.port}")

    # Build and start frontend server
    frontend_process = run_command(f"cd UI && npm run start")

    print(f"Backend is running on port {args.port}")
    print(f"Frontend is running on port {args.frontend_port}")
    print("Application is running. Press CTRL+C to stop.")

    try:
        # Keep the script running
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping the application...")
        server_process.terminate()
        frontend_process.terminate()