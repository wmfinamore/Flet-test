import flet as ft
from flet import Ref

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    nome1 = Ref[ft.TextField]()
    texto1 = Ref[ft.Column]()
    
    def mensagem1(e):
        texto1.current.controls.append(ft.Text(f'Olá {nome1.current.value}'))
        nome1.current.value = ''
        page.update()
        nome1.current.focus()
    
    page.add(
        ft.TextField(ref = nome1, label = 'Digite o seu nome '),
        ft.ElevatedButton('Dizer Olá', on_click = mensagem1),
        ft.Column(ref = texto1)
    )
    
ft.app(target = main)
