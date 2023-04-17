import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    def confirma(v):
        opcoes.value = (f'{opcao1.value}', {opcao2.value}, {opcao3.value}, {opcao4.value}, {opcao5.value}, {opcao6.value})
        
        page.update()
        
    texto1 = ft.Text('Selecione os condimentos')
    
    opcao1 = ft.Checkbox(label = 'Maionese', value = False)
    opcao2 = ft.Checkbox(label = 'Ketchup', value = False)
    opcao3 = ft.Checkbox(label = 'Mostarda', value = False)
    opcao4 = ft.Checkbox(label = 'Pimenta', value = False)
    opcao5 = ft.Checkbox(label = 'Molho Barbecue', value = False)
    opcao6 = ft.Checkbox(label = 'Molho Lemon Pepper', value = False)
    
    opcoes = ft.Text()
    
    botao_confirma = ft.ElevatedButton(text = 'Confirma', on_click = confirma)
    
    page.add(texto1, opcao1, opcao2, opcao3, opcao4, opcao5, opcao6, botao_confirma, opcoes)
    
ft.app(target = main)
