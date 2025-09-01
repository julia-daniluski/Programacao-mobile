import flet as ft

def main(page: ft.Page):
    page.title ="Campo de Texto"
    page.padding = ft.padding.only(top=48, left=20, right=20, bottom=20) #Padding superior para area segura
    #Criando um campo onde o usuário pode digitar
    campo_nome = ft.TextField(
        label="Digite seu nome aqui",
        width=300, 
        border_color=ft.Colors.BLUE 
    )
#Texto que mostrará a resposta
    resposta = ft.Text(
        value="", #Inicialmente vazio
        size=18,
        text_align=ft.TextAlign.CENTER
    )
    def processar_nome(evento):
    #Pegando o valor digitado no campo
        nome_digitado= campo_nome.value
    #Verificando se o usuário realmente digitou algo
        if nome_digitado =="" or nome_digitado is None:
            resposta.value = " Por favor, digite seu nome!"
            resposta.color= ft.Colors.RED
        elif len(nome_digitado) <2:
            resposta.value = "Nome muito curto!"
            resposta.color = ft.Colors.ORANGE
        else:
            resposta.value = f" ola, {nome_digitado}! Prazer em conhecê-lo(a)!"
            resposta.color = ft.Colors.GREEN

        page.update()
    botao_ok = ft.ElevatedButton(
        text="Confirmar",
        on_click=processar_nome,
        width=150
    )
    page.add(
        ft.Text("Vamos nos conhecer!", size=22, weight=ft.FontWeight.BOLD),
        campo_nome,
        botao_ok,
        resposta
    )
ft.app(target=main)