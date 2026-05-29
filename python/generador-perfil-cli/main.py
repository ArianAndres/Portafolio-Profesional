# Generador de Perfiles
print("=== Generador de Perfiles v2.0 ===")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa tu ciudad: ")
rol = input("Ingresa tu profesión/rol: ")
bio = input("Escribe una breve biografía sobre ti: ")

edad_futura = edad + 5

# Usando slicing para mostrar partes del perfil
primera_letra = nombre[0]
ultima_letra = nombre[-1]
primer_nombre = nombre[0:5]
nombre_invertido = nombre[::-1]
cantidad_letras = len(nombre)

# Usando .format para mostrar el perfil
perfil = """
--- Perfil Generado con .format ---
Nombre: {}
Primera Letra = {}
Última Letra = {}
Primer Nombre = {}
Nombre Invertido = {}
Cantidad de Letras = {}

Edad: {}
Ciudad: {}
Rol: {}
Biografía: {}

En 5 años, tendrás {} años.
¡Perfil guardado correctamente!
""".format(nombre, primera_letra, ultima_letra, primer_nombre, nombre_invertido, cantidad_letras, edad, ciudad, rol, bio, edad_futura)

print(perfil)

# Bonus: Usando f-strings para mostrar el perfil
print("\n--- Mismo perfil con f-strings ---")
print(f"Nombre: {nombre}\nEdad: {edad}\nCiudad: {ciudad}\nRol: {rol}\nBiografía: {bio}\nEn 5 años, tendrás {edad_futura} años.\n¡Perfil guardado correctamente!")
