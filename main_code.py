import numpy as np
import matplotlib.pyplot as plt

def Current(Voltage,R,L,C,Initial_Charge,Initial_Current,Tf=10.0,n=1e3):
    Time=np.linspace(0.0,Tf,n)
    Particular_charge=C*Voltage
    #Finding the roots of the equation
    Delta = (R/C)**2 - 4.0/(L*C) + 0.0j
    r1 = (-(R/C)-cmath.sqrt(Delta))/2.0
    r2 = (-(R/C)+cmath.sqrt(Delta))/2.0
    if r1 != r2:
        C1 = (r2*(Initial_Charge - C*Voltage) - Initial_Current)/(r2-r1)
        C2 = (r1*(Initial_Charge - C*Voltage) - Initial_Current)/(r1-r2)
        Charge = C*Voltage + C1*np.exp(r1*Time) + C2*np.exp(r2*Time)
    else:
        C1 = Initial_Current - r1*(Initial_Charge - C*Voltage)
        C2 = Initial_Charge - C*Voltage
        Charge = np.exp(C1*Time + C2) + C*Voltage
    return Charge

if __name__ == '__main__':
    Charge_ud = Charge(10,1.5,1,1,0,0)
    