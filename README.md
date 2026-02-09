# Practica-1-TAP
## Planteamineto
Crear una interfaz grafica en Python Flet, la inferfaz debe mostrar 6 botones, cada boton con un color distinto, cinco de ellos deben tener numero y el sexto borrara lo escrito por los anteriores tres, ademas, debe agregarse un espacio que muestre las acciones de estor botones.
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
* Ahora que esta activo instalarmos Flet, esto nos permitira usar sus dependencias, para hacerlos ingreamos:
  ```bash
  pip install 'flet[all]'
  ```
* ¡¡¡Listo!!! ahora solo debes verificar si esta intalado, para ello ingreasa cualquiera de los siguinetes comandos en Git Bash.
  ```bash
  flet --version
  ```
  ó
  ```bash
  flet doctor
  ```
  
* Una vez comprobada su instalacion abrimos un editor de código apto para Python, en mi caso sera Visual Studio Code, y desde el editor abrimos nuestra carpeta anteriormente creada.

**Librería y función principal**
```Python
  import flet as ft
  ```
Importamos la librería flet y la renombramos ft, para trabajar con mas comodidad.
```Python
  def main(page: ft.Page):
    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 300
    page.padding = 30
  ```
Creamos la ventana donde se colocaran todods nuestros elementos, seguido del nombre de laventana, su altura y ancho, además, de colocar el margen que separara cada elemento.

**Display**
```Python
   display_text = ft.Text("0", size=30)

    display = ft.Container(
        content=display_text,
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=210,
        height=70,
  ```
Se crea el display, ventana que mostrara las acciones de los botones, tendra un "0" cuando no se de click en algún boton. Se define su tamaño, color, forma de los bordes y su alineacion.

**Entrada de números**
```Python
   def number_click(i):
        value = i.control.content.value
        if display_text.value == "0":
            display_text.value = value
        else:
            display_text.value += value
        page.update()
  ```

**Eliminar**
```Python
  def clear(i):
        display_text.value = "0"
        page.update()

  ```

**Botones**
```Python
   grid = ft.GridView(
        runs_count=3,
        spacing=10,
        run_spacing=10,
        width=210,
        height=210,
        expand=False
  ```

```Python
        ft.ElevatedButton(
            content=ft.Text("1",color=ft.Colors.BLACK),
            bgcolor=ft.Colors.PINK_100,
            width=100,
            height=50,
            on_click=number_click
  ```
**Organizacion y Ejecución**
```Python
   page.add(
        ft.Column(
            controls=[display, grid],
            tight=True
        )
    )

ft.app(target=main)
  ```

## Resultado
