import flet as ft

def main(page: ft.Page):
    page.title = "✅ Lista de Tarefas"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.scroll = ft.ScrollMode.AUTO

    tarefas = []

    input_tarefa = ft.TextField(
        label="Nova tarefa",
        hint_text="Digite a descrição da tarefa...",
        width=400,
        autofocus=True
    )

    lista_tarefas = ft.Column(spacing=10)

    status_tarefa = ft.Text(
        value="Nenhuma tarefa adicionada ainda!",
        color=ft.Colors.GREY,
        size=14,
        text_align=ft.TextAlign.CENTER
    )

    def atualizar_status():
        total = len(tarefas)
        concluidas = len([t for t in tarefas if t["concluida"]])
        pendentes = total - concluidas
        status_tarefa.value = f"📋 Total: {total} | ✅ Concluídas: {concluidas} | 🕒 Pendentes: {pendentes}"

    def atualizar_lista():
        lista_tarefas.controls.clear()

        for i, tarefa in enumerate(tarefas):
            check = ft.Checkbox(
                label=tarefa["descricao"],
                value=tarefa["concluida"],
                on_change=lambda e, i=i: alternar_conclusao(i)
            )

            excluir_btn = ft.IconButton(
                icon=ft.icons.DELETE,
                tooltip="Excluir tarefa",
                on_click=lambda e, i=i: excluir_tarefa(i),
                icon_color=ft.Colors.RED
            )

            lista_tarefas.controls.append(
                ft.Row(
                    controls=[check, excluir_btn],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )

        atualizar_status()
        page.update()

    def alternar_conclusao(index):
        tarefas[index]["concluida"] = not tarefas[index]["concluida"]
        atualizar_lista()

    def excluir_tarefa(index):
        del tarefas[index]
        atualizar_lista()

    def adicionar_tarefa(e):
        descricao = input_tarefa.value.strip()
        if descricao:
            tarefas.append({"descricao": descricao, "concluida": False})
            input_tarefa.value = ""
            atualizar_lista()
        else:
            input_tarefa.error_text = "A descrição não pode estar vazia."
        page.update()

    def limpar_tarefas(e):
        tarefas.clear()
        atualizar_lista()

    def excluir_concluidas(e):
        global tarefas
        tarefas = [t for t in tarefas if not t["concluida"]]
        atualizar_lista()

    def concluir_todas(e):
        for tarefa in tarefas:
            tarefa["concluida"] = True
        atualizar_lista()

    # Layout principal
    page.add(
        ft.Column([
            ft.Text("📝 Lista de Tarefas", size=24, weight=ft.FontWeight.BOLD),
            input_tarefa,
            ft.Row([
                ft.ElevatedButton("➕ Adicionar", on_click=adicionar_tarefa),
                ft.ElevatedButton("🗑️ Limpar Tudo", on_click=limpar_tarefas, bgcolor=ft.Colors.RED),
            ], spacing=20),
            lista_tarefas,
            status_tarefa,
            ft.Divider(),
            ft.Row([
                ft.ElevatedButton("❌ Excluir Concluídas", on_click=excluir_concluidas),
                ft.ElevatedButton("✅ Concluir Todas", on_click=concluir_todas),
            ], spacing=20)
        ],
        spacing=25,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

    atualizar_lista()

ft.app(target=main)

