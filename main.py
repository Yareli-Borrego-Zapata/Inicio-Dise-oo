import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de Sesión"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Column(
            [
                ft.Text("Inicio de Sesión", size=20, weight=ft.FontWeight.BOLD),
                ft.TextField(label="Usuario"),
                ft.TextField(label="Contraseña", password=True, can_reveal_password=True),
                ft.ElevatedButton(content ="Entrar"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,))
ft.app(target=main)
