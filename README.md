# Python Webcam Streaming Server

A lightweight HTTP webcam streaming server built with Python, OpenCV, and the built-in `http.server` module. It captures live video from a connected camera and streams JPEG frames to a web browser using MJPEG (Motion JPEG).

## Features

- Live webcam streaming over HTTP.
- MJPEG video output using multipart responses.
- Multi-client HTTP handling with `ThreadingHTTPServer`.
- Basic handling of client disconnections.
- Automatic camera resource cleanup on shutdown.

## Requirements

- Python 3.8 or later
- A connected webcam or compatible camera
- OpenCV for Python

## Installation

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_REPOSITORY_DIRECTORY
```

Replace the placeholders with your Git repository URL and directory name.

### 2. Install dependencies

```bash
pip install opencv-python
```

## Usage

Start the server:

```bash
python camera_server.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:8080/video
```

The browser should display the live camera stream.

### Access from another device

To view the stream from another device on the same local network:

1. Find the local IP address of the computer running the server.
2. Ensure both devices are connected to the same network.
3. Open this URL on the other device:

```text
http://YOUR_COMPUTER_IP:8080/video
```

Replace `YOUR_COMPUTER_IP` with the server computer's local IP address.

You may need to allow inbound connections on port `8080` in your firewall.

## Configuration

The server settings are defined in `camera_server.py`:

- `HOST = "0.0.0.0"` — listens on available network interfaces.
- `PORT = 8080` — HTTP server port.
- `cv2.VideoCapture(0)` — opens the default camera. Change `0` if a different camera index is required.

## Stopping the Server

Press `Ctrl+C` in the terminal to stop the server and release the camera.

## Troubleshooting

**Camera not opening**

- Verify that the camera is connected and working.
- Close other applications using the camera.
- Check camera permissions.
- Try another camera index in `cv2.VideoCapture()`.

**Stream not loading**

- Confirm that the Python server is running.
- Check that the URL ends in `/video`.
- Check firewall settings and network connectivity.
- Look for camera or OpenCV errors in the terminal.

## Security Notice

This server does not provide authentication or HTTPS encryption. Do not expose it directly to the public internet. Use it only on a trusted network unless appropriate access controls and secure transport are added.

## Technologies

- Python
- OpenCV
- HTTP server
- MJPEG streaming

## License

This project is available under the MIT License if you choose to distribute it under that license. Add a `LICENSE` file containing the MIT License text before claiming the project is MIT-licensed.
