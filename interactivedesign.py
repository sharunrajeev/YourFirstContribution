# importing all libraries
import cadquery as cq
from cadquery import exporters
import pyaudio
import json
from vosk import Model, KaldiRecognizer
import pyttsx3
from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as TkFont 
import os
from word2number import w2n

#loading vosk ml audio recognition model
model = Model(
    r"path\to\any\vosk\voice recognition model"
)

model = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16,
                  channels=1,
                  rate=16000,
                  input=True,
                  frames_per_buffer=8192)

# initialize Text-to-speech engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')  #getting details of current voice
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def say(text):
    engine.say(text)
    engine.runAndWait()


stream.start_stream()

#default name
name = "any_default_name"

coldstart=True

def record_audio():
    while True:
        data = stream.read(44100, exception_on_overflow=False)
        if model.AcceptWaveform(data):
            text = json.loads(model.Result())["text"]
            try:
                if len(text.split()) > 0:
                    return text
            except:
                continue


def introduce():
    say("Welcome everyone to the interactive interface. I hope you are doing well"
        )


def voice_set():
    z = clicked.get()
    if z[-1] == "e":
        engine.setProperty('voice', voices[0].id)
    elif z[-1] == "1":
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[2].id)
    say("Voice changed successfully")


def entry_box_update(text):
    e.delete(0, END)
    e.insert(0, text)
    root.update()

def end_instance():
    b.configure(text="Instance ended. Click to start again.",
                    bg='red',
                    fg='white')
    root.update()

def finalize_design(result):
    exporters.export(result,"output.step")
#     end_instance()
    os.startfile("output.step")

def start():
    #initialize name to change
    global name
    global coldstart
    
    stop = False

    e.delete(0, END)
    b.configure(text="Instance started", bg='green', fg='white')
    root.update()

    temp = "New Instance started successfully."
    if coldstart:
        temp+=" You can take my name, " + str(
        name) + " to start interacting."
    entry_box_update(temp)
    say(temp)
    
    #wait till name is taken
    while coldstart:
        text = record_audio()
        entry_box_update(text)
        text = " " + text + " "
        if name in text:
            temp = "Welcome, my name is " + str(name) + ". How may I help you?"
            entry_box_update(temp)
            say(temp)
            coldstart=False
            break

        if " stop " in text or " end " in text:
            stop = True
            say("Ok, ending the instance")
            end_instance()
            break
            
        if "repeat" in text:
            temp = "New Instance started successfully. You can take my name, " + str(
                name) + " to start interacting."
            entry_box_update(temp)
            say(temp)

    while not stop:
        text = record_audio()
        entry_box_update(text)
        text = " " + text + " "
        if "repeat" in text:
            temp = "Welcome, my name is " + str(name) + ". How may I help you?"
            entry_box_update(temp)
            say(temp)
        if " end " in text or " stop " in text:
            say("Ok, ending the instance")
            end_instance()
            break
        if " name " in text:
            say("Ok, tell me my new name")
            temp = record_audio()
            name = temp
            n2.delete(0, END)
            n2.insert(0, temp)
            say("ok my name is " + str(temp))
            coldstart=True
            start()
            end_instance()
            break
            
        #shapes start here
        if "cube" in text:
            say("OK, designing a cube")
            result = cq.Workplane("XY").box(1, 1, 1)
            finalize_design(result)
#             break
        if "cylinder" in text:
            say("OK, designing a cylinder")
            result = cq.Workplane("XY").circle(10).extrude(50)
            finalize_design(result)
#             break    
        if "cuboid" in text:
            say("OK, designing a cuboid")
            result = cq.Workplane("XY").box(5, 10, 20)
            finalize_design(result)
#             break   
        if "column" in text:
            say("OK, designing a column")
            (L, H, W, t) = (100.0, 20.0, 20.0, 1.0)
            
            pts = [
                (0, H / 2.0),
                (W / 2.0, H / 2.0),
                (W / 2.0, (H / 2.0 - t)),
                (t / 2.0, (H / 2.0 - t)),
                (t / 2.0, (t - H / 2.0)),
                (W / 2.0, (t - H / 2.0)),
                (W / 2.0, H / -2.0),
                (0, H / -2.0),
            ]
            
            result = cq.Workplane("front").polyline(pts).mirrorY().extrude(L)
            finalize_design(result)
#             break
        if "box" in text:
            say("OK, designing a box")
            result = cq.Workplane("front").box(2, 2, 2).faces("+Z").shell(0.05)
            finalize_design(result)
