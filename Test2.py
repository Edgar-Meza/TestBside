# Para este ejercicio necesitas hacer uso del documento nombrado Tabla1.
# Escribe un algoritmo para consolidar los registros en uno sololos registros encontrados en Tabla1.
# Usa el documento Tabla1 para generar la salida.

import pandas as pa

datos = pa.read_csv('Tabla1.csv', header=0, encoding='latin-1')
print(datos)
data = pa.DataFrame(datos)

data['Nombre'] = data['Nombre'].str.title()

texto_1 = ['Jose','Joce','Jocé','Jóce','Jóse']
texto_2 = ['Dias','Diaz','Diás','Diáz']
texto_3 = ['Hernandez','Hernandes']
texto_4 = ['Gonzales','Gonsales','Gonzalez','Gonsalez']
texto_5 = ['Sanchez','Sanches']
texto_6 = ['Peres','Perez','Péres']

def corregir(texto_o, texto_c):
  for i in texto_o:
    data['Nombre'] = data['Nombre'].str.replace(i, texto_c)

corregir(texto_1, 'José')
corregir(texto_2, 'Díaz')
corregir(texto_3, 'Hernández')
corregir(texto_4, 'González')
corregir(texto_5, 'Sánchez')
corregir(texto_6, 'Pérez')


dataf = data.groupby(by=['Nombre'])['idCliente'].unique()
dataa = data.groupby(by='Nombre')['Numero de tarjeta'].unique()
datafinal = pa.concat([dataa, dataf], axis=1)
datafinal['Nombre'] = datafinal.index
index_new = []

for i in range(len(datafinal)):
  index_new.append(i)

datafinal.index = index_new

print()
print(datafinal[['Nombre','Numero de tarjeta','idCliente']]) 