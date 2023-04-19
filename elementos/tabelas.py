import flet as ft

def main(page: ft.Page):
    page.title = 'Meu Programa'
    
    tabela1 = ft.DataTable(
        columns=[ft.DataColumn(ft.Text('Nome')),
                 ft.DataColumn(ft.Text('Idade')),
                 ft.DataColumn(ft.Text('Peso')),
                 ft.DataColumn(ft.Text('Altura')),],
        rows = [ft.DataRow(cells = [
            ft.DataCell(ft.Text('Fernando Feltrin')),
            ft.DataCell(ft.Text('35')),
            ft.DataCell(ft.Text('115')),
            ft.DataCell(ft.Text('1,90')),
            ]),
                ft.DataRow(cells = [
                    ft.DataCell(ft.Text('João da Silva')),
                    ft.DataCell(ft.Text('49')),
                    ft.DataCell(ft.Text('98')),
                    ft.DataCell(ft.Text('1,76')),
            ])
        ]
    )
    page.add(tabela1)
    
ft.app(target = main)
