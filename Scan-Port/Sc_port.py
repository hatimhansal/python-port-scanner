import socket




for port in range (20,100):
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    resultat = s.connect_ex(("google.com",port))
    if resultat == 0 :
        print(f"connect in port {port} Open ")
    else :
        print(f"not connect , Port {port} Close")
    s.close()