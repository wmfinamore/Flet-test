import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    txt1 = ft.Text('Nome', size = 16)
    nome1 = ft.TextField(label = 'Digite o Nome: ')
    
    page.add(txt1, nome1)
    
    page.update()
    
ft.app(target = main)
