import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    bloco1 = ft.Container(content = ft.Text('Ficha Cadastral'),
                          bgcolor = ft.colors.AMBER_50,
                          border_radius = ft.border_radius.only(topLeft = 5,
                                                         bottomRight = 5),
                          padding = 5,
                          gradient = ft.LinearGradient(begin = ft.alignment.bottom_left,
                                                       end = ft.alignment.top_right,
                                                       colors = [ft.colors.AMBER,
                                                                 ft.colors.AMBER_900]))
    page.add(bloco1)
    
ft.app(target = main)
