from concurrent.futures import ThreadPoolExecutor
import random
import socket

def check(ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10000)

    try:
        sock.connect((ip, port))
        return True
    except socket.error:
        return False
    finally:
        sock.close()

def save(filename, data):
    with open(filename, 'r+') as file:
        content = file.read()
        file.seek(0)
        file.write(content + "\n" + data)

def finalCheck():
    while True:
 
        randomstr1 = str(random.randint(0, 256))
        randomstr2 = str(random.randint(0, 256))
        randomstr3 = str(random.randint(0, 256))
        randomstr4 = str(random.randint(0, 256))

        ip = f"{randomstr1}.{randomstr2}.{randomstr3}.{randomstr4}"
        port = 25565

        if check(ip, port):
            save("bruh.txt", f"{ip}:25565")
            print(f"Port 25565 is open ({ip})")
        else:
            print(f"Port 25565 is not open ({ip})")

with ThreadPoolExecutor(max_workers=10000) as e:
    while True:
        e.submit(finalCheck)
