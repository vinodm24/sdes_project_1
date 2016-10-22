import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pylab import *

def Voltage_RLC(Voltage,R,L,C,Initial_Charge=0.0,Initial_Current=0.0,Tf=20):
    Time=np.linspace(0.0,Tf,1000)
    Particular_charge=C*Voltage
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
    return Current*R,Voltage-Charge/C-Current*R,Charge/C,Time

def animate(X1,Y1,X2,Y2,X3,Y3,name):
    fig = plt.figure()
    ax = plt.axes(xlim=(0,20.0), ylim=(-10.,20.))
    line, = ax.plot([], [], lw=2)
    line1, = ax.plot([], [], lw=2)
    line2, = ax.plot([], [], lw=2)

    def init():
        line.set_data([],[])
        line1.set_data([],[])
        line2.set_data([],[])
        return line,line1,line2,
    
    def animate(i):
        line.set_data(X1[:i], Y1[:i])
        line1.set_data(X2[:i],Y2[:i])
        line2.set_data(X3[:i],Y3[:i])
        return line,line1,line2,
        
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=1000, interval=2, blit=True)
    anim.save(name+'.mp4', fps=120, extra_args=['-vcodec', 'libx264'])
    plt.show()

if __name__ == '__main__':
    Voltage_R_ud,Voltage_L_ud,Voltage_C_ud,Time_ud=Voltage_RLC(10,0.5,1,1)
    Voltage_R_cd,Voltage_L_cd,Voltage_C_cd,Time_cd=Voltage_RLC(10,1,1,1)
    Voltage_R_od,Voltage_L_od,Voltage_C_od,Time_od=Voltage_RLC(10,2,1,1)
    
    figure(0)
    plt.plot(Time_ud,Voltage_R_ud,label = 'Resistor')
    plt.plot(Time_ud,Voltage_L_ud,label = 'Inductor')
    plt.plot(Time_ud,Voltage_C_ud,label = 'Capacitor')
    plt.title('Voltage across Elements with time in Under damped case')
    plt.ylabel('Voltage (V)')
    plt.xlabel('time (s)')
    plt.legend()
    plt.savefig('voltage_across_elements_in_Underdamped_case.png')
    
    figure(1)
    Voltage_R_cd,Voltage_L_cd,Voltage_C_cd,Time_cd=Voltage_RLC(10,1,1,1)
    plt.plot(Time_cd,Voltage_R_cd,'r',label = 'Resistor')
    plt.plot(Time_cd,Voltage_L_cd,'g',label = 'Inductor')
    plt.plot(Time_cd,Voltage_C_cd,'b',label = 'Capacitor')
    plt.title('Voltage across Elements with time in Critically damped case')
    plt.ylabel('Voltage (V)')
    plt.xlabel('time (s)')
    plt.legend(loc = 'center right')
    plt.savefig('voltage_across_elements_in_Criticallydamped_case.png')
    
    figure(2)
    Voltage_R_cd,Voltage_L_cd,Voltage_C_cd,Time_cd=Voltage_RLC(10,1,1,1)
    plt.plot(Time_od,Voltage_R_od,'r',label = 'Resistor')
    plt.plot(Time_od,Voltage_L_od,'g',label = 'Inductor')
    plt.plot(Time_od,Voltage_C_od,'b',label = 'Capacitor')
    plt.title('Voltage across Elements with time in Over damped case')
    plt.ylabel('Voltage (V)')
    plt.xlabel('time (s)')
    plt.legend(loc = 'center right')
    plt.savefig('voltage_across_elements_in_overdamped_case.png')

    animate(Time_ud,Voltage_R_ud,Time_ud,Voltage_L_ud,Time_ud,Voltage_C_ud,'voltage_across_elements_in_Underdamped_case')
    animate(Time_cd,Voltage_R_cd,Time_cd,Voltage_L_cd,Time_cd,Voltage_C_cd,'voltage_across_elements_in_Critically_damped_case')
    animate(Time_od,Voltage_R_od,Time_od,Voltage_L_od,Time_od,Voltage_C_od,'voltage_across_elements_in_overdamped_case')
    