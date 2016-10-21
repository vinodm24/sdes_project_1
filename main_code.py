import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def Charge(Voltage,R,L,C,Initial_Charge,Initial_Current,Tf=25.0,n=1e3):
    Time=np.linspace(0.0,Tf,n)
    Particular_charge=C*Voltage
    #Finding the roots of the equation
    Delta = (R/C)**2 - 4.0/(L*C) + 0.0j
    r1 = (-(R/C)-np.sqrt(Delta))/2.0
    r2 = (-(R/C)+np.sqrt(Delta))/2.0
    if r1 != r2:
        C1 = (r2*(Initial_Charge - C*Voltage) - Initial_Current)/(r2-r1)
        C2 = (r1*(Initial_Charge - C*Voltage) - Initial_Current)/(r1-r2)
        Charge = C*Voltage + C1*np.exp(r1*Time) + C2*np.exp(r2*Time)
        Current = r1*C1*np.exp(r1*Time) + r2*C2*np.exp(r2*Time)
    else:
        C1 = Initial_Current - r1*(Initial_Charge - C*Voltage)
        C2 = Initial_Charge - C*Voltage
        Charge = np.exp(r1*Time)*(C1*Time + C2) + C*Voltage
        Current = np.exp(r1*Time)*((r1*Time+1.0)*C1 + r1*C2)
    return Charge/C,Current*R,Voltage-Charge/C-Current*R,Time

if __name__ == '__main__':
    Voltage_C,Voltage_R,Voltage_L,Time = Charge(10,0.5,1,1,0,0)
    plt.plot(Time,Voltage_C,'b')
    plt.plot(Time,Voltage_R,'r')
    plt.plot(Time,Voltage_L,'g')
    plt.show()