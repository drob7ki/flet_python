import flet as ft


def main(page: ft.Page):
    # Configurações da página
    page.title = "Informações de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_GREY_100

    # Caixa principal
    caixa = ft.Container(
        width=350,
        padding=30,
        bgcolor=ft.Colors.BLACK,
        border_radius=20,

        content=ft.Column(
            controls=[
                # Título
                ft.Text(
                    "Júlia Leme",
                    color=ft.Colors.WHITE,
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                ),

                # Subtítulo
                ft.Text(
                    "Desenvolvedora mobile",
                    color=ft.Colors.WHITE,
                    size=14,
                    text_align=ft.TextAlign.CENTER,
                ),
                
                # E-mail
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.Icons.EMAIL,
                            color=ft.Colors.WHITE,
                        ),
                        ft.Text(
                            "email@exemplo.com",
                            color=ft.Colors.WHITE,
                            size=16,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),

                # Telefone
                ft.Row(
                    controls=[
                        ft.Icon(
                            ft.Icons.PHONE,
                            color=ft.Colors.WHITE,
                        ),
                        ft.Text(
                            "(11) 99999-9999",
                            color=ft.Colors.WHITE,
                            size=16,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
    )

    # Adiciona a caixa na página
    page.add(caixa)


# Inicia o aplicativo
ft.app(target=main)