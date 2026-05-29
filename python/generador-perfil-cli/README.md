# Generador de Perfiles CLI

Script de línea de comandos hecho en Python que genera un perfil de usuario personalizado a partir de datos ingresados por consola

## Ejecución
'''bash
python main.py

### Ejemplo de Uso

=== Generador de Perfiles ===
Ingresa tu nombre: Arián
Ingresa tu edad: 24
Edad + 5
Ingresa tu ciudad: Alerce
Ingresa tu profesión/rol: Ingeniero en Informática
Escribe una breve biografía sobre ti: Hola, soy Arián...

--- Perfil Generado ---
Nombre: Arián
Edad: 24
Ciudad: Alerce
rol: Ingeniero en Informática
Biografía: Hola, soy Arián:
En 5 años, tendrás 29 años

¡Perfil guardado correctamente!

#### Tecnologías Usadas

- Python 3.14.5
- Librería estándar únicamente

##### Conceptos Aplicados

- Función Input() y print()
- f-strings para formateo
- Variables y tipos de datos básicos
- Conversión de tipos con 'int()'
- Operaciones aritméticas con variables
- Variables para almacenar resultados calculados

## v2.0 - Formateo de Strings

### Nuevas Características

- Outpot formateado usando '.format()'
- String multilínea con '"""' para mejor presentación
- Comparación entre '.format()' y 'f-strings'

### Conceptos Aplicados

- Strings multilínea con triple comillas
- Método '.format()' para insertar variables
- Concatenación y formateo de texto
- Conversión 'int()' + operaciones aritméticas

## v2.1 - Análisis de Strings con Slicing

### Nuevas características

- Extrae primera letra con 'nombre[0]'
- Extrae última letra con 'nombre[-1]'
- Obtiene substring con 'nombre[0:5]'
- Invierte texto con 'nombre[::-1]'
- Cuenta caracteres con 'len(nombre)'

### Conceptos Aplicados

- Indexación de strings: acceso por posición
- Índices negativos: acceso desde el final
- Slicing '[inicio:fin:paso]'
- Función 'len()' para longitud de strings
