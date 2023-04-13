import flet as ft

def main(page = ft.Page):
    page.title = 'Meu programa'
    
    base = {
        'Nome': '',
        'Sobrenome': '',
    }
    
    def cadastra(dados):
        base['Nome'] = nome1.value
        base['Sobrenome'] = nome2.value
        nome_completo.value = '{} {}'.format(base['Nome'], base['Sobrenome'])
        page.update()
        
    nome1 = ft.TextField(label = 'Digite o Nome: ')
    nome2 = ft.TextField(label = 'Digite o Sobrenome: ')
    nome_completo = ft.Text(value = '',
                            size = 20,
                            color = 'red',
                            )
    
    botao_cadastrar = ft.FilledButton(text = 'Cadastrar',
                                      on_click = cadastra)
    
    
    page.add(nome1, nome2, botao_cadastrar, nome_completo)
    
    
ft.app(target = main)
