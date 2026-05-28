# Generador de Perfiles
print("=== Generador de Perfiles v2.0 ===")

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa tu ciudad: ")
rol = input("Ingresa tu profesión/rol: ")
bio = input("Escribe una breve biografía sobre ti: ")

edad_futura = edad + 5

# Usando .format para mostrar el perfil
perfil = """
--- Perfil Generado con .format ---
Nombre: {}
Edad: {}
Ciudad: {}
Rol: {}
Biografía: {}

En 5 años, tendrás {} años.
¡Perfil guardado correctamente!
""".format(nombre, edad, ciudad, rol, bio, edad_futura)

print(perfil)

# Bonus: Usando f-strings para mostrar el perfil
print("\n--- Mismo perfil con f-strings ---")
print(f"Nombre: {nombre}\nEdad: {edad}\nCiudad: {ciudad}\nRol: {rol}\nBiografía: {bio}\nEn 5 años, tendrás {edad_futura} años.\n¡Perfil guardado correctamente!")
