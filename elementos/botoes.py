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
    
ft.app(target = main)
