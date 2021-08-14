import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class RegresionExponencial:
  
  def __init__(self, Archivo):
    self.Archivo = Archivo

  def __ploteandoDatosArchivoExcel(self):
    plt.figure(1)
    plt.title("Dataframe Excel")
    plt.scatter(self.Archivo["datox"], self.Archivo["saliday"], color = "blue")
    plt.xlabel("Dato x")
    plt.ylabel("Salida y")
    plt.show()

  def getPloteandoDatosArchivoExcel(self):
    return self.__ploteandoDatosArchivoExcel()

  def __creandoRegresionExponencial(self):
    a, b = self.RegresionExponencial()
    x_min = self.Archivo["datox"].min()
    x_max = self.Archivo["datox"].max()
    valores_x = np.linspace(x_min, x_max, 200)
    cy = (a * np.exp(b * valores_x))
    return valores_x, cy

  def RegresionExponencial(self):
    lny = np.log(self.Archivo["saliday"])
    sum1 = (self.Archivo["datox"]*lny).sum()
    prod1 = (lny.mean()) * self.Archivo["datox"].sum()
    sum2 = (self.Archivo["datox"] * self.Archivo["datox"]).sum()
    prod2 = self.Archivo["datox"].mean() * self.Archivo["datox"].sum()
    b = (sum1 - prod1)/(sum2 - prod2)
    exponente = lny.mean() - (b * self.Archivo["datox"].mean())
    a = np.exp(exponente)
    return a, b

  def getcreandoRegresionExponencial(self):
    return self.__creandoRegresionExponencial()


  # Plotenado Regresión exponencial
  def ploteandoRegresionExponencial(self, valores_x, cy):
    self.valores_x = valores_x
    self.cy = cy
    plt.figure(2)
    plt.title("Regresión Exponencial")
    plt.scatter(self.Archivo["datox"], self.Archivo["saliday"], color = "red", alpha = 0.5)
    plt.plot(valores_x, cy, color = "m", linewidth = 0.5)
    plt.xlabel("Dato x")
    plt.ylabel("Salida y")
    plt.show()


def ArchivoExcel():
  return pd.read_excel("exponencial.xlsx", sheet_name = "datos", header = 0)

def Main():
  # Cargando archivo Excel
  Archivo = ArchivoExcel()
  Regresion = RegresionExponencial(Archivo)
  Regresion.getPloteandoDatosArchivoExcel()
  valores_x, cy  = Regresion.getcreandoRegresionExponencial()
  Regresion.ploteandoRegresionExponencial(valores_x, cy)


if __name__ == '__main__':
  Main()