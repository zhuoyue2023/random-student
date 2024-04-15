from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import pickle
from sys import argv
import os
import random
import time
import winsound

up = []

if len(argv) != 1:
    f = open(argv[1],'rb')
    up = pickle.load(f)
    f.close()
    # c = {}
    # while True:
    #     p = f.readline()
    #     if not p: break
    #     if p == '': continue
    #     c[p] = 0
    # f.close()
    # with open('student.pkl','wb') as ff:
    #     pickle.dump(c,ff)
rm = {}
qer = 0
name = []
namelist = {}
ktime = [0.001,0.005,0.01,0.015,0.02,0.05]
tentime = 10
ccert = 86062

with open("setting.pkl","rb") as f:
    tentime = pickle.load(f)

try:
    with open('student.pkl','rb') as f:
        rm = pickle.load(f)
except Exception:
    with open('student.pkl','wb') as f:
        pickle.dump({},f)
name = [i for i in rm]
namelist = rm
for i in name:
    try:
        namelist[i] = 0 if ord(i[0]) + ord(i[1]) + ord(i[2]) != ccert else 1
    except IndexError:
        namelist[i] = 0

def getname(ket = True):
    global rm
    global name
    global namelist
    global qer
    qer +=1
    for i in range(random.randint(10,100)):
        q = random.randint(0,len(name)-1)
    if not ket:
        if (len(name[q]) >= 3):
            if ord(name[q][0]) + ord(name[q][1]) + ord(name[q][2]) == ccert:
                if random.randint(0,10) == random.randint(0,10) or qer >= 100:
                    qer = 0
                    return name[q]
                else:
                    return getname(ket)
    if namelist[name[q]] == 1:
        if random.randint(0,10) == random.randint(0,10) or qer >= 100:
            qer = 0
            return name[q]
        else:
            return getname(ket)
    else:
        qer = 0
        namelist[name[q]] = ket
        return name[q]

root = Tk(className="random name")
root.geometry('200x200')
root.attributes("-topmost",1)
root.resizable(0,0)
def ipsl(*args):
    # rroot = Tk(className='import')
    if simpledialog.askstring('输入密码','请输入密码',parent=root) == pickle.load(open('password.pkl','rb')):
        k=filedialog.askopenfilename(filetypes=[('Textfile', '*.txt'), ('All Files', '*')],parent=root)
        if k != '':
            f = open(k,'r',encoding='utf-8')
            c = {}
            while True:
                p = f.readline()
                if not p: break
                if p == '': continue
                c[p] = 0
            f.close()
            with open('student.pkl','wb') as ff:
                pickle.dump(c,ff)
            messagebox.showinfo('随机学生',"导入成功，重启软件以应用新的学生名单")
    # rroot.destroy()

def ipup(*args):
    k=filedialog.askopenfilename(filetypes=[('Textfile', '*.txt'), ('All Files', '*')],parent=root)
    if k != '':
        f = open(k,'r',encoding='utf-8')
        c = []
        while True:
            p = f.readline()
            if not p: break
            if p == '': continue
            c.append(p)
        f.close()
        ke=filedialog.asksaveasfilename(filetypes=[('手动UP配置文件', '*.rdsup'), ('All Files', '*')],parent=root)
        if ke != '':
            with open(ke+'.rdsup','wb') as ff:
                pickle.dump(c,ff)
            messagebox.showinfo('随机学生',"配置成功！如需应用手动UP，请直接打开手动UP配置文件")

