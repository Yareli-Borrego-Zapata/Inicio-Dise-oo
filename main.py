import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de Sesión"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    USUARIO = "admin"
    CONTRASENA = "1234"

    usuario = ft.TextField(label="Usuario")
    contrasena = ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    mensaje = ft.Text(color="red")

    def panel():
        page.clean()

        page.add(
            ft.Text("Panel Principal", size=30, weight=ft.FontWeight.BOLD),
            ft.Text("Bienvenido al sistema"),
            ft.Container(height=200),

            ft.NavigationBar(
                destinations=[
                    ft.NavigationBarDestination(
                        icon=ft.Icons.HOME,
                        label="Inicio"
                    ),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.SEARCH,
                        label="Explorar"
                    ),
                    ft.NavigationBarDestination(
                        icon=ft.Icons.PERSON,
                        label="Perfil"
                    ),
                ]
            )
        )

        page.update()

    def login(e):
        if usuario.value.strip() == USUARIO and contrasena.value.strip() == CONTRASENA:
            panel()
        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            page.update()

    boton = ft.ElevatedButton("Entrar", on_click=login)

    page.add(
        ft.Column(
            [
                ft.Text("Inicio de Sesión", size=20, weight=ft.FontWeight.BOLD),
                usuario,
                contrasena,
                boton,
                mensaje
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    )

    ft.app(target=main)