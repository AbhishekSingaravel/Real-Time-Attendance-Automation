import cv2
import numpy as np
import pandas as pd
import face_recognition
import os
from datetime import datetime as dt
import csv
import schedule
import time
import sys



 
path = 'images'
img = []
clNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    img.append(curImg)
    clNames.append(os.path.splitext(cl)[0])
print(clNames)



def findEncodings(img):
    encodeList = []
    for img in img:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList



encodeListKnown = findEncodings(img)
print('Encoding Complete')




def markAttendance(name):

    filename = dt.now().strftime("%d-%m-%Y.csv")
    file = open(filename,'')
    with open(filename,'r+') as f:
        headers = ['Name','Date','Time']
        writer = csv.DictWriter(f, delimiter=',', lineterminator='\n',fieldnames=headers)

        
        myDataList = f.readlines()
        nameList = []

        print(myDataList)
        for line in myDataList:
            
            entry = line.split(',')
            nameList.append(entry[0])

            if not filename:
                writer.writeheader()
            
            writer.writerow({'Name': line['name'], 'Date' : line['date'],'Time' : line['time1']})
            
            if name not in nameList:
                now = datetime.now()
                time1 = now.strftime('%H:%M:%S')
                date = now.strftime('%d-%B-%Y')
                f.writelines(f'\n{name}, {date}, {time1}')

                

cap = cv2.VideoCapture(0)
         
while True:
    ret, img = cap.read()
            
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
         
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        name = "Unknown"
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)
         
        if matches[matchIndex]:
            name = clNames[matchIndex].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            
            markAttendance(name)
                    
    cv2.imshow('Webcam',img)
            
    key = cv2.waitKey(1)
    if key == 27:
            break

cap.release()
cv2.destroyAllWindows()




#schedule.every().minutes.at(":10").do(main)

#while True:
#    schedule.run_pending()
#    time.sleep(1)











