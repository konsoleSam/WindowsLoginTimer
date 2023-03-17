import time,psutil,os
tseconds=0
seconds=0
minutes=0
hours=0

def isLocked():
    x=[]
    for p in psutil.process_iter():
        x.append(p.name())
    if 'LogonUI.exe' in x:
        return True
    else:
        return False

while True:
    if not isLocked():
        time.sleep(.1)
        tseconds+=1
        if tseconds>=10:
            tseconds=0
            seconds+=1
        if seconds>=60:
            seconds=0
            minutes+=1
        if minutes>=60:
            minutes=0
            hours+=1
        os.system("cls")
            
        print("hr:{} min:{} sec:{} tenth:{}".format(hours,minutes,seconds,tseconds))
