import flet as ft


def main(page: ft.Page):
    page.title = "Lista de itens"
    page.bgcolor = ft.Colors.BLUE_GREY_100
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    nome = ft.TextField(
        label="Novo item",
        width=220,
        color=ft.Colors.WHITE,
        border_color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color=ft.Colors.WHITE),
    )

    lista = ft.Column(spacing=10)

    def adicionar(e):
        if nome.value.strip() == "":
            return

        quantidade = ft.Text(
            "1",
            width=30,
            text_align=ft.TextAlign.CENTER,
            color=ft.Colors.WHITE,
        )

        def menos(e):
            numero = int(quantidade.value)

            if numero > 1:
                quantidade.value = str(numero - 1)

            page.update()

        def mais(e):
            quantidade.value = str(int(quantidade.value) + 1)
            page.update()

        def excluir(e):
            lista.controls.remove(item)
            page.update()

        item = ft.Row(
            controls=[
                ft.Text(
                    nome.value,
                    color=ft.Colors.WHITE,
                    expand=True,
                ),

                ft.IconButton(
                    icon=ft.Icons.REMOVE,
                    icon_color=ft.Colors.WHITE,
                    on_click=menos,
                ),

                quantidade,

                ft.IconButton(
                    icon=ft.Icons.ADD,
                    icon_color=ft.Colors.WHITE,
                    on_click=mais,
                ),

                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    icon_color=ft.Colors.RED,
                    on_click=excluir,
                ),
            ]
        )

        lista.controls.append(item)
        nome.value = ""
        page.update()

    botao = ft.ElevatedButton(
        "Adicionar",
        icon=ft.Icons.ADD,
        on_click=adicionar,
    )

    caixa = ft.Container(
        width=450,
        padding=30,
        bgcolor=ft.Colors.BLACK,
        border_radius=20,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Lista de itens",
                    size=25,
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Row(
                    controls=[
                        nome,
                        botao,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),

                lista,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
    )

    page.add(caixa)


ft.app(target=main)