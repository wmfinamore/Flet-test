import flet as ft

def main(page: ft.Page):
    page.window_width = 450
    page.window_height = 300
    page.title = 'Meu Programa Básico'
    page.vertical_alignment = 'center'
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.AMBER_50
    page.padding = 20
    page.update()
    
ft.app(target = main)
