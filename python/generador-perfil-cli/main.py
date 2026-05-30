# Generador de Perfiles
print("=== Generador de Perfiles v2.2 ===")

nombre = input("Ingresa tu nombre: ")
nombre_limpio = nombre.strip().title()

edad = int(input("Ingresa tu edad: "))

ciudad = input("Ingresa tu ciudad: ")
ciudad_limpia = ciudad.strip().capitalize()

email = input("Ingresa tu email: ")
email_limpio = email.strip().lower()

rol = input("Ingresa tu profesión/rol: ")
rol_limpio = rol.strip().title()

bio = input("Escribe una breve biografía sobre ti: ")
bio_limpia = bio.strip().capitalize()

tiene_python = "python" in bio_limpia.lower()
cantidad_a = nombre_limpio.lower().count('a')
palabras_bio = len(bio_limpia.split(" "))

edad_futura = edad + 5

# Usando .format para mostrar el perfil
perfil = """
--- Perfil Generado con .format ---
Nombre: {}
Edad: {}
Ciudad: {}
Email: {}
Rol: {}

Análisis automático:
- Tu nombre tiene {} letras 'a'
- Tu biografía tiene {} palabras
- ¿Mencionaste Python?: {}

Biografía: {}

En 5 años, tendrás {} años.
¡Perfil guardado correctamente!
""".format(nombre_limpio, edad, ciudad_limpia, email_limpio, rol_limpio, cantidad_a, palabras_bio, tiene_python, bio_limpia, edad_futura)

print(perfil)
