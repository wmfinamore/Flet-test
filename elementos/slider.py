import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    def altera_potencia(val):
        num1.value = val.control.value
        page.update()
        
    num1 = ft.Text()
    
    slider1 = ft.Slider(min = 0,
                        max = 100,
                        divisions = 10,
                        label = '{value}',
                        on_change = altera_potencia)
    
    page.add(num1, slider1)
    
ft.app(target = main)
