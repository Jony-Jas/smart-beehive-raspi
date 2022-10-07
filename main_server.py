from temp_humi import *
from time_fun import *
from weight import *
while True:
    temp_Hum=temp_hum()
    temp=temp_Hum[0]
    hum=temp_Hum[1]
    wei=weight()
    t=time_curr()
    print("======================")
    print("temp=",temp)
    print("hum=",hum)
    print("weight=",wei)
    print("time=",t)
    print("======================")
    time.sleep(60)

