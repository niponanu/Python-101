from tkinter import *
from tkinter import ttk  #theme of tk
from tkinter import messagebox


GUI=Tk()  #หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')  #ชื่อโปรแกรม
GUI.geometry('500x500') #ขนาดโปรแกรม
L1= Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=50)
B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)

def Button2():
    text='ตอนนี้มีเงินใน บช 300 บาท'
    messagebox.showinfo('เงินใน บช',text)

FB1 = LabelFrame(GUI,text='Money')  #คล้ายกระดาน
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20,padx=50,pady=50)



GUI.mainloop()
