import flet
from flet import Page, Row, TextField, icons, IconButton

def main(page: Page):
    page.title = 'Meu programa'
    page.vertical_alignment = 'center'
    
    valor1 = TextField(value = '0',
                       text_align = 'right',
                       width = 80)
    
    def diminui_num(num):
        valor1.value = int(valor1.value) - 1
        page.update()
        
    def aumenta_num(num):
        valor1.value = int(valor1.value) + 1
        page.update()
        
    page.add(Row([
        IconButton(icons.REMOVE, on_click = diminui_num),
        valor1,
        IconButton(icons.ADD, on_click = aumenta_num)
    ],
    alignment='center'             
    ))
    
flet.app(target = main)
