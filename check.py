import tkinter as tk
import numpy as np
from PIL import ImageTk, Image
import os
import time
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


LARGE_FONT= ("Verdana", 12)


E0 = 8.854e-12
Er = 3.9
u = 4e-7*np.pi

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        
        w = tk.DoubleVar()
        l = tk.DoubleVar() 
        h = tk.DoubleVar() 
        t = tk.DoubleVar()
        p = tk.DoubleVar()
        R = tk.DoubleVar()
        L = tk.DoubleVar()
        C = tk.DoubleVar()
        
        message = """ INSTRUCTIONS\n
        l is the length of the interconnect metal(M1) in micrometer.\n
        w is the width of the interconnect metal(M1)\n
        t is the thickness of the interconnect metal(M1)\n
        h is the height between ground and metal(M1) \n
        p is the resistivity of interconnect metal(M1)\n
        E0 = 8.854*10^(-12) is the permittivity of free space\n
        Er = 3.9 assuming SiO2 is the relative permittivity"""
        
        msg = tk.Message(self, text = message)
        msg.config(bg='lightblue', font=('times', 10))
        msg.pack()

        #tk.Label(self, text="Inputs", bg = 'lightblue',font=('times', 20, 'italic')).pack(fill = "x")
        
        tk.Label(self, text='Width', bg = 'lightblue').pack( fill="x" )
        width = tk.StringVar()
        w1 = tk.Entry(self)
        w1.pack()


        tk.Label(self, text='Length', bg = 'lightblue').pack( fill="x")
        l1 = tk.Entry(self) 
        l1.pack()

        tk.Label(self, text='Thickness', bg = 'lightblue').pack( fill="x")
        t1 = tk.Entry(self) 
        t1.pack()

        
        tk.Label(self, text='Height', bg = 'lightblue').pack(fill = "x")
        h1 = tk.Entry(self) 
        h1.pack()

        
        tk.Label(self, text='Rho', bg = 'lightblue').pack(fill = "x")
        rho1 = tk.Entry(self) 
        rho1.pack()


        def read_ip():
            try:
                l = float(l1.get())
                w = float(w1.get())
                h = float(h1.get())
                t = float(t1.get())
                p = float(rho1.get())
                print(type(l))
                R = ((p*l)/(w*t))/(100000000)
                C = (((2*np.pi*E0*Er)/(np.log10(h/t)))+ ((w- 0.5*t)*E0*Er/h))
                L = (u)/(2*np.pi)*(np.log10(2*l/(w+t))+ 0.5 + (0.22 *(w+t)/l))
                file1 = open("C:\\Users\\Sahith\\Desktop\\VLSI\\Interconnect.txt","w")
                file1.write("L1 Out1 X "+str(L)+"\n")
                file1.write("R1 X In2 "+str(R)+"\n")
                file1.write("C1 Out1 0 "+str(C)+"\n")
                file1.write("C2 In2 0 "+str(C)+"\n")
                file1.close()
                print(R)
                print(C)
                print(L)
                R1.insert(10,str(R))
                C1.insert(10,str(C))
                L1.insert(10,str(L))
            except Exception as e:
                print(e)

        
        B = tk.Button(self, text ="OK",command = read_ip, bg = 'white')
        B.pack()

        

        tk.Label(self, text="RLC", bg = 'lightblue', font=('times', 20, 'italic')).pack()

        tk.Label(self, text='Resistance',bg = 'lightblue').pack()
        R1 = tk.Entry(self)
        R1.pack()

        tk.Label(self, text='Capacitance',bg = 'lightblue').pack()
        C1 = tk.Entry(self)
        C1.pack()

        tk.Label(self, text='Inductance',bg = 'lightblue').pack()
        L1 = tk.Entry(self)
        L1.pack()


        
        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        #button2 = tk.Button(self, text="Visit Page 2",
        #                    command=lambda: controller.show_frame(PageTwo))
        #button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
    
   
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


        def calc():
            try:
                os.system('cmd /k "START "" ngspice C:\\Users\\Sahith\\Desktop\\VLSI\\GUI_basic.txt"')
                with open("C:\\Users\\Sahith\\Desktop\\VLSI\\output.txt") as f:
                    data = f.read()

                data = data.split('\n')
                l = len(data)

                IN = []
                OUT = []
                x = []
                for i in range(l-1):
                    t = data[i].split(' ')
                    x.append(t[1])
                    IN.append(t[3])
                    OUT.append(t[5])

                fig = plt.figure()

                ax1 = fig.add_subplot(111)

                ax1.set_title("Plot title")    
                ax1.set_xlabel('x label')
                ax1.set_ylabel('y label')

                ax1.plot(x,IN, c='r', label='the INPUT')
                ax1.plot(x,OUT,c='g', label='the OUTPUT')
                
                leg = ax1.legend()

                plt.show()
                os.system('cmd /k "taskkill /F /IM ngspice.exe /T"')
                
            except Exception as e:
                print(e)
                
            
        
        button3 = tk.Button(self, text ="Calculate",
                            command = calc,bg = 'white')
        button3.pack()        
        
        
        


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        #button2 = tk.Button(self, text="Page One",
        #                    command=lambda: controller.show_frame(PageOne))
        #button2.pack()
        


app = SeaofBTCapp()
app.mainloop()
