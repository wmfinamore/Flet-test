import flet as ft

def main(page: ft.Page):
    txts_ = ['Texto 1', 'Texto 2', 'Texto 3']
    txts = []
    
    for txt in txts_:
        txts.append(ft.Text(txt))
        
    page.add(
        ft.Row(controls = txts)
    )
    
ft.app(target = main)
