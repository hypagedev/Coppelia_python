import sim
import sys
import time
import math


def gripper(j1,j2, clientID, close):
    if(close == True):
        sim.simxSetJointTargetVelocity(clientID, j2,0.04, sim.simx_opmode_oneshot)
    else:
        sim.simxSetJointTargetVelocity(clientID, j2,-0.04, sim.simx_opmode_oneshot)
    r, p2 = sim.simxGetJointPosition(clientID, j2,sim.simx_opmode_oneshot)
    sim.simxSetJointTargetPosition(clientID,j1, p2*-1, sim.simx_opmode_oneshot)


print ('Programa inicio')
sim.simxFinish(-1) # cerrar todas las conexiones
# Conectar a CoppeliaSim
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5)
if clientID!=-1:
    print ('Conectado al API del servidor remoto')

    _, M1 =sim.simxGetObjectHandle(clientID, 'youBotArmJoint0', sim.simx_opmode_blocking)
    _, M2 =sim.simxGetObjectHandle(clientID, 'youBotArmJoint1', sim.simx_opmode_blocking)
    _, M3 =sim.simxGetObjectHandle(clientID, 'youBotArmJoint2', sim.simx_opmode_blocking)
    _, M4 =sim.simxGetObjectHandle(clientID, 'youBotArmJoint3', sim.simx_opmode_blocking)
    _, M5 =sim.simxGetObjectHandle(clientID, 'youBotArmJoint4', sim.simx_opmode_blocking)
    sim.simxSetJointPosition(clientID, M1,0*math.pi/180,sim.simx_opmode_streaming)
    sim.simxSetJointPosition(clientID, M2,0*math.pi/180,sim.simx_opmode_streaming)
    sim.simxSetJointPosition(clientID, M3,0*math.pi/180,sim.simx_opmode_streaming)
    sim.simxSetJointPosition(clientID, M4,0*math.pi/180,sim.simx_opmode_streaming)
    sim.simxSetJointPosition(clientID, M5,0*math.pi/180,sim.simx_opmode_streaming)

    _, j1 =sim.simxGetObjectHandle(clientID, 'youBotGripperJoint1', sim.simx_opmode_blocking)
    _, j2 =sim.simxGetObjectHandle(clientID, 'youBotGripperJoint2', sim.simx_opmode_blocking)

    for i in range(5):
        print("Abrir")
        gripper(j1, j2, clientID, True)
        time.sleep(2)
        print("Cerrar")
        gripper(j1, j2, clientID, False)
        time.sleep(2)


    #sim.simxSetJointTargetVelocity(clientID, j1,-0.02, sim.simx_opmode_blocking)

    print("velocidad")
    time.sleep(1)
    # Ahora cerrar la conexion a CoppeliaSim:
    sim.simxFinish(clientID)
else:
    sys.exit('Fallo conectando al API del servidor remoto')
print ('Programa finalizado')
