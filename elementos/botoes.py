import flet as ft

def main(page: ft.Page):
    txt1 = ft.Text('Exemplo de botão')
    
    botao1 = ft.ElevatedButton(text = 'Salvar',
                               color = 'white',
                               bgcolor = 'black',
                               width = 200,
                               height = 50,
                               on_click = lambda x: print('Botão clicando...'))
    page.add(txt1, botao1)
    
    txt2 = ft.Text('Exemplo de botão preenchido')# não permite definição de cor de fundo
    
    botao2 = ft.FilledButton(text = 'Salvar',
                             width = 200,
                             height = 50,
                             on_click = lambda x: print('Botão clicado...'))
    page.add(txt2, botao2)
    
    txt3 = ft.Text('Exemplo de botão preenchido')# Coloração visível durante a interação
    
    botao3 = ft.FilledTonalButton(text = 'Salvar',
                             width = 200,
                             height = 50,
                             on_click = lambda x: print('Botão clicado...'))
    page.add(txt3, botao3)
    
    txt4 = ft.Text('Exemplo de botão flutuante')# Botão flutuante
    
    botao4 = ft.FloatingActionButton(text = 'Add',
                             on_click = lambda x: print('Botão clicado...'))
    page.add(txt4, botao4)
    
    
ft.app(target = main)
