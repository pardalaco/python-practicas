#la funcion super no se porque pero da error

class Vehiculos():

	def __init__(self, marca, modelo):
		
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		
		self.enmarcha=True

	def acelerar(self):

		self.acelera=True

	def frena(self):
		
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
		 self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena)#Poniendo "\n" lo que hacemos es un salto de linia.

class furgoneta(Vehiculos):

	def carga(self, cargar):
		self.cargado=cargar

		if (self.cargado):
			return "La furgoneta esta cargada"

		else:
			return "La furgoneta no esta cargada"
		
class Moto(Vehiculos):#Dentro de la clase ejos heredado la herencia veiculos
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",
			 self.enmarcha, "\nAcelera: ", self.acelera, "\nFrena: ", self.frena, "\n", self.hcaballito)#El metodo estado de la clase moto(que le hemos agregado self.hcaballito) sobre escribe el estado "padre" anterior

class VElectricos(Vehiculos):

	def __init__(self, marca, modelo):

		super().__init__(marca, modelo)

		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True
		


"""class cuad(Moto):#Si crearamos esta clase estaria eredado de moto y tendria todos los valores de veiculos y los valores de la moto
	pass"""

miMoto=Moto("Honda", "CBR")#Le indicamos la marca y el modlo (Linia 3)

miMoto.caballito()#Si no activamos la funcion caballito, el self.hcaballito no tene valor y no se muestra nada

miMoto.estado()

miFurgoneta=furgoneta("Renaut", "3000")

miFurgoneta.arrancar()

miFurgoneta.estado()

print(miFurgoneta.carga(True))#Si no la metemos en un print no hay manera de verlo porque no podemos ver el return

#miMoto.carga(True)#Esto nos da error porque la cariable carga pertenece a la clase furgoneta no a la de moto

class BicicletaElectrica(VElectricos, Vehiculos):#Aqui tenemos una erencia multiple, Cuando hay erencia multiple se da preferencia a la primera clase que indiques (en este caso VElectricos) y solo se utilizara el metodo init que pertenece a la primera
	pass

miBici=BicicletaElectrica("Orbea", "Hks")