#             break
        if "cone" in text:
            say("Ok, designing a cone")
            result = (cq.Workplane("front").box(4.0, 4.0, 0.25).faces(">Z").circle(1.5).workplane(offset=3.0).rect(0.75, 0.5).loft(combine=True))
            finalize_design(result)
#             break
        if "spring" in text:
            say("Ok, designing a spring")
            r = 0.5  # Radius of the helix
            p = 0.4  # Pitch of the helix - vertical distance between loops
            h = 2.4  # Height of the helix - total height
            
            # Helix
            wire = cq.Wire.makeHelix(pitch=p, height=h, radius=r)
            helix = cq.Workplane(obj=wire)
            
            # Final result: A 2D shape swept along a helix.
            result = (
                cq.Workplane("XZ")  # helix is moving up the Z axis
                .center(r, 0)  # offset isosceles trapezoid
                .polyline(((-0.15, 0.1), (0.0, 0.05), (0, 0.35), (-0.15, 0.3)))
                .close()  # make edges a wire
                .sweep(helix, isFrenet=True)  # Frenet keeps orientation as expected
            )
            finalize_design(result)
#             break
def delet(dummy):
    n2.delete(0, END)


def change_name():
    global name
    coldstart=True
    name = n2.get()
    say("Changed name to " + str(name) + " successfully")
    
#initialize

root = Tk()

# root.geometry("1280x720")

#structures
root.title("Automated Engine Design using Machine Learning")
root.iconbitmap(r"path\to\ico\file")

#logo
myimg = ImageTk.PhotoImage(Image.open("logo\path"))
DMCE_logo = Label(image=myimg, bg="white")
DMCE_logo.grid(row=1, column=1, rowspan=2)

#title label
title_label = Label(
    root,
    text=
    "'Automated Design using Voice Recognition'",
    font=TkFont.Font(family="Times New Roman", size=24, weight="bold"),
).grid(row=1, column=2, columnspan=5, padx=10, pady=10, sticky=W + E)

#subtitle label
subtitle_label = Label(
    root,
    text="Python Project AY:2022-2023",
    font=TkFont.Font(family="Times New Roman", size=15),
    bd=1
).grid(
    row=2,
    column=2,
    #                                padx=10,
    #                                pady=10,
    columnspan=5,
    sticky=W + E)

#desclabel
desc_label = Label(
    root,
    text=
    "\tThis application has been developed as an interface for 'Automated Design using Voice Recognition'.",
    font=TkFont.Font(family="Times New Roman", size=12),
    bd=1,
    anchor=E,
    justify="left").grid(row=3, column=2, columnspan=5, sticky=W + E)

#buttons below description
it = Button(root, text="Introduction", command=introduce)
it.grid(row=4, column=2, pady=10)

#options tab
options = ["Voice Male", "Voice Female 1", "Voice Female 2"]
clicked = StringVar()
clicked.set("Voice Female 1")

#option dropdown
nm = OptionMenu(root, clicked, *options)
nm.grid(row=4, column=3, pady=10)

#setting voices
n1 = Button(root, text="Set voice", command=voice_set)
n1.grid(row=4, column=4, pady=10)

#name
n2 = Entry(root, bg="lightgrey")
n2.insert(0, "Name: " + name)
n2.bind("<1>", delet)
n2.grid(row=4, column=5, pady=10)

#name button
n3 = Button(root, text="Set Name", command=change_name)
n3.grid(row=4, column=6, pady=10)

#credits label
name_label = Label(
    root,
    text=
    "Developed By:\n\nParas Raorane",
    font=TkFont.Font(family="Times New Roman", size=12),
    bd=1,
    anchor=W,
    pady=10,
    padx=10).grid(row=6, column=1, rowspan=2)

#label before terminal
Label(
    root,
    text="Interactive Terminal",
    font=TkFont.Font(family="Times New Roman", size=12, weight="bold"),
).grid(row=5, column=2, columnspan=5, sticky=W + E)

#main entry
e = Entry(root, bg="lightgrey", width=100)  #, borderwidth=10)
e.grid(row=6, column=2, columnspan=5, sticky=W + E)
# #inserting text into the box
e.insert(
    0,
    "Detected text will be displayed here. You can make changes as required.")

b = Button(root, text="Initialize", command=start)
b.grid(row=7, column=2, columnspan=5, pady=10)

root.mainloop()