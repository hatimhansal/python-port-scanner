import socket


host = input(" Entre Host :")
start_port =int(input( "Entre  first Port Scan :"))
end_port =int(input( "Entre  last Port Scan :"))





print("""==================================== \n
Python Port Scanner\n
==================================== \n"""
)

    
print(f" Host :{host}")
host_ipAddress =socket.gethostbyname(host)
print(f" Ip Address {host_ipAddress}")
print(" Scanning ports 70-100 ....")
for port in range (start_port,end_port):
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
        
        

