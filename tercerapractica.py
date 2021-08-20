import random 
#Instalar python -m pip install -U pip
#python -m pip install -U matplotlib
import matplotlib.pylot as plt 
#Generar numero aleatorio
print(random.randrange(10,100,2))

#Reacomodar una lista al azar
lista = [1,2,3,4,5,6,7,8,9,10]
print("Lsita original", lista)

random.shuffle(lista)
print("Lista mixeada", lista)

campana = [random.gauss(1,0.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show