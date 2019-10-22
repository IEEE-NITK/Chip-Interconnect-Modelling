import tkinter as tk
import numpy as np
from PIL import ImageTk, Image

E0 = 8.854e-12
Er = 3.9
u = 4e-7*np.pi
##GUI##

pi_model = tk.Tk()
pi_model.title("Interconnect model")
pi_model.geometry('700x500')
#pi_model.resizable(0,0)

img=tk.PhotoImage(file = "bg.png")

w = tk.DoubleVar(pi_model)
l = tk.DoubleVar(pi_model) 
h = tk.DoubleVar(pi_model) 
t = tk.DoubleVar(pi_model)
p = tk.DoubleVar(pi_model)
R = tk.DoubleVar(pi_model)
L = tk.DoubleVar(pi_model)
C = tk.DoubleVar(pi_model)

##Frames##
Instructions = tk.Frame(pi_model,bg="lightblue")
Instructions.pack(fill = tk.X)

Inputs = tk.Frame(pi_model,bg="lightblue")
Inputs.pack(fill = tk.X)

RLC = tk.Frame(pi_model,bg="lightblue")
RLC.pack(fill = tk.X)


##Instructions##

message = """ INSTRUCTIONS\n
l is the length of the interconnect metal(M1) in micrometer.\n
w is the width of the interconnect metal(M1)\n
t is the thickness of the interconnect metal(M1)\n
h is the height between ground and metal(M1) \n
p is the resistivity of interconnect metal(M1)\n
E0 = 8.854*10^(-12) is the permittivity of free space\n
Er = 3.9 assuming SiO2 is the relative permittivity"""
msg = tk.Message(Instructions, text = message)
msg.config(bg='lightblue', font=('times', 10, 'italic'))
msg.pack()


##Inputs##

tk.Label(Inputs, text="Inputs", bg = 'lightblue',font=('times', 20, 'italic')).grid(column=0, row=0,padx=3)

tk.Label(Inputs, text='Width', bg = 'lightblue').grid(row=1)
width = tk.StringVar(pi_model)
w1 = tk.Entry(Inputs)
w1.grid(row=1, column=1)

tk.Label(Inputs, text='Length', bg = 'lightblue').grid(row=2) 
l1 = tk.Entry(Inputs) 
l1.grid(row=2, column=1)

tk.Label(Inputs, text='Thickness', bg = 'lightblue').grid(row=3) 
t1 = tk.Entry(Inputs) 
t1.grid(row=3, column=1)

tk.Label(Inputs, text='Height', bg = 'lightblue').grid(row=4) 
h1 = tk.Entry(Inputs) 
h1.grid(row=4, column=1)

tk.Label(Inputs, text='Rho', bg = 'lightblue').grid(row=5) 
rho1 = tk.Entry(Inputs) 
rho1.grid(row=5, column=1)

def read_ip():
    try:
        l = float(l1.get())
        w = float(w1.get())
        h = float(h1.get())
        t = float(t1.get())
        p = float(rho1.get())
        print(type(l))
        R = ((p*l)/(w*t))
        C = (((2*np.pi*E0*Er)/(np.log10(h/t)))+ ((w- 0.5*t)*E0*Er/h))
        L = (u)/(2*np.pi)*(np.log10(2*l/(w+t))+ 0.5 + (0.22 *(w+t)/l))
        print(R)
        print(C)
        print(L)
        R1.insert(10,str(R))
        C1.insert(10,str(C))
        L1.insert(10,str(L))
    except Exception as e:
        print(e)

        
B = tk.Button(Inputs, text ="OK",command = read_ip, bg = 'white')
B.grid(row = 6, column = 0)
##RLC##
tk.Label(RLC, text="RLC", bg = 'lightblue', font=('times', 20, 'italic')).grid(row=0)

tk.Label(RLC, text='Resistance',bg = 'lightblue').grid(row=1)
R1 = tk.Entry(RLC)
R1.grid(row=1, column=1)

tk.Label(RLC, text='Capacitance',bg = 'lightblue').grid(row=2)
C1 = tk.Entry(RLC)
C1.grid(row=2, column=1)

tk.Label(RLC, text='Inductance',bg = 'lightblue').grid(row=3)
L1 = tk.Entry(RLC)
L1.grid(row=3, column=1)


pi_model.mainloop()
