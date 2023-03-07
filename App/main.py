from tkinter import *
import webbrowser, os, pyautogui, time


def openyt():
    webbrowser.open_new("https://youtube.com")
def openaternos():
    webbrowser.open_new("https://aternos.org/server")
    os.startfile("EasyMC Launcher.lnk")
def openrblx():
    webbrowser.open_new("https://roblox.com/home")
def opentktk():
    webbrowser.open_new("https://tiktok.com")
    time.sleep(6)
    pyautogui.click(1397,545)
def opencforge():
    webbrowser.open_new("https://curseforge.com")
def openscratch():
    webbrowser.open_new("https://scratch.mit.edu")
def openppt():
    os.startfile("PowerPoint.lnk")
def openword():
    os.startfile("Word.lnk")
def openexcel():
    os.startfile("Excel.lnk")
def openamazon():
    webbrowser.open_new("https://www.amazon.co.uk")
def openmcbrck():
    pyautogui.click(11,1439)
    time.sleep(0.25)
    pyautogui.click(11, 1439)
    time.sleep(0.1)
    pyautogui.click(525,627)

window1 = Tk()
window1.title("AutoApp")

window1.config(background="#2743a1")
window1.iconbitmap(r"applogo.ico")

title1 = Label(window1, text="Choose an app or web to open", font=("Algerian", 30), bg="#2743a1", fg="#ffffff").pack()
sp1 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk1 = Button(window1, text="Youtube", font=("Algerian", 15), command=openyt, width=25, bg="#2743a1", fg="#ffffff").pack()
sp2 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk2 = Button(window1, text="Minecraft Server", font=("Algerian", 15), command=openaternos, width=25, bg="#2743a1", fg="#ffffff").pack()
sp3 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk3 = Button(window1, text="Roblox", font=("Algerian", 15), command=openrblx, width=25, bg="#2743a1", fg="#ffffff").pack()
sp4 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk4 = Button(window1, text="Tiktok", font=("Algerian", 15), command=opentktk, width=25, bg="#2743a1", fg="#ffffff").pack()
sp5 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk5 = Button(window1, text="Curseforge", font=("Algerian", 15), command=opencforge, width=25, bg="#2743a1", fg="#ffffff").pack()
sp6 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk6 = Button(window1, text="Scratch", font=("Algerian", 15), command=openscratch, width=25, bg="#2743a1", fg="#ffffff").pack()
sp7 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk7 = Button(window1, text="PowerPoint", font=("Algerian", 15), command=openppt, width=25, bg="#e3752b", fg="#ffffff").pack()
sp8 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk8 = Button(window1, text="Word", font=("Algerian", 15), command=openword, width=25, bg="#375bfa", fg="#ffffff").pack()
sp9 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk9 = Button(window1, text="Excel", font=("Algerian", 15), command=openexcel, width=25, bg="#40b348", fg="#ffffff").pack()
sp10 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk10 = Button(window1, text="Amazon", font=("Algerian", 15), command=openamazon, width=25, bg="#e09b24", fg="#ffffff").pack()
sp11 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()
lk11 = Button(window1, text="Minecraft Bedrock", font=("Algerian", 15), command=openmcbrck, width=25, bg="#2743a1", fg="#ffffff").pack()
sp12 = Label(window1, font=("Algerian", 5), bg="#2743a1").pack()






window1.mainloop()