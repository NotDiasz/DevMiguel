import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://192.168.100.122:12345/")
print(proxy.multiplicar(2,3))
