import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    sidebar = ft.NavigationRail(
        selected_index = 0,
        min_width = 100,
        height = 170,
        extended = True,
        min_extended_width = 250,
        leading = ft.Text('Menu Principal',
                           size = 16),
        group_alignment = -0.9,
        destinations = [
        ft.NavigationRailDestination(label = 'Agenda Consulta',
                                     icon = ft.icons.BOOKMARK,
                                     selected_icon = ft.icons.BOOKMARK_ROUNDED),
        ft.NavigationRailDestination(label = 'Cadastrar Paciente',
                                     icon = ft.icons.CREATE,
                                     selected_icon = ft.icons.CREATE_OUTLINED),
        ft.NavigationRailDestination(label = 'Administrativo',
                                     icon = ft.icons.SETTINGS,
                                     selected_icon = ft.icons.SETTINGS_OUTLINED)],
        on_change = lambda e: print('Destino selectionado: ', e.control.selected_index)
    )
    
    page.add(ft.Row([sidebar,
                     ft.VerticalDivider(width = 1),
                     ft.Column([ft.Text('Conteúdo da página')],
                               alignment = ft.MainAxisAlignment.START,
                               expand = True)],
                    expand = True))

ft.app(target = main)
    