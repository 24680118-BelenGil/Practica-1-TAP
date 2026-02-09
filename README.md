# Practica-1-TAP
## Planteamineto
Crear una interfaz grafica en Python Flet, la inferfaz debe mostrar 4 botones, cada boton con un color distinto, tres de ellos deben tener numero y el cuarto borrara lo escrito por los anteriores tres, ademas, debe agregarse un espacio que muestre las acciones de estor botones.
## Desarrollo
**1.Entorno virtual Flet**

Debemos crear un entorno virtual Flet, en esta seccion describiremos su instalacion de forma resumida, para mas informacion ingresa al siguinete link que te llevara a la pagina official de Flet.

https://docs.flet.dev/getting-started/installation/#operating-system

* Desde Git Bash ingresamos a nuestro escritorio y creamos una carpeta con los siguientes comandos:
  ```bash
  mkdir my-app
  cd my-app
  ```
  **my-app** puede ser sustituida por el nombre que desees.

* Una vez dentro de tu carpeta, debemos crear el entorno virtual con:
 ```bash
  python -m venv .venv
  ```
* Cuando se termine de crear, podras activaro con el comando:
 ```bash
  source .venv/bin/activate
  ```
* Ahora que esta activos instalarmos Flet, esto nos permitira usar sus dependencias, para hacerlos ingreamos:
 ```bash
  pip install 'flet[all]'
  ```
* ¡¡¡Listo!!! ahora solo debes verificar si esta intalado, para ello ingreasa cualquiera de los siguinetes comandos en Git Bash.
 ```bash
 flet --version
# or
flet doctor
  ```
* Una vez comprobada su instalacion abrimos un editor de código apto para Python, en mi caso sera Visual Studio Code, y desde el editor abrimos nuestra carpeta anteriormente creada.

****
##Resultado
