import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    texto1 = ft.Tooltip(content = ft.Text('Cadastro de Clientes'),
                        message = 'Apenas clientes...')
    page.add(texto1)
    
ft.app(target = main)
