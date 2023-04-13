import flet as ft

def main(page: ft.Page):
    page.window_width = 450
    page.window_height = 300
    page.title = 'Meu Programa Básico'
    #page.vertical_alignment = 'center'
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.bgcolor = ft.colors.AMBER_50
    page.padding = 20
    
    ft.Text()
    titulo1 = ft.Text('Cadastro de Paciente')
    titulo2 = ft.Text(value = 'Cadastro de Paciente',
                      color = 'blue',
                      size = 18,
                      weight = 'bold',
                      font_family = 'Open Sans')
    
    page.add(titulo1, titulo2)
    
    page.update()
    
ft.app(target = main)
