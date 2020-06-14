import sim
import sys

print ('Programa inicio')
sim.simxFinish(-1) # cerrar todas las conexiones
# Conectar a CoppeliaSim
clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) 
if clientID!=-1:
    print ('Conectado al API del servidor remoto')

    
    # Ahora cerrar la conexion a CoppeliaSim:
    sim.simxFinish(clientID)
else:
    sys.exit('Fallo conectando al API del servidor remoto')
print ('Programa finalizado')