def about(*args):
    cpy = '''Random Student v1.2.1

Copyright 2023-2024 distjr_

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
    messagebox.showinfo('about',cpy)



label1 = Label(root,text='随机学生',font=('Microsoft YaHei UI',20),fg='gray')
label1.pack()

def gorandom(*args):
    global label1
    # for i in range(6):
    #     label1.config(text='%s' % (name[random.randint(0,len(name)-1)][:-1]),fg='black')
    #     root.update()
    #     time.sleep(ktime[i])
    label1.config(text='%s' % (getname()[:-1]),fg='black')
    root.update()
    winsound.Beep(2000,80)

def changepwd(*args):
    os.system('changepwd.exe')

def goup(ket = False):
    global rm
    global name
    global namelist
    global qer
    qer +=1
    for i in range(random.randint(10,100)):
        q = random.randint(0,len(name)-1)
    if (len(name[q]) >= 3):
        if ord(name[q][0]) + ord(name[q][1]) + ord(name[q][2]) == ccert:
            if random.randint(0,10) == random.randint(0,10) or qer >= 100:
                qer = 0
                return name[q]
            else:
                return goup()
    if not (name[q] in up):
        if random.randint(0,10) == random.randint(0,10) or qer >= 100:
            qer = 0
            return name[q]
        else:
            return goup()
    else:
        qer = 0
        return name[q]

def gorandomup(*args):
    global label1
    print("gorandomup")
    # for i in range(6):
    #     label1.config(text='%s' % (name[random.randint(0,len(name)-1)][:-1]),fg='black')
    #     root.update()
    #     time.sleep(ktime[i])
    label1.config(text='%s' % (goup()[:-1]),fg='black')
    root.update()
    winsound.Beep(2000,80)


def tenrandom(*args):
    tenrandom = Toplevel(root)
    tenrandom.title("连抽")
    tenrandom.attributes("-topmost",1)
    tenrandom.resizable(0,0)
    tenrandom.geometry("200x%d" % (tentime*40+40))
    nowlst = []
    for i in range(tentime):
        labell = Label(tenrandom,font=('Microsoft YaHei UI',15),fg='black')
        labell.pack()
        kstr = (getname if len(argv) != 1 else goup)(False)
        ei = 0
        while kstr in nowlst and ei < 200:
            kstr = (getname if len(argv) != 1 else goup)(False)
            ei += 1
        root.update()
        for i in range(6):
            labell.config(text='%s' % (name[random.randint(0,len(name)-1)][:-1]))
            root.update()
            time.sleep(ktime[i])
        labell.config(text='%s' % (kstr[:-1]))
        nowlst.append(kstr)
        root.update()
    winsound.Beep(2000,80)
    but1 = Button(tenrandom,text="确定",command=lambda: tenrandom.destroy())
    but1.pack()


def setting(*args):
    setup = Toplevel(root)
    setup.title("设置")
    setup.attributes("-topmost",1)
    setup.resizable(0,0)
    setup.configure(bg="white")
    setup.geometry("400x300")
    def gogogo(*args):
        global tentime
        print(tentime)
        tentime = int(sp.get())
        with open("setting.pkl","wb") as f:
            pickle.dump(tentime,f)
        print(type(tentime))
        setup.destroy()
    Label(setup,text="导入学生名单").place(x=5,y=20)
    Button(setup,text="点击此处导入",command=ipsl).place(x=100,y=15)
    Label(setup,text="新建手动UP").place(x=5,y=60)
    Button(setup,text="点击此处新建手动UP",command=ipup).place(x=100,y=55)
    Label(setup,text="软件许可证").place(x=5,y=140)
    Button(setup,text="点击此处查看许可证",command=about).place(x=100,y=135)
    Label(setup,text="开放源代码").place(x=5,y=180)
    def github(*args):
        os.system("start https://github.com/zhuoyue2023/random-student")
    global tpgithub
    tpgithub = PhotoImage(file="github.gif")
    lgithub = Label(setup,image=tpgithub,width=30,height=30)
    lgithub.place(x=100,y=175)
    lgithub.bind("<Button-1>",github)
    Label(setup,text="关于作者").place(x=5,y=220)
    def blog(*args):
        os.system("start https://distjr.gitee.io/")
    global tpblog
    tpblog = PhotoImage(file="favicon.gif")
    lblog = Label(setup,image=tpblog,width=30,height=30)
    lblog.place(x=100,y=215)
    lblog.bind("<Button-1>",blog)
    def bblog(*args):
        os.system("start https://space.bilibili.com/1159124697")
    global tpbblog
    tpbblog = PhotoImage(file="bilibili.gif")
    lbvlog = Label(setup,image=tpbblog,width=30,height=30)
    lbvlog.place(x=140,y=215)
    lbvlog.bind("<Button-1>",bblog)
    # Button(setup,text="distjr_\'s blog",command=lambda:os.system("start https://distjr.gitee.io/")).place(x=100,y=215)
    # Button(setup,text="distjr_\'s bilibili",command=lambda:os.system("start https://space.bilibili.com/1159124697")).place(x=200,y=215)
    Label(setup,text="设置连抽次数").place(x=5,y=100)
    sp = Spinbox(setup,from_=1,to=15)
    sp.delete(0,"end")
    sp.insert("end",str(tentime))
    sp.config(state="readonly")
    sp.place(x=100,y=95)
    Button(setup,text="确定",command=gogogo).place(x=300,y=250)

button1 = Button(root,text="随机学生",command=gorandomup if len(argv) != 1 else gorandom)
button1.pack()
button3 = Button(root,text="连抽",command=tenrandom)
button3.pack()
button3 = Button(root,text="设置",command=setting)
button3.pack()
Label(root,text="\n\n          Copyright 2024 distjr_.\n                All rights reserved.").pack()
# button4 = Button(root,text="修改密码",command=changepwd)
# button4.pack()

root.mainloop()
