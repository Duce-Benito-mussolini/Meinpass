import tkinter as tk
import string as st
import random
import ctypes
import pyperclip
import tkinter.messagebox as tkm

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)
except:
    pass

WHITE = "#ffffff"
DARKBLUE = "#16212c"

class Copy():
    def copy(self, entry):
        pyperclip.copy(entry.get())


class Renzoku():
    def ifrenzoku(self, *dainyu, **hantei):
        kaerichi = ""
        count = 0
        for i in hantei:
            if hantei[i]:
                kaerichi += dainyu[count]
            count += 1
        return kaerichi


class FileManeger():
    def write(self):
        with open("data.sav", mode="a") as f:
            f.write("\n" + contents_name.get() + "\n" + passen.get())
    
    def shokichi(self, nambamme):
        with open("data.sav") as f:
            kaerichi = f.readlines()[0][nambamme]
        return kaerichi


class Hozon():
    def hozon(self):
        filer = FileManeger()
        if contents_name.get() == "":
            pass
        else:
            filer.write()


class Kisomojiretsuteigi():
    def kisomojiretsu(self, eiko, eioo, suji, kigo):
        maeteigi = {"eiko": eiko, "eioo": eioo, "suji": suji, "kigo": kigo}
        ifrencall = Renzoku()
        return ifrencall.ifrenzoku(
            st.ascii_lowercase, 
            st.ascii_uppercase, 
            st.digits, 
            st.punctuation,
            **maeteigi)


class Rancon():
    def randomer_one(self, given_sen):
        try:
            return given_sen[random.randint(0, (len(given_sen))-1)]
        except ValueError:
            return "ERROR"
    
    def randomer_charas(self, mojisuu, given_sen):
        kaerichi = ""
        for i in range(mojisuu):
            kaerichi += self.randomer_one(given_sen)
        return kaerichi


class TFF():
    def toggle(self, input_):
        return not input_


class On_Off():
    def onoff(self, input_):
        if input_:
            return "ON"
        else:
            return "OFF"
        return "ERROR"


class Button_Modern():
    def koniro(self, tex, wx, wy, com):
        button = tk.Button(
            text=tex,
            fg=WHITE,
            bg=DARKBLUE,
            activeforeground=WHITE,
            activebackground=DARKBLUE,
            width=6,
            command=com)
        button.place(x=wx, y=wy)


class Label_Modern(Button_Modern):
    def koniro(self, tex):
        self.label = tk.Label(
            text = tex,
            fg=WHITE,
            bg=DARKBLUE)
    
    def prepre(self, wx, wy):
        self.label.place(x=wx, y=wy)
    
    def destroy(self):
        self.label.destroy()


class Buttonshories():
    def __init__(self, nambamme):
        filer = FileManeger()
        self.whether_on = int(filer.shokichi(nambamme))
        self.label = Label_Modern()
        self.label.koniro(On_Off().onoff(self.whether_on))
    
    def independence(self, x, y):
        self.label.prepre(x, y)
    
    def shori(self, x, y):
        self.whether_on = TFF().toggle(self.whether_on)
        self.label.destroy()
        self.label.koniro(On_Off().onoff(self.whether_on))
        self.independence(x, y)


class Run_():
    def hyoji(self):
        passen.delete(0, tk.END)
        passen.insert(
            tk.END, Rancon().randomer_charas(
                int(inpmojisu.get()),
                Kisomojiretsuteigi().kisomojiretsu(
                    eikoshori.whether_on,
                    eiooshori.whether_on,
                    sujishori.whether_on,
                    kigoshori.whether_on)))








root = tk.Tk()
root.title("Meinpass")
root.geometry("854x480")
root.resizable(0, 0)
root.configure(bg=DARKBLUE)


contents_label = Label_Modern()
contents_label.koniro("コンテンツ名")
contents_label.prepre(380, 40)
contents_name = tk.Entry(root, width=64)
contents_name.place(x=100, y=70)

password_label = Label_Modern()
password_label.koniro("パスワード名")
password_label.prepre(380, 170)
passen = tk.Entry(root, width=64)
passen.place(x=100, y=200)

# SPINBOX
inpmojisu = tk.Spinbox(root, from_=1, to=999, increment=1, width=3)
inpmojisu.delete(0, 1)
inpmojisu.insert(0, 8)
inpmojisu.place(x=275, y=280)
# /SPINBOX

eikoshori = Buttonshories(0)
eikoshori.independence(300, 360)
eiko_c = Button_Modern()
eiko_c.koniro("英(小)", 280, 400, lambda:eikoshori.shori(300,360))

eiooshori = Buttonshories(1)
eiooshori.independence(370, 360)
eioo_c = Button_Modern()
eioo_c.koniro("英(大)", 350, 400, lambda:eiooshori.shori(370,360))

sujishori = Buttonshories(2)
sujishori.independence(440, 360)
suji_c = Button_Modern()
suji_c.koniro("数字", 420, 400, lambda:sujishori.shori(440,360))

kigoshori = Buttonshories(3)
kigoshori.independence(510, 360)
kigo_c = Button_Modern()
kigo_c.koniro("記号", 490, 400, lambda:kigoshori.shori(510,360))

run = Button_Modern()
run.koniro("実行", 340, 275, Run_().hyoji)

on_button_copy = Copy()
passcopy = Button_Modern()
passcopy.koniro("コピー", 420, 275, lambda:on_button_copy.copy(passen))

contencopy = Button_Modern()
contencopy.koniro("コピー", 385, 110, lambda:on_button_copy.copy(contents_name))

hozoner = Hozon()
saving = Button_Modern()
saving.koniro("保存", 500, 275, hozoner.hozon)

root.mainloop()