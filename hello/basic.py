import flet as ft

def main(page: ft.Page):
    #page.window_width = 450
    #page.window_height = 300
    page.title = 'Meu Programa Básico'
    #page.vertical_alignment = 'center'
    #page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    #page.bgcolor = ft.colors.AMBER_50
    page.padding = 20
    
    menu1 = ft.Icon(ft.icons.MENU)
    texto1 = ft.Text('Menu')
    pesquisar1 = ft.Icon(ft.icons.SEARCH)
    txtpesquisar1 = ft.Text('Pesquisar')
    page.add(menu1, texto1, pesquisar1, txtpesquisar1)
    
    ft.Text()
    titulo1 = ft.Text('Cadastro de Paciente')
    titulo2 = ft.Text(value = 'Cadastro de Paciente',
                      color = 'blue',
                      size = 18,
                      weight = 'bold',
                      font_family = 'Open Sans')
    
    page.add(titulo1, titulo2)
    
    imagem1 = ft.Image(src = f"https://picsum.photos/536/354",
                       width = 300,
                       height = 300,
                       fit = ft.ImageFit.CONTAIN)
    page.add(imagem1)
    
    page.update()
    
ft.app(target = main)
