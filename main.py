import flet as ft

def main(page: ft.Page):
    # Definir o tamanho da janela
    page.window_width = 460
    page.window_height = 550

    # Background da janela
    page.bgcolor = ft.colors.WHITE24

    # Nome do app
    page.title= "TAREFAS"
    nome_app = ft.Text("APLICATIVO DE TAREFAS", color=ft.colors.WHITE60, size=20, weight=ft.FontWeight.BOLD)
    
    # App Bar 
    app_bar = page.appbar = ft.AppBar(
        leading= ft.Icon(ft.icons.CHECKLIST_OUTLINED, color=ft.colors.WHITE60),
        leading_width=40,
        title= nome_app,
        center_title= True,
        bgcolor= ft.colors.BLUE_500
    )

    # Fechar notificação
    def fechar_notificacao(e):
        page.banner.open = False
        page.update()

    # Cria uma notificação que aparece quando o campo de tarefa está vazio
    page.banner = ft.Banner(
        bgcolor= ft.colors.BLUE_300,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER_700, size=45),
        content=ft.Text("INSIRA ALGUM VALOR", color=ft.colors.WHITE60, size=20),
        actions=[
            ft.TextButton("OK", on_click= fechar_notificacao,),
        ],
    )

    # Lista para armazenar referências aos checkboxes de tarefa e as linhas de tarefa
    tarefas_checkboxes = []
    tarefas_rows = []
    
    # Função pra adicionar tarefa
    def add_tarefa(e):
        # Verifica se o campo tá vazio ou tem espaço
        if nova_tarefa.value.strip() == "":
            # notifica que está vazio
            page.banner.open = True
            # atualiza a pagina para exibir a notificação
            page.update()
        else:
            # Cria a nova tarefa
            tarefa_texto = nova_tarefa.value
            # Cria uma nova tarefa em forma de Checkbox
            tarefa_checkbox = ft.Checkbox(label=tarefa_texto)
            # Adiciona a tarefa criada como Checkbox a lista
            tarefas_checkboxes.append(tarefa_checkbox) 

            # Botão de editar e excluir 
            botao_editar = ft.IconButton(ft.icons.EDIT, on_click=lambda e: editar_tarefa(e, tarefa_checkbox))
            botao_excluir = ft.IconButton(ft.icons.DELETE, on_click=lambda e: excluir_tarefa(e, tarefa_row))

            # Cria uma Linha contendo o Checkbox e os botões
            tarefa_row = ft.Row([tarefa_checkbox, botao_editar, botao_excluir], alignment="spaceBetween")
            # Adiciona essa linha criada a lista de linhas de tarefas
            tarefas_rows.append(tarefa_row)

            # Adicionar a linha
            page.add(tarefa_row)

            # Limpa o campo de nova_tarefa e foca nele
            nova_tarefa.value = ""
            nova_tarefa.focus()

            # Atualiza a pagina e exibe a nova tarefa
            page.update()
            nova_tarefa.update()

    
    # Função para excluir a tarefa
    def excluir_tarefa(e, tarefa_row):
        if tarefa_row in tarefas_rows:
            # Remove a linha de lista de linhas de tarefas
            tarefas_rows.remove(tarefa_row)
            # Remove a linha da página
            page.remove(tarefa_row)
            # Atualiza a página
            page.update()
    


    # Função para editar a tarefa
    def editar_tarefa(e, tarefa_checkbox):
        # Cria um campo de edição com o texto atual da tarefa
        edicao_tarefa = ft.TextField(label="Tarefa", value=tarefa_checkbox.label)  
        # Cria uma tela com os botões de salvar e cancelar
        page.dialog = ft.AlertDialog(
            title=ft.Text("Editar Tarefa"),
            content=edicao_tarefa,
            actions=[
                ft.TextButton("Salvar", on_click=lambda e: salvar_edicao(e, tarefa_checkbox, edicao_tarefa)),
                ft.TextButton("Cancelar", on_click=lambda e: setattr(page.dialog, 'open', False) or page.update())
            ]
        )
        # Abre a nova tela e atualiza a pagina
        page.dialog.open = True
        page.update()

    # Função para salvar a edição
    def salvar_edicao(e, tarefa_checkbox, edicao_tarefa):
        # Atualiza o texto da tarefa
        tarefa_checkbox.label = edicao_tarefa.value
        # Fecha a tela 
        page.dialog.open = False
        page.update()  # Atualiza a página para refletir a edição
    

    # Criando valores para os campos
    nova_tarefa = ft.TextField(hint_text="O que precisa ser feito", width=300)
    botao_adicionar = ft.ElevatedButton("ADICIONAR", on_click= add_tarefa, color=ft.colors.WHITE60 )

    # Adicionando os itens criados para a pagina
    page.add(app_bar)
    page.add(ft.Row([nova_tarefa, botao_adicionar]) )
    # Definindo um scroll
    page.scroll = "auto"



# Inicia o aplicativo
ft.app(target=main)