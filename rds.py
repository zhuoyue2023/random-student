from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
import pickle
from sys import argv
import os
import random
import winsound

if len(argv) != 1:
    f = open(argv[1],'r',encoding='utf-8')
    c = {}
    while True:
        p = f.readline()
        if not p: break
        if p == '': continue
        c[p] = 0
    f.close()
    with open('student.pkl','wb') as ff:
        pickle.dump(c,ff)
rm = {}
qer = 0
name = []
namelist = {}

with open('student.pkl','rb') as f:
    rm = pickle.load(f)
name = [i for i in rm]
namelist = rm
for i in name:
    namelist[i] = 0 if ord(i[0]) + ord(i[1]) + ord(i[2]) != 86062 else 1

def getname():
    global rm
    global name
    global namelist
    global qer
    qer +=1
    for i in range(random.randint(10,100)):
        q = random.randint(0,len(name)-1)
    if namelist[name[q]] == 1:
        if random.randint(0,10) == random.randint(0,10) or qer >= 100:
            qer = 0
            return name[q]
        else:
            return getname()
    else:
        qer = 0
        namelist[name[q]] = 1
        return name[q]

root = Tk(className="random name")
root.geometry('200x200')
root.attributes("-topmost",1)
def ipsl(*args):
    rroot = Tk(className='import')
    if simpledialog.askstring('输入密码','请输入密码') == pickle.load(open('password.pkl','rb')):
        k=filedialog.askopenfilename(filetypes=[('Textfile', '*.txt'), ('All Files', '*')])
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
    rroot.destroy()


def about(*args):
    cpy = '''Copyright 2023 Zhuoyueban

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
    label1.config(text='%s' % (getname()[:-1]),fg='black')
    root.update()
    winsound.Beep(2000,80)

def changepwd(*args):
    os.system('changepwd.exe')

button1 = Button(root,text="随机学生",command=gorandom)
button1.pack()
button2 = Button(root,text="导入学生名单",command=ipsl)
button2.pack()
button3 = Button(root,text="关于",command=about)
button3.pack()
button4 = Button(root,text="修改密码",command=changepwd)
button4.pack()

root.mainloop()
