import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    img1 = ft.Stack([
        ft.Image(src = f'https://picsum.photos/300/300',
                 width = 300,
                 height = 300,
                 fit = ft.ImageFit.CONTAIN),
        ft.Row([ft.Text('Imagem 001',
                        color = 'White',
                        size = 40,
                        weight = 'bold',
                        opacity = 0.8)],
               alignment = ft.MainAxisAlignment.CENTER)],
                    width = 300,
                    height = 300)
    
    page.add(img1)
    
ft.app(target = main)
