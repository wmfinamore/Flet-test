import flet as ft

def main(page: ft.Page):
    page.add(ft.Text(value = 'Olá Mundo!!!!'))
    page.update()
    
ft.app(target = main, view = ft.WEB_BROWSER)