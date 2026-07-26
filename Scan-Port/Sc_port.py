import socket


host = input(" Entre Host :")
start_port =int(input( "Entre  first Port Scan :"))
end_port =int(input( "Entre  last Port Scan :"))





print("""==================================== \n
Python Port Scanner\n
==================================== \n"""
)

    
print(f" Host :{host}")
host_ip_Address =socket.gethostbyname(host)
print(f" Ip Address {host_ip_Address}")
print(f" Scanning ports {start_port} - {end_port} .....")
def scan_port(start_port,end_port):
    for port in range (start_port,end_port+1):
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

scan_port(start_port,end_port)
        
        

