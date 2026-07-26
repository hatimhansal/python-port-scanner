import socket
import threading


host = input(" Entre Host :")

first_port =int(input( "Entre First Port Scan :"))
last_port =int(input( "Entre Last Port Scan :"))




print("""==================================== \n
Python Port Scanner\n
==================================== \n"""
)

    
print(f" Host :{host}")
host_ip_Address =socket.gethostbyname(host)
print(f" Ip Address {host_ip_Address} \n")
print(f" Scanning port  .....\n" )
def scan_port(port):
        s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        resultat = s.connect_ex((host,port))
        if resultat == 0 :
            try :
                service_name=socket.getservbyport(port)
                print(f"connect in port {port} Open  {service_name}")
            except Exception as e :
                service_name ='Unknown'
                print(f"connect In port {port} Open  {service_name} ,{e}")
        else :
            print(f"  Port {port} CLOSED")
        s.close()
        
threads=[]

for port in range(first_port,last_port+1) :
    t =threading.Thread(target=scan_port,args=(port,))
    threads.append(t)
    t.start()

for t in threads :
    t.join()