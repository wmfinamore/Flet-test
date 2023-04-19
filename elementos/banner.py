import flet as ft

def main(page: ft.Page):
    base = {'Nome': '',
            'Sobrenome': ''}
    
    def cadastra(var):
        base['Nome'] = nome1.value
        base['Sobrenome'] =nome2.value
        for i in base.values():
            if not i:
                banner.open = True
                page.update()
        return
    
    def fecha_banner(var):
        banner.open = False
        page.update()
        
    banner = page.banner = ft.Banner(bgcolor = ft.colors.AMBER_100,
                                     leading = ft.Icon(ft.icons.DANGEROUS_SHARP,
                                                       color = ft.colors.RED_400,
                                                       size = 40),
                                     content = ft.Text('Existem campos não preenchidos no formulário',
                                                       color = 'red'),
                                     actions = [ft.TextButton('Confirmar',
                                                              on_click = fecha_banner)]
                                     )
    nome1 = ft.TextField(label = 'Digite o Nome: ')
    nome2 = ft.TextField(label = 'Digite o Sobrenome: ')
    
    botao_cadastrar = ft.FilledButton(text = 'Cadastrar',
                                      on_click = cadastra)
    page.add(banner, nome1, nome2, botao_cadastrar)
    
ft.app(target = main)
