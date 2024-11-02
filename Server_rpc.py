from xmlrpc.server import SimpleXMLRPCServer

def multiplicar(x, y):
    return x * y

server = SimpleXMLRPCServer(("192.168.100.122", 12345))
print("Ouvindo na porta 12345...")
server.register_function(multiplicar, "multiplicar")
server.serve_forever()
