import cv2
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "0.0.0.0"
PORT = 8080

# Initialize the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not open the camera.")

# Lock camera access to prevent concurrent reads
camera_lock = threading.Lock()


class CameraHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/video":
            self.send_error(404, "Endpoint not found")
            return

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "multipart/x-mixed-replace; boundary=frame"
        )
        self.send_header("Cache-Control", "no-cache")
        self.send_header("Connection", "close")
        self.end_headers()

        try:
            while True:
                with camera_lock:
                    ret, frame = cap.read()

                if not ret:
                    break

                success, jpeg = cv2.imencode(".jpg", frame)
                if not success:
                    continue

                self.wfile.write(b"--frame\r\n")
                self.wfile.write(
                    b"Content-Type: image/jpeg\r\n\r\n"
                )
                self.wfile.write(jpeg.tobytes())
                self.wfile.write(b"\r\n")

        except (BrokenPipeError, ConnectionResetError, OSError):
            # Client disconnected
            pass

    def log_message(self, format, *args):
        # Optional: suppress per-request logging
        pass


def run():
    server = ThreadingHTTPServer((HOST, PORT), CameraHandler)
    server.daemon_threads = True

    print(f"Streaming on http://127.0.0.1:{PORT}/video")
    print(f"On your local network: http://<computer-ip>:{PORT}/video")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping camera server...")
    finally:
        server.server_close()
        cap.release()


if __name__ == "__main__":
    try:
        run()
    finally:
        if cap.isOpened():
            cap.release()
