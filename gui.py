'''
Author: Marks Calderon Niquin
Email: markscalderonniquin@gmail.com
github: hypagetech
Program to control kuka arm robot on CoppeliaSim through sliders GUI with TKinder
'''
from tkinter import *
from tkinter import messagebox
import sim
import time
import math

root = Tk()

class GUI(Frame):
    scales_l = []
    labels_l = []
    handles = []
    angs = [[-169,169], [-65,90],[-150, 146],[-102.5, 102.5],[-167.5, 167.5]]
    boolConnect = False
    clientID = -1
    base = 'Joint'
    final = 'LBR_iiwa_14_R820_connection'

    def __init__(self):
        super().__init__()
        self.initUI()
        #sim.simxFinish(-1) #clean all ports

    def initUI(self):
        self.master.title("YoubotARM Robot control")
        for i in range(5):
            tit = "M"+str(i + 1)
            w_label = Label(self.master, text=tit).grid(row=i, column=0, pady=4, padx = 4)
            win = Scale(self.master, from_= self.angs[i][0], to=self.angs[i][1], tickinterval= 30, orient=HORIZONTAL, resolution=2, length=450, command=lambda value, name=i: self.onScale(name, value))
            win.set(0)
            win.grid(row=i, column=1)

            self.scales_l.append(win)
            self.labels_l.append(w_label)

        self.conectar = Button(self.master, text ="Conectar", command = self.onConnect)
        self.conectar.grid(row=8,column=1)

    def onScale(self, name,value):
        if(self.clientID != -1):
            print("{} : {}".format(name, value))
            obj = self.handles[int(name)]
            ang = float(value)*math.pi/180
            sim.simxSetJointPosition(self.clientID, obj ,ang ,sim.simx_opmode_oneshot)
            #print(self.objFinal)
            #pos = sim.simxGetObjectPosition(self.clientID, self.objFinal, -1, sim.simx_opmode_streaming )
            #print(pos)


    def init_robot(self):
        for h in self.handles:
            sim.simxSetJointPosition(self.clientID, h,0 ,sim.simx_opmode_oneshot)
        print("termino de inicializar")

    def onConnect(self):
        if self.clientID != -1:
            return

        self.clientID = sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to CoppeliaSim
        if self.clientID == -1:
            messagebox.showinfo( "No se puede conectar")
        else:

            for i in range(5):
                j = i + 1
                nom = self.base + str(j)
                _, handle=sim.simxGetObjectHandle(self.clientID, nom, sim.simx_opmode_blocking)
                self.handles.append(handle)
            time.sleep(1)
            print("Conectado y envio comando al motor")
            self.init_robot()

def close_window():
  print("Close all ports")
  sim.simxFinish(-1) #clean all ports
  root.destroy()

def main():
    root.protocol("WM_DELETE_WINDOW", close_window)
    ex = GUI()
    root.geometry("500x400")
    root.mainloop()


if __name__ == '__main__':
    main()
