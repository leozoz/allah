import requests
import time
import threading


file = open("token.txt", "r")
token = file.read()

headers = {"authorization": token}

file = open("text.txt", "r")
line = file.read()


#MTEzMDUwMzI1MDQ2MjkwMDI3NA.Gp0Z1u.RmdY2FY_26ui1WTRk3U8JzTjOhRBvM4A0lRtBc
#ODIwNjE1MTc3MzgwMDM2Njg4.GRRDuT.FbJ3gvMw6QQbXxtBdJl6NoISWWDpvptB4Xb2sQ


def mesaj(channelID):
    requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages", headers = headers, json = {"content": line} )
    print("Mesaj atıldı")
    
    


def gro():
    while True:
        # 13 minutes of work for gro
        mesaj(691266691522363444)  # blok
        time.sleep(1)
        mesaj(895702150196383884)  # consumable
        time.sleep(1)
        mesaj(895690960586031104)  # pack
        print("growtopia atıldı")
        time.sleep(13 * 60)
        print("growtopia restarted")

def thelast1():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(846671811223355402)
        print("Thelastnemo başladı")
        time.sleep(135 * 60)
        print("thelast1 restart")

def thelast2():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(782718523629633567)
        time.sleep((135+15) * 60)
        print("thelast2 restart")
    
def thelast3():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(846661246303469598)
        time.sleep((135+30) * 60)
        print("thelast3 restart")

def thelast4():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(846673193426354176)
        time.sleep((135+45) * 60)
        print("thelast4 restart")

def thelast5():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(806523338797219860)
        time.sleep((195+1) * 60)
        print("thelast5 restart")

def thelast6():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(733050809314705458)
        time.sleep((195+15) * 60)
        print("thelast6 restart")
    
def thelast7():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(1105154359114875072)
        time.sleep((195+30) * 60)
        print("thelast7 restart")

def thelast8():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(737344235199660123)
        time.sleep((195+45) * 60) #4 saat
        print("thelast8 restart")

def thelast9():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(846678280928624650)
        time.sleep((255+1) * 60)
        print("thelast9 restart")

def thelast10():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(900823352275521546)
        time.sleep((255+15) * 60)
        print("thelast10 restart")

def thelast11():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(762434767912173588)
        time.sleep((255+30) * 60)
        print("thelast11 restart")

def thelast12():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(846671811223355402)
        time.sleep((255+45) * 60)
        print("thelast12 restart")

def thelast13():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(782718823488290826)
        time.sleep((315+1) * 60)
        print("thelast13 restart")

def thelast14():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(733350990010384464)
        time.sleep((315+15) * 60)
        print("thelast14 restart")

def thelast15():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(806498636065931265)
        time.sleep((315+30) * 60)
        print("thelast15 restart")

def thelast16():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(944657054377836645)
        time.sleep((315+45) * 60)
        print("thelast16 restart")

def thelast17():
    while True:
        #uzun olan the last nemo growtopia
        mesaj(1104057271215984741)
        time.sleep((375+1) * 60)
        print("thelast17 restart")


thread1 = threading.Thread(target=gro)
thread2 = threading.Thread(target=thelast1)
thread3 = threading.Thread(target=thelast2)
thread4 = threading.Thread(target=thelast3)
thread5 = threading.Thread(target=thelast4)
thread6 = threading.Thread(target=thelast5)
thread7 = threading.Thread(target=thelast6)
thread8 = threading.Thread(target=thelast7)
thread9 = threading.Thread(target=thelast8)
thread10 = threading.Thread(target=thelast9)
thread11 = threading.Thread(target=thelast10)
thread12 = threading.Thread(target=thelast11)
thread13 = threading.Thread(target=thelast12)
thread14 = threading.Thread(target=thelast13)
thread15 = threading.Thread(target=thelast14)
thread16 = threading.Thread(target=thelast15)
thread17 = threading.Thread(target=thelast16)
thread18 = threading.Thread(target=thelast17)

thread1.start()
print("growtopia")
thread2.start()
time.sleep(60)
thread3.start()
time.sleep(60)
thread4.start()
time.sleep(60)
thread5.start()
time.sleep(60)
thread6.start()
time.sleep(60)
thread7.start()
time.sleep(60)
thread8.start()
time.sleep(60)
thread9.start()
time.sleep(60)
thread10.start()
time.sleep(60)
thread11.start()
time.sleep(60)
thread12.start()
time.sleep(60)
thread13.start()
time.sleep(60)
thread14.start()
time.sleep(60)
thread15.start()
time.sleep(60)
thread16.start()
time.sleep(60)
thread17.start()



