# Generador de Perfiles
print("=== Generador de Perfiles ===")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
edad_futura = edad + 5
ciudad = input("Ingresa tu ciudad: ")
rol = input("Ingresa tu profesión/rol: ")

print("--- Perfil Generado ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Ciudad: {ciudad}")
print(f"rol: {rol}")

bio = input("Escribe una breve biografía sobre ti: ")
print(f"Biografía: {bio}")
print(f"En 5 años, tendrás {edad_futura} años.")

print("¡Perfil guardado correctamente!")
