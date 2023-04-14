import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    titulo1 = ft.Text('Ficha Cadastral',
                      size = 20)
    nome1 = ft.TextField(label = 'Digite o Nome:')
    sobrenome1 = ft.TextField(label = 'Digite o Sobrenome:')
    data_nasc1 = ft.TextField(label = 'Digite a Data de Nascimento:')
    rg1 = ft.TextField(label = 'Digite o RG:')
    cpf1 = ft.TextField(label = 'Digite o CPF:')
    
    bloco1 = ft.Row(controls = [titulo1])
    bloco2 = ft.Row(controls = [nome1, sobrenome1])
    bloco3 = ft.ResponsiveRow(controls = [
        ft.Column(controls = [data_nasc1],
                  col = {'sm': 6, 'md': 4, 'xl':2}),
        ft.Column(controls = [ft.Row(controls = [rg1, cpf1])],
                  col = {'sm': 6, 'md': 4, 'xl': 2})])
    
    page.add(bloco1, bloco2, bloco3)
    
ft.app(target = main)
