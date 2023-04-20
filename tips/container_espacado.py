import flet as ft

def main(page: ft.Page):
    menu1 = ft.Icon(ft.icons.MENU)
    pesquisar = ft.Icon(ft.icons.SEARCH)
    
    pagina1 = ft.Container(content = ft.Column(
        controls = [ft.Row(
            controls = [ft.Text('Olá Mundo!!!')]),
                    ft.Container(height = 25), #Container como espaçador entre elementos
                    ft.Text('Python > Dart')]))
    page.add(menu1, pesquisar, pagina1)
    
ft.app(target = main)
