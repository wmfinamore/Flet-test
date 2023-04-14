import flet as ft

def main(page: ft.Page):
    
    page.title = 'Meu Programa'
    page.bgcolor = 'white'
    
    bloco1 = ft.Container(
        content = ft.Text('Ficha Cadastral',
                          color = 'black',
                          size = 20,
                          weight = 'bold',),
        bgcolor = ft.colors.BLUE_100,
        border_radius = ft.border_radius.all(25),
        padding = 5
    )
    page.add(bloco1)
    
ft.app(target = main)