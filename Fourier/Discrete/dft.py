import numpy as np  
import matplotlib.pyplot as plt

def discrete_fourier(f :list) -> list :
    N=len(f)
    F=np.zeros(N,dtype=complex)
    for k in range(N):
        for n in range(N):
            F[k]+=f[n]*np.exp((-1j*2*np.pi/N)*n*k)
    return F
#creating the samples
a=0 ; frequency=534 ; N=300; b=N/frequency
t=np.linspace(a,b,N)

f=np.sin((2*np.pi)*100*t)
F=discrete_fourier(f)
x=np.fft.fftfreq(N,1/frequency)
plt.style.use("seaborn-v0_8")
fig,axis=plt.subplots(1,2,figsize=(8, 6))
axis[0].plot(x[:N//2],np.abs(F)[:N//2])
axis[0].set_xlabel("Frequências Hz")
axis[0].set_ylabel("Magnitude")
axis[1].plot(x[:N//2],np.angle(F)[:N//2])
axis[1].set_xlabel("Frequências Hz")
axis[1].set_ylabel("Fase")
fig.savefig("teste.png")