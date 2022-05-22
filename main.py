import socket

a = 10
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((socket.gethostname(), 1022))
soc.listen(5)

while True:
    clt, add = soc.accept()
    print("connected to: {add}")

    obj = {
        1: "Server",
        2: "Client"
    }
    msg = pickle.dumps(obj)
    msg = bytes(f"{len(msg):<{a}}", 'utf-8') + msg
    print(msg)
    clt.send(bytes("Hello World!"))
