import flet as ft

def main(page: ft.Page):

    # Configurações básicas da página
    page.title = "Meu primeiro App Flet", # titulo que aparece na aba do navegador
    page.padding = 20 # espaçamento interno da página

    # criando nosso primeiro elemento: um texto
    meu_texto = ft.Text(
        value="🎊 Primeiro app desenvolvido com Flet!",
        size=24,
        color=ft.Colors.BLUE,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    page.add(meu_texto)

    # adicionando o texto na nossa página
    page.add(
        ft.Text("Bem-vindo ao mundo do desenvolvimento mobile!", size=16),
        ft.Text("Com let, você pode criar apps incriveis.", size=16, color=ft.Colors.GREEN)
    )

ft.app(target=main)