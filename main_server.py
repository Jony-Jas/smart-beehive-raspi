from temp_humi import *
from time_fun import *
from weight import *

from pyrebase import pyrebase

firebaseConfig = {
    # Paste Your firebase Config
}


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

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
    
    db.child("temp").update({t:temp})
    db.child("hum").update({t:hum})
    db.child("weight").update({t:wei})
    
    print("At db")
    temp_data = db.child("temp").get()
    for key,value in temp_data.val().items():
        print(key,value)
        
    time.sleep(2)