import numpy as np
import matplotlib.pyplot as plt

#Movimiento Subamortiguado, Datos conocidos:

t = np.arange(0,15,0.01)
m = 0.2197
c = 0.1795
w = 3.2675
Phi = 0
Xm = 1
B = (c/(2*m))

class MovimientoSubamortiguado:
  def __init__(self, t, m, c, w, Phi, Xm, B):
    self.t = t
    self.m = m
    self.c = c
    self.w = w
    self.Phi = Phi
    self.Xm = Xm
    self.B = B
  
  """
  Función que se encarga de calcular las 
  envolventes de la oscilación subamortiguada
  """
  def funcionExponencial(self):
    A = np.exp(-self.B * self.t)  # Envolvente Positiva
    B = -np.exp(-self.B * self.t) # Envolvente Positiva
    return A, B
  
  """
  Función que se encarga de calcular al movimiento subamortiguado
  """
  def funcionSinusoidal(self):
    return (np.exp(-self.B * self.t)) * (np.sin(self.w * self.t)) # Se calcula usando Seno, ya que la gràfica debe iniciar en Cero

  """
  Función que se encarga de imprimir el
  movimiento subamortiguad y las envolventes
  """
  def Graficas(self, envolventeP, envolventeN, movimientoSub):
    self.envolventeP = envolventeP
    self.envolventeN = envolventeN
    self.movimientoSub = movimientoSub

    self.Envolventes()
    self.Subamortiguado()
    self.Final()
  
  # Gráficando solamente las envolventes
  def Envolventes(self):
    plt.figure(1)
    ax = plt.axes()
    plt.title("Envolventes Movimiento subamortiguado")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.plot(self.t, self.envolventeP, linewidth = 1.0, linestyle = "--", color = "red", label = "y(t) = np.exp(-Bt)")
    plt.plot(self.t, self.envolventeN, linewidth = 1.0, linestyle = "--", color = "red", label = "y(t) = -np.exp(-Bt)")
    plt.legend(loc="upper right")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.xticks(np.linspace(0,20,5))
    plt.yticks(np.linspace(-1,1,3))

  #Graficando solamente el movimiento subamortiguado
  def Subamortiguado(self):
    plt.figure(2)
    ax = plt.axes()
    plt.title("Movimiento subamortiguado")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.plot(self.t, self.movimientoSub, linewidth = 2.0, color = "blue", label = "y(t) = np.exp(-Bt)np.cos(wt)")
    plt.legend(loc="upper right")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.xticks(np.linspace(0,20,5))
    plt.yticks(np.linspace(-1,1,3))

  #Graficando las envolventes y el movimiento subamortiguado en una sola gráfica
  def Final(self):
    plt.figure(3)
    ax = plt.axes()
    plt.title("Movimiento subamortiguado con envolventes")
    plt.xlabel("Tiempo")
    plt.ylabel("Amplitud")
    plt.plot(self.t, self.movimientoSub, linewidth = 2.0, color = "blue", label = "y(t) = np.exp(-Bt)np.cos(wt)")
    plt.plot(self.t, self.envolventeP, linewidth = 1.0, linestyle = "--", color = "red", label = "y(t) = np.exp(-Bt)")
    plt.plot(self.t, self.envolventeN, linewidth = 1.0, linestyle = "--", color = "red", label = "y(t) = -np.exp(-Bt)")
    plt.legend(loc="upper right")
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    plt.xticks(np.linspace(0,20,5))
    plt.yticks(np.linspace(-1,1,3))
  

def Main():
  ejecutar = MovimientoSubamortiguado(t, m, c, w, Phi, Xm, B)
  envolventePositiva, envolvente_Negativa = ejecutar.funcionExponencial()
  subamortiguado = ejecutar.funcionSinusoidal()
  ejecutar.Graficas(envolventePositiva, envolvente_Negativa, subamortiguado)


if __name__ == '__main__':
  Main()
