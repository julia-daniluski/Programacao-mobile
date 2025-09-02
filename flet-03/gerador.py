import flet as ft
import random
import string

def main(page: ft.Page):
    page.title = "Gerador e Analisador de Senhas"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 550
    page.window_height = 700
    page.padding = 20

    senha_atual = ""

    # ---------------- FUNÇÕES ----------------
    def gerar_senha(e):
        nonlocal senha_atual
        comprimento = int(slider.value)
        caracteres = ""

        if upper_switch.value:
            caracteres += string.ascii_uppercase
        if lower_switch.value:
            caracteres += string.ascii_lowercase
        if numbers_switch.value:
            caracteres += string.digits
        if symbols_switch.value:
            caracteres += string.punctuation

        if caracteres:
            senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
            senha_output.value = senha
            senha_atual = senha
            copiar_btn.visible = True
            limpar_btn.visible = True
        else:
            senha_output.value = "Selecione ao menos um tipo de caractere."
            senha_atual = ""
            copiar_btn.visible = False
            limpar_btn.visible = False

        page.update()

    def mostrar_senha_copiada(e):
        if senha_atual:
            text_display.value = f"Senha copiada: {senha_atual}"
            text_display.visible = True
            page.update()
            try:
                page.set_clipboard(senha_atual)
            except:
                pass

    def limpar_senha(e):
        nonlocal senha_atual
        senha_atual = ""
        senha_output.value = ""
        text_display.value = ""
        text_display.visible = False
        copiar_btn.visible = False
        limpar_btn.visible = False
        page.update()

    def toggle_theme(e):
        nonlocal is_dark
        is_dark = not is_dark
        page.theme_mode = ft.ThemeMode.DARK if is_dark else ft.ThemeMode.LIGHT
        theme_button.icon = ft.Icons.DARK_MODE if is_dark else ft.Icons.LIGHT_MODE
        page.update()

    # ---- Função para analisar senha digitada ----
    def analisar_senha(e):
        senha = senha_input.value
        if not senha:
            analise_text.value = "Digite uma senha para analisar."
            analise_text.color = ft.Colors.ORANGE
        else:
            problemas = []
            if len(senha) < 8:
                problemas.append("❌ Mínimo de 8 caracteres")
            if not any(c.islower() for c in senha):
                problemas.append("❌ Precisa de letra minúscula")
            if not any(c.isupper() for c in senha):
                problemas.append("❌ Precisa de letra maiúscula")
            if not any(c.isdigit() for c in senha):
                problemas.append("❌ Precisa de número")
            if not any(c in string.punctuation for c in senha):
                problemas.append("❌ Precisa de símbolo")

            if problemas:
                analise_text.value = "Senha fraca:\n" + "\n".join(problemas)
                analise_text.color = ft.Colors.RED
            else:
                analise_text.value = "✅ Senha forte!"
                analise_text.color = ft.Colors.GREEN
        analise_text.visible = True
        page.update()

    # ---------------- COMPONENTES ----------------
    is_dark = False

    theme_button = ft.IconButton(
        icon=ft.Icons.LIGHT_MODE,
        on_click=toggle_theme
    )

    title_switch_row = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("🔐 Gerador e Analisador de Senhas", size=22, weight="bold"),
            theme_button
        ]
    )

    senha_output = ft.TextField(
        value="",
        label="Senha Gerada",
        read_only=True,
        width=300,
        bgcolor=ft.Colors.PURPLE_100,
        border_color=ft.Colors.PURPLE,
        color=ft.Colors.BLACK,
        label_style=ft.TextStyle(color=ft.Colors.BLACK)
    )

    text_display = ft.Text(
        value="",
        color=ft.Colors.GREEN,
        visible=False
    )

    copiar_btn = ft.ElevatedButton(
        text="Copiar Senha",
        on_click=mostrar_senha_copiada,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.PURPLE,
        width=200,
        visible=False
    )

    limpar_btn = ft.ElevatedButton(
        text="Limpar",
        on_click=limpar_senha,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.PURPLE_700,
        width=200,
        visible=False
    )

    slider = ft.Slider(
        min=8,
        max=20,
        value=12,
        divisions=12,
        label="CARACTERES: {value}",
        active_color=ft.Colors.PURPLE,
        inactive_color=ft.Colors.PURPLE_200
    )

    # ---- Switches com cor personalizada ----
    upper_switch = ft.Switch(
        label="Letras maiúsculas",
        active_color=ft.Colors.PURPLE,
        track_color=ft.Colors.PURPLE_100,
        label_style=ft.TextStyle(color=ft.Colors.PURPLE)
    )

    lower_switch = ft.Switch(
        label="Letras minúsculas",
        value=True,
        active_color=ft.Colors.PURPLE,
        track_color=ft.Colors.PURPLE_100,
        label_style=ft.TextStyle(color=ft.Colors.PURPLE)
    )

    numbers_switch = ft.Switch(
        label="Incluir números",
        active_color=ft.Colors.PURPLE,
        track_color=ft.Colors.PURPLE_100,
        label_style=ft.TextStyle(color=ft.Colors.PURPLE)
    )

    symbols_switch = ft.Switch(
        label="Incluir símbolos",
        active_color=ft.Colors.PURPLE,
        track_color=ft.Colors.PURPLE_100,
        label_style=ft.TextStyle(color=ft.Colors.PURPLE)
    )

    preferencias_column = ft.Column(
        [
            ft.Text("⚙️ PREFERÊNCIAS", size=16, weight="bold", color=ft.Colors.PURPLE_800),
            upper_switch,
            lower_switch,
            numbers_switch,
            symbols_switch,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.START,
        spacing=10
    )

    gerar_button = ft.ElevatedButton(
        text="Gerar Senha",
        on_click=gerar_senha,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.PURPLE,
        width=250
    )

    # ---- Área para analisar senha digitada ----
    senha_input = ft.TextField(
        label="Digite sua senha",
        password=True,
        can_reveal_password=True,
        width=200,
        border_color=ft.Colors.PURPLE
    )

    enviar_btn = ft.ElevatedButton(
        text="Enviar",
        on_click=analisar_senha,
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.PURPLE,
        width=100
    )

    analise_text = ft.Text(
        value="",
        visible=False,
        size=14,
        weight="bold"
    )

    # ---------------- LAYOUT ----------------
    page.add(
        ft.Column(
            [
                title_switch_row,
                senha_output,
                senha_input,
                text_display,
                ft.Row([copiar_btn, limpar_btn], spacing=10, alignment="center"),
                slider,
                preferencias_column,
                gerar_button,
                ft.Divider(),
                # linha com campo, botão e resultado lado a lado
                ft.Row(
                    [
                        enviar_btn,
                        analise_text
                    ],
                    spacing=10,
                    alignment=ft.MainAxisAlignment.START,
                    vertical_alignment=ft.CrossAxisAlignment.START
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
    )

ft.app(
    target=main,
    assets_dir="assets"
)
