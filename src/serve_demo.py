#!/usr/bin/env python3
"""
HTTP server for the /docs browser demo.

Serves the static files with proper MIME types for TensorFlow.js model loading.
"""

import argparse
import http.server
import socketserver
import socket
import os
from pathlib import Path


def get_local_ip():
    """
    Get the local network IP address.

    Returns:
        str: Local IP address or 'unknown' if detection fails
    """
    try:
        # Create a socket to find the local IP
        # Doesn't actually connect, just determines routing
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "unknown"


def serve_demo(port=8080, directory="docs"):
    """
    Start an HTTP server for the browser demo.

    Args:
        port (int): Port number to serve on (default: 8080)
        directory (str): Directory to serve (default: "docs")
    """

    class DemoHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory=directory, **kwargs)

        def end_headers(self):
            # Add CORS headers for local testing
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
            super().end_headers()

        def guess_type(self, path):
            """Ensure correct MIME types for model files."""
            mimetype = super().guess_type(path)
            if path.endswith(".bin"):
                return "application/octet-stream"
            if path.endswith(".json"):
                return "application/json"
            return mimetype

    # Validate directory exists
    docs_path = Path(directory)
    if not docs_path.exists():
        print(f"Error: Directory '{directory}' does not exist.")
        print(f"Expected path: {docs_path.absolute()}")
        return

    # Start server
    local_ip = get_local_ip()

    # Allow address reuse to avoid "Address already in use" errors
    socketserver.TCPServer.allow_reuse_address = True

    with socketserver.TCPServer(("0.0.0.0", port), DemoHTTPRequestHandler) as httpd:
        print(f"🍀 Four-Leaf Clover YOLO Demo Server")
        print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"📂 Serving: {docs_path.absolute()}")
        print(f"🌐 Local:   http://localhost:{port}")
        print(f"📱 Network: http://{local_ip}:{port}")
        print(f"🔌 Press Ctrl+C to stop\n")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped.")


def main():
    """CLI entrypoint for serve-demo command."""
    parser = argparse.ArgumentParser(
        description="Serve the Four-Leaf Clover YOLO browser demo."
    )
    parser.add_argument(
        "--port", type=int, default=8080, help="Port to serve on (default: 8080)"
    )
    parser.add_argument(
        "--directory",
        type=str,
        default="docs",
        help="Directory to serve (default: docs)",
    )

    args = parser.parse_args()
    serve_demo(port=args.port, directory=args.directory)


if __name__ == "__main__":
    main()
