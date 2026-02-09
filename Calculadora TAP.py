import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 300
    page.padding = 30

    # Display
    display_text = ft.Text("0", size=30)

    display = ft.Container(
        content=display_text,
        bgcolor=ft.Colors.BLACK12,
        border_radius=8,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=210,
        height=70,
    )

    # Acción de botones numéricos
    def number_click(i):
        value = i.control.content.value
        if display_text.value == "0":
            display_text.value = value
        else:
            display_text.value += value
        page.update()

    # Borrar
    def clear(i):
        display_text.value = "0"
        page.update()

    # Grid
    grid = ft.GridView(
        runs_count=3,
        spacing=10,
        run_spacing=10,
        width=210,
        height=210,
        expand=False
    )

    # Botones
    grid.controls.extend([
        ft.ElevatedButton(
            content=ft.Text("1",color=ft.Colors.BLACK),
            bgcolor=ft.Colors.PINK_100,
            width=100,
            height=50,
            on_click=number_click
        ),
        ft.ElevatedButton(
            content=ft.Text("2",color=ft.Colors.BLACK),
            bgcolor=ft.Colors.PURPLE_100,
            width=100,
            height=50,
            on_click=number_click
        ),
        ft.ElevatedButton(
            content=ft.Text("3",color=ft.Colors.BLACK),
            bgcolor=ft.Colors.BLUE_100,
            width=100,
            height=50,
            on_click=number_click
        ),
        ft.ElevatedButton(
            content=ft.Text("4",color=ft.Colors.BLACK),
            bgcolor=ft.Colors.GREEN_100,
            width=100,
            height=50,
            on_click=number_click
        ),
        ft.ElevatedButton(
            content=ft.Text("5",color=ft.Colors.BLACK),
            bgcolor=ft.Colors.TEAL_50,
            width=100,
            height=50,
            on_click=number_click
        ),
        ft.ElevatedButton(
            content=ft.Text("C",color=ft.Colors.BLACK),
            bgcolor=ft.Colors.RED_ACCENT_700,
            width=100,
            height=50,
            on_click=clear
        ),
    ])

    page.add(
        ft.Column(
            controls=[display, grid],
            tight=True
        )
    )

ft.app(target=main)
