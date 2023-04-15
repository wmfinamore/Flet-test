import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    abas_pag1 = ft.Tabs(selected_index = 0,
                        animation_duration = 200,
                        tabs = [
                            ft.Tab(text = 'Pacientes',
                                   content = ft.Container(
                                       content = ft.Text('Relação de pacientes')
                                   )),
                            ft.Tab(text = 'Médicos',
                                   content = ft.Container(
                                       content = ft.Text('Relação de médicos')
                                   )),
                            ft.Tab(text = 'Funcionários',
                                   content = ft.Container(
                                       content = ft.Text('Relação de funcionários')
                                   ))
                        ])
    page.add(abas_pag1)
    
ft.app(target = main)
