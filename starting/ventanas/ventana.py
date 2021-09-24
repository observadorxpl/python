from tkinter import *

ventana = Tk()
ventana.title("My first window with Python")
ventana.resizable(True, True) #para poder modificar el tamaño de la ventana
ventana.iconbitmap("ic_python.ico")
ventana.geometry("1080x360")
ventana.config(bg="red")
frame = Frame()
frame.pack(side="right", anchor="n")
frame.config(bg="yellow", width="640", height="320")

ventana.mainloop() #para que escuche los clicks etc
