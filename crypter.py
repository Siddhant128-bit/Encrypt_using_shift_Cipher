import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
root=tk.Tk()
root.geometry('500x500')
root.title('Crypter')
root.iconbitmap('logo.ico')
frame0=LabelFrame(root)

def main_menu():
    frame0.destroy()
    frame=LabelFrame(root)
    frame.pack(padx=20,pady=20)
    def encrypt():
        frame.destroy()
        frame1=LabelFrame(root,padx=5,pady=5)
        frame1.pack()
        def get():
            text=Entrye1.get()
            key=Entrye2.get()
            key=int(key)
            temp_encrypt=""
            for i in text:
                ow=ord(i)
                nw=ow+key
                i=chr(nw)
                temp_encrypt=temp_encrypt+i

            print(temp_encrypt)
            Entrye3=Entry(frame1,width=200)
            Entrye3.insert(0,temp_encrypt)
            Entrye3.pack()
        def main_menu1():
            frame1.destroy()
            main_menu()

        button=Button(frame1,text='Back',command=main_menu1)
        button.pack()

        label1=Label(frame1,text='Enter plain text: ')
        label1.pack()
        Entrye1=Entry(frame1,width=100)
        Entrye1.pack()
        label2=Label(frame1,text='Enter the key: ')
        label2.pack()
        Entrye2=Entry(frame1)
        Entrye2.pack()
        buttone1=Button(frame1,text='Submit',fg='green',command=get)
        buttone1.pack()
        label3=Label(frame1,text='Encrypted text: ')
        label3.pack()

    def decrypt():
        print('Welcome to decryption')
        frame.destroy()
        frame1=LabelFrame(root,padx=5,pady=5)
        frame1.pack()
        def get():
            text=Entrye1.get()
            key=Entrye2.get()
            key=int(key)
            temp_encrypt=""
            for i in text:
                ow=ord(i)
                nw=ow+(-1)*key
                i=chr(nw)
                temp_encrypt=temp_encrypt+i

            print(temp_encrypt)
            Entrye3=Entry(frame1,width=200)
            Entrye3.insert(0,temp_encrypt)
            Entrye3.pack()
        def main_menu1():
            frame1.destroy()
            main_menu()

        button=Button(frame1,text='Back',command=main_menu1)
        button.pack()

        label1=Label(frame1,text='Enter encrypted text: ')
        label1.pack()
        Entrye1=Entry(frame1,width=100)
        Entrye1.pack()
        label2=Label(frame1,text='Enter the key: ')
        label2.pack()
        Entrye2=Entry(frame1)
        Entrye2.pack()
        buttone1=Button(frame1,text='Submit',fg='green',command=get)
        buttone1.pack()
        label3=Label(frame1,text='Decrypted text: ')
        label3.pack()




    Button0=Button(frame,text='Encrypt',command=encrypt)
    Button0.pack()

    Button1=Button(frame,text='Decrypt',command=decrypt)
    Button1.pack()

    Button2=Button(frame,text='Quit',fg='red',command=root.quit)
    Button2.pack()









img=ImageTk.PhotoImage(Image.open('logo.png'))
img_Label=Label(image=img)
img_Label.pack()
frame0.pack()
buttonp=Button(frame0,text='Start',command=main_menu)
buttonp.pack()


root.mainloop()
