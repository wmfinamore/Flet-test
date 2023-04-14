import flet as ft

def main(page: ft.Page):
    
    page.add(
        ft.Row(
            controls = [
                ft.Text('Texto 1'),
                ft.Text('Texto 2'),
                ft.Text('Texto 3'),
            ]
        )
    )
    
ft.app(target = main)
