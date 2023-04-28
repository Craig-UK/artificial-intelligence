import tkinter as tk
from tkinter import * 
import cv2
from PIL import Image, ImageTk #need import 'Image Magic'
import os
import numpy as np
import cv2
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.optimizers import Adam
from keras.layers import MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
import threading
import sqlite3

def GetEmotion(videoname):

    cur_path = os.path.dirname(os.path.abspath(__file__))
    
    rel_path = "media/" + videoname
    abs_file_path = os.path.join(cur_path, rel_path)

    model_file = "model.h5"
    abs_model_path = os.path.join(cur_path, model_file)

    haarcascade = "haarcascade_frontalface_default.xml"
    haar_path = os.path.join(cur_path, haarcascade)

    emotion_model = Sequential()
    emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))
    emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(Dropout(0.25))
    emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(MaxPooling2D(pool_size=(2,2)))
    emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
    emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
    emotion_model.add(Dropout(0.25))
    emotion_model.add(Flatten())
    emotion_model.add(Dense(1024, activation='relu'))
    emotion_model.add(Dropout(0.5))
    emotion_model.add(Dense(7, activation='softmax'))
    emotion_model.load_weights(abs_model_path) #Add model.h5 to backend folder
    cv2.ocl.setUseOpenCL(False)

    emotion_dict =  {0: "   Angry   ", 1: "   Disgusted   ", 2: "   Fearful   ", 3: "   Happy   ", 4: "   Neutral   ", 5: "   Sad   ", 6: "   Surprised   "}

    emoji_dist={0:os.path.join(cur_path,"emojis/angry.png"),1:os.path.join(cur_path,"emojis/disgust.png"),2:os.path.join(cur_path,"emojis/fear.png"),3:os.path.join(cur_path,"emojis/happy.png"),4:os.path.join(cur_path,"emojis/neutral.png"),5:os.path.join(cur_path,"emojis/sad.png"),6:os.path.join(cur_path,"emojis/surprised.png")}

    global last_frame1
    last_frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
    global cap1
    show_text=[0]
    global frame_number

    global video_file_name
    video_file_name = r"{}".format(abs_file_path)

    global happy, angry, disgust, fear, neutral, sad, surprised, theMood
    happy = 0
    angry = 0
    disgust = 0
    fear = 0
    neutral = 0
    sad = 0
    surprised = 0
    theMood = 'test'

    global cap1
    cap1 = cv2.VideoCapture(video_file_name)

    global length
    length = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))

    global frame_number
    frame_number = 0
    

    def show_subject():
        global video_file_name
        if not cap1.isOpened():
            print("Can't open the camera")
        global frame_number
        frame_number += 1
        if frame_number >= length  - 1:
            root.quit()
        else:
            cap1.set(1, frame_number)
            flag1, frame1 = cap1.read()
            frame1 = cv2.resize(frame1,(600,500))
            bounding_box = cv2.CascadeClassifier(haar_path) #Add haarcascade_frontalface_default.xml file to backend folder
            gray_frame = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
            num_faces = bounding_box.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in num_faces:
                cv2.rectangle(frame1, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2)
                roi_gray_frame = gray_frame[y:y + h, x:x + w]
                cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray_frame, (48, 48)), -1), 0)
                prediction = emotion_model.predict(cropped_img)
                maxindex = int(np.argmax(prediction))
                cv2.putText(frame1, emotion_dict[maxindex], (x+20, y-60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                show_text[0] = maxindex
            if flag1 is None:
                print("Major Error!")
            elif flag1:
                global last_frame1
                last_frame1 = frame1.copy()
                pic = cv2.cvtColor(last_frame1, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(pic)
                imgtk = ImageTk.PhotoImage(image=img)
                lmain.imgtk = imgtk
                lmain.configure(image=imgtk)
                root.update()
                lmain.after(10, show_subject)
                lmain.after(10, show_avatar)
                average_mood(show_text[0])
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print('Quitting early, data from interview will not be saved')
            exit()

    def show_avatar():
        frame2 = cv2.imread(emoji_dist[show_text[0]])
        frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)
        img2 = Image.fromarray(frame2)
        imgtk2 = ImageTk.PhotoImage(image=img2)
        lmain2.imgtk2=imgtk2
        lmain3.configure(text=emotion_dict[show_text[0]], font=('comic sans',45,'bold'))

        lmain2.configure(image=imgtk2)
        root.update()
        #lmain2.after(10, show_avatar)

    def average_mood(numberIn):
        global angry
        global happy
        global disgust
        global fear
        global neutral
        global sad
        global surprised

        match numberIn:
            case 0:
                angry += 1
            case 1:
                disgust += 1
            case 2:
                fear += 1
            case 3:
                happy += 1
            case 4:
                neutral += 1
            case 5:
                sad += 1
            case 6:
                surprised += 1
        
        list1 = [angry, disgust, fear, happy, neutral, sad, surprised]
        maxValue = max(list1)

        index = list1.index(maxValue)
        
        frame3 = cv2.imread(emoji_dist[index])
        frame3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2RGB)
        img3 = Image.fromarray(frame3)
        imgtk3 = ImageTk.PhotoImage(image=img3)
        lmain4.imgtk3=imgtk3
        lmain5.configure(text=(f"Average Emotion: {emotion_dict[index]}"), font=('comic sans',45,'bold'))

        lmain4.configure(image=imgtk3)
        root.update()

    def write_emotion():
        global angry
        global happy
        global disgust
        global fear
        global neutral
        global sad
        global surprised

        global video_file_name

        list1 = [angry, disgust, fear, happy, neutral, sad, surprised]
        maxValue = max(list1)

        index = list1.index(maxValue)

        match index:
            case 0: 
                theMood = 'Angry'
            case 1:
                theMood = 'Disgust'
            case 2:
                theMood = 'Fear'
            case 3:
                theMood = 'Happy'
            case 4:
                theMood = 'Neutral'
            case 5:
                theMood = 'Sad'
            case 6:
                theMood = 'Surprised'

        print(theMood)
        return theMood

    
    root=tk.Tk()
    lmain = tk.Label(master=root,padx=50,bd=10)
    lmain2 = tk.Label(master=root,bd=10) #emoji
    lmain3 = tk.Label(master=root,bd=10,fg='#CDCDCD',bg='black') #emoji label
    lmain4 = tk.Label(master=root, bd=10) #emoji average
    lmain5 = tk.Label(master=root,bd=10,fg='#CDCDCD',bg='black') #emoji average label
    lmain.pack(side=LEFT)
    lmain.place(x=50,y=250)
    lmain3.pack()
    lmain3.place(x=960,y=250)
    lmain2.pack(side=RIGHT)
    lmain2.place(x=1040,y=350)
    lmain5.pack()
    lmain5.place(x=200,y=0)
    lmain4.pack(side=TOP)
    lmain4.place(x=700, y=100)

    root.title("Photo to Emoji")
    root.geometry("1400x900+100+10")
    root['bg']='black'
    exitButton = Button(root, text='Quit', fg='red', command=root.destroy, font=('arial',25,'bold')).pack(side=BOTTOM)
    threading.Thread(target=show_subject).start()
    threading.Thread(target=show_avatar).start()
    root.mainloop()
    
    root.wait_window(root)
    return write_emotion()