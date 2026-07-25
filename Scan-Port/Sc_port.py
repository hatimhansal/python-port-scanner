import socket


host = input(" Entre Host :")





print("""==================================== \n
Python Port Scanner\n
==================================== \n"""
)

    
print(f" Host :{host}")
host_ipAddress =socket.gethostbyname(host)
print(f" Ip Address {host_ipAddress}")
print(" Scanning ports 70-100 ....")
for port in range (70,100):
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    resultat = s.connect_ex((host,port))
        
    if resultat == 0 :
        try :
            service_name=socket.getservbyport(port)
            print(f"connect in port {port} Open  {service_name}")
            s.close()
        except Exception as e :
            service_name ='Unknown'
            print(f"connect in port {port} Open  {service_name} ,{e}")
    else :
        print(f"not connect , Port {port} Close")
        s.close()
        
        

