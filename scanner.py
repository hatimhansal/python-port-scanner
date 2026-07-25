import socket 

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)


#try :
#    s.connect(("google.com",80))
#    print(" Connect")
#    s.close()
#except Exception as e :
#    print(f"no Connect,{e}")
    


resultat=s.connect_ex(("google.com",80)) 

try :    
    if resultat == 0 :
        print('connect')
    else :
        print("close ")
    s.close()
except Exception as e :
    print("not connect ",e)
