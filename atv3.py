import flet as ft


def main(page: ft.Page):
    page.title = "Informações"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.BLUE_GREY_100

    # Campo de nome
    nome = ft.TextField(
        label="Digite seu nome",
        width=250,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
    )

    # Checkbox dos termos
    termos = ft.Checkbox(
        label="Aceito os termos",
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
    )

    # Mensagem
    mensagem = ft.Text(
        "",
        color=ft.Colors.GREEN,
        text_align=ft.TextAlign.CENTER,
    )

    # Função do botão
    def enviar(e):
        if nome.value == "":
            mensagem.value = "Digite seu nome."
            mensagem.color = ft.Colors.RED

        elif not termos.value:
            mensagem.value = "Aceite os termos."
            mensagem.color = ft.Colors.RED

        else:
            mensagem.value = (
                f"Obrigado, {nome.value}! "
            )
            mensagem.color = ft.Colors.GREEN

            # Limpar campos
            nome.value = ""
            termos.value = False

        page.update()

    # Botão
    botao = ft.ElevatedButton(
        "Enviar",
        on_click=enviar,
    )

    # Container
    caixa = ft.Container(
        width=350,
        padding=30,
        bgcolor=ft.Colors.BLACK,
        border_radius=20,

        content=ft.Column(
            controls=[
                nome,
                termos,
                botao,
                mensagem,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
    )

    page.add(caixa)


ft.app(target=main)
