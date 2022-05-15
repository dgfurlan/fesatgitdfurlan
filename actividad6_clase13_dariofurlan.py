# -*- coding: utf-8 -*-
"""Actividad_Clase13_DarioFurlan.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yvIxHc5xiOqxRd4e3wgQtjuxTcrG1QKu
"""

"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
- Un constructor.
 1) mostrar(): Muestra los datos de la cuenta.
 2) ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
 3) retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos

"""
class Cuenta:
  # limite = -10.000 (en caso que sea para todos los titulares)
  
  def __init__(self, titular, cantidad):
    self.titular = ""
    self.cantidad = 0
  
  def mostrar(self):
    print(f"El titular nro 1 se llama {self.titular}, con una cantidad de $ {self.cantidad}")

  def ingresar_titular(self):
    apellido = input("Por favor ingrese su apellido: ")
    nombre = input("Por favor ingrese su nombre: ")
    dni = input("Por favor ingrese su DNI: ")
    self.titular = apellido + ", " + nombre + ". DNI:" + dni

  def ingresar_cantidad(self):
    cant = int(input("Por favor ingrese la cantidad a sumar: $"))
    if cant >= 0:
      self.cantidad = self.cantidad + cant
    else:
      print("No se realizaron cambios en la cantidad.")

  def retirar(self):
    cant = int(input("Por favor ingrese la cantidad a retirar: $"))
    if cant >= 0:
      self.cantidad = self.cantidad - cant
    else:
      print("No se realizaron cambios en la cantidad.")

  def saldo(self):
    print("Su saldo es: $", self.cantidad)

cuenta1 = Cuenta("Dario",100)
cuenta1.ingresar_titular()
cuenta1.ingresar_cantidad()
cuenta1.mostrar()
cuenta1.retirar()
cuenta1.saldo()
cuenta1.retirar()
cuenta1.saldo()