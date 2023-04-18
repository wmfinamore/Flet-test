import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    def seleciona_quarto(v):
        quarto.value = (f'Quarto escolhido: {escolha.value}')
        page.update()
        
    texto1 = ft.Text('Escolha o quarto: ')
    
    escolha = ft.RadioGroup(
        content = ft.Column([
            ft.Radio(value = 'quarto_tipo_1',
                     label = 'Executivo (cama de solteiro + tv + ar)'),
            ft.Radio(value = 'quarto_tipo_2',
                     label = 'Luxo (cama de casal + tv + ar)'),
            ft.Radio(value = 'quarto_tipo_3',
                     label = 'Master (cama de casal + tv + ar + hidromassagem)')
        ])
    )
    
    quarto = ft.Text()
    botao_confirma = ft.ElevatedButton(text = 'Confirma',
                                       on_click = seleciona_quarto)
    page.add(texto1, escolha, botao_confirma, quarto)
    
ft.app(target = main)
