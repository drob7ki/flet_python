import flet as ft

def main (page: ft.Page):
    page.title = "cartão de apresentação"

    page.add(ft.Text("Júlia PL", color="#FFFFC5", size=25))

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.padding = ft.Padding(top=30, left=0, right=0)
    

    # Força o tamanho de uma tela de celular no desktop
    page.window.width = 320
    page.window.height = 600
    
    page.add(ft.Text("Estudante de programação mobile"))

    

ft.app(target=main)



ft.run(main)