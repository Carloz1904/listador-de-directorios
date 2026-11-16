import os 

# 1. Define la ruta de la carpeta (',' es la carpeta donde esta el script)
carpeta = "."

# 2. Obtiene la lista de nombres de archivos y subcarpetas
elementos = os.listdir(carpeta)

for nombre in elementos:
	# Une la ruta de la carpeta con el nombre del elemento
	ruta_completa = os.path.join(carpeta, nombre)

	# 3. Verifica que sea un archivo y no una subcarpeta
	if os.path.isfile(ruta_completa):
		# Obtiene el tamaño en bytes
		tamano = os.path.getsize(ruta_completa)
		print(f"Archivo: {nombre} | Tamaño: {tamano} bytes")
