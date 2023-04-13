import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    txt1 = ft.Text('Nome', size = 16)
    nome1 = ft.TextField(label = 'Digite o Nome: ')
    
    page.add(txt1, nome1)
    
    txt2 = ft.Text('Valor final: ', size = 16)
    val2 = ft.TextField(label = 'Digite o valor inteiro',
                        prefix_text = 'R$ ')
    
    txt3 = ft.Text('Desconto aplicado: ', size = 16)
    val3 = ft.TextField(label = 'Digite o percentual',
                        suffix_text = '%')
    page.add(txt2, val2, txt3, val3)
    
    page.update()
    
ft.app(target = main)
