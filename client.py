import socket
import pickle

a = 10
soc = socket.socket(socket.AF_IRDA, socket.SOCK_STREAM)
soc.connect((socket.gethostname(), 1042))

try:
    while True:
        rec_info = b''
        rec_msg = True
        while True:
            msg = soc.recv(16)
            if rec_msg:
                x = msg[:a]
                print(f"The length of message: {x}")
                rec_msg = False

            rec_info += msg
            if len(rec_info) - a == x:
                print("recived complite info")
                info = rec_info[a:]
                print(info)
                m = pickle.loads(info)
                print(m)
                rec_msg = True
                rec_info = b''
            print(rec_info)

except:
    pass
