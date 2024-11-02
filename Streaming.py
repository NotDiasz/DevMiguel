from http.server import BaseHTTPRequestHandler, HTTPServer
import time

class StreamingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'video/mp4')
        self.end_headers()

        # Abra o arquivo de vídeo em modo binário
        with open("video.mp4", "rb") as file:
            data = file.read(1024)  # Lê 1024 bytes do arquivo
            while data:
                self.wfile.write(data)
                data = file.read(1024)  # Continue lendo até o final

if __name__ == '__main__':
    server_address = ('192.168.100.116', 12345)  # Substitua pelo seu endereço IP e porta
    server = HTTPServer(server_address, StreamingHandler)
    print(f"Starting server on http://{server_address[0]}:{server_address[1]}, press Ctrl+C to stop")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    server.server_close()

