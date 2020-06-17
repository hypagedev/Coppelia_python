import sim
import sys
import time
import math
print(__version__)
print ('Programa inicio')
sim.simxFinish(-1) # cerrar todas las conexiones
# Conectar a CoppeliaSim
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID!=-1:
    print ('Conectado al API del servidor remoto')

    _, M1 =sim.simxGetObjectHandle(clientID, 'Joint1', sim.simx_opmode_blocking)
    sim.simxSetJointPosition(clientID, M1,90*math.pi/180,sim.simx_opmode_streaming)

    print("velocidad")
    time.sleep(10)#dormir unos segundos antes de terminar
    # Ahora cerrar la conexion a CoppeliaSim:
    sim.simxFinish(clientID)
else:
    sys.exit('Fallo conectando al API del servidor remoto')
print ('Programa finalizado')
