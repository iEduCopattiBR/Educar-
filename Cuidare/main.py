from kivy.app import App

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner

import sqlite3
from datetime import datetime

#===========================================================
#                   BANCO DE DADOS
#===========================================================

def criar_banco():

    conexao = sqlite3.connect('cuidare.db')

    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conteudos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            titulo TEXT NOT NULL,
            texto TEXT NOT NULL,
            data_criacao TEXT NOT NULL
        )
    ''')

    conexao.commit()

    conexao.close()

# ==========================================================
#              BUSCAR CONTEÚDOS DO BANCO
# ==========================================================

def buscar_conteudos(categoria):

    conexao = sqlite3.connect('cuidare.db')

    cursor = conexao.cursor()

    cursor.execute(
        '''
        SELECT titulo, texto
        FROM conteudos
        WHERE categoria = ?
        ORDER BY id DESC
        ''',
        (categoria,)
    )

    resultados = cursor.fetchall()

    conexao.close()

    return resultados

# ==========================================================
#                    TELA INICIAL
# ==========================================================

class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # ----------------------------------------------------
        # Layout principal
        # ----------------------------------------------------

        layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            padding=50
        )

        # ----------------------------------------------------
        # Título
        # ----------------------------------------------------

        titulo = Label(
            text='Cuidarê',
            font_size=50
        )

        # ----------------------------------------------------
        # Subtítulo
        # ----------------------------------------------------

        subtitulo = Label(
            text='Cuidar é responsabilidade.\n'
                 'Conhecer é parte dela.',
            font_size=16
        )

        # ----------------------------------------------------
        # Descrição
        # ----------------------------------------------------

        subtitulo2 = Label(
            text='Cuidarê reúne informações práticas\n'
                 'e conteúdos elaborados com profissionais\n'
                 'para ajudar quem cuida de crianças\n'
                 'a oferecer um cuidado mais seguro e consciente.',
            font_size=12,
            size_hint_x=0.5,
            size_hint_y=None,
            height=70,
            pos_hint={'center_x': 0.5},
            text_size=(None, None),
            halign='center',
            valign='middle'
        )

        # ----------------------------------------------------
        # Frase
        # ----------------------------------------------------

        subtitulo3 = Label(
            text='Conhecimento para quem cuida!',
            font_size=16
        )

        # ====================================================
        #                    BOTÕES
        # ====================================================

        botao_sos = Button(
            text='S.O.S',
            size_hint_x=0.4,
            size_hint_y=None,
            height=40,
            pos_hint={'center_x': 0.5}
        )

        botao_guia = Button(
            text='Guia de Cuidados',
            size_hint_x=0.4,
            size_hint_y=None,
            height=40,
            pos_hint={'center_x': 0.5}
        )

        botao_cursos = Button(
            text='Cursos',
            size_hint_x=0.4,
            size_hint_y=None,
            height=40,
            pos_hint={'center_x': 0.5}
        )

        botao_profissionais = Button(
            text='Profissionais',
            size_hint_x=0.4,
            size_hint_y=None,
            height=40,
            pos_hint={'center_x': 0.5}
        )

        botao_gerenciar = Button(
            text='Gerenciar Conteúdos',
            size_hint_x=0.4,
            size_hint_y=None,
            height=40,
            pos_hint={'center_x': 0.5}
        )

        # ====================================================
        #                    CORES
        # ====================================================

        botao_sos.background_color = (1, 0, 0, 1)

        botao_guia.background_color = (0, 0, 1, 1)

        botao_cursos.background_color = (0, 1, 0, 1)

        botao_profissionais.background_color = (0, 0, 1, 1)

        # ====================================================
        #               ADICIONANDO À TELA
        # ====================================================

        layout.add_widget(titulo)
        layout.add_widget(subtitulo)
        layout.add_widget(subtitulo2)
        layout.add_widget(subtitulo3)

        layout.add_widget(botao_sos)
        layout.add_widget(botao_guia)
        layout.add_widget(botao_cursos)
        layout.add_widget(botao_profissionais)
        layout.add_widget(botao_gerenciar)

        # ====================================================
        #                 FUNÇÕES DOS BOTÕES
        # ====================================================

        botao_sos.bind(
            on_press=self.abrir_sos
        )

        botao_guia.bind(
            on_press=self.abrir_guia
        )

        botao_cursos.bind(
            on_press=self.abrir_cursos
        )

        botao_profissionais.bind(
            on_press=self.abrir_profissionais
        )

        botao_gerenciar.bind(
            on_press=self.abrir_gerenciar
        )

        self.add_widget(layout)

    # ======================================================
    #                  NAVEGAÇÃO
    # ======================================================

    def abrir_sos(self, instance):
        self.manager.current = 'sos'

    def abrir_guia(self, instance):
        self.manager.current = 'guia'

    def abrir_cursos(self, instance):
        self.manager.current = 'cursos'

    def abrir_profissionais(self, instance):
        self.manager.current = 'profissionais'

    def abrir_gerenciar(self, instance):
        self.manager.current = 'gerenciar' 
        
# ==========================================================
#                       TELA S.O.S
# ==========================================================

class SosScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='S.O.S',
            font_size=50,
            halign='center'
        )

        subtitulo = Label(
            text='Tela de contatos de emergência',
            font_size=18,
            halign='left'
        )

        botao_192 = Button(
            text='192 - SAMU',
            font_size=14
        )

        botao_193 = Button(
            text='193 - Bombeiros',
            font_size=14
        )

        botao_190 = Button(
            text='190 - Polícia',
            font_size=14
        )

        botao_0800_722_6001 = Button(
            text='0800-722-6001\n'
                 'Disque-Intoxicação',
            font_size=14
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=40
        )

        # ====================================================
        #                     CORES
        # ====================================================

        titulo.color = (1, 0, 0, 1)

        botao_192.background_color = (0, 1, 0, 1)

        botao_193.background_color = (0, 0, 1, 1)

        botao_190.background_color = (1, 0, 0, 1)

        botao_0800_722_6001.background_color = (1, 1, 0, 1)

        # ====================================================
        #              ADICIONANDO À TELA
        # ====================================================

        layout.add_widget(titulo)
        layout.add_widget(subtitulo)

        layout.add_widget(botao_192)
        layout.add_widget(botao_193)
        layout.add_widget(botao_190)
        layout.add_widget(botao_0800_722_6001)

        layout.add_widget(botao_voltar)

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'home'


# ==========================================================
#                  TELA GUIA DE CUIDADOS
# ==========================================================

class GuiaScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        scroll = ScrollView(
            size_hint=(1, 1)
        )

        layout = BoxLayout(
            orientation='vertical',
            spacing=10,
            padding=40,
            size_hint_y=None
        )

        layout.bind(
            minimum_height=layout.setter('height')
        )

        # ====================================================
        #                    TÍTULO
        # ====================================================

        titulo = Label(
            text='Guia de Cuidados',
            font_size=40,
            size_hint_y=None,
            height=60
        )

        # ====================================================
        #                    TEXTO
        # ====================================================

        texto = Label(
            text='Selecione uma categoria para conhecer '
                 'mais informações sobre os cuidados infantis.',
            size_hint_y=None,
            height=60,
            halign='center',
            valign='middle'
        )

        # ====================================================
        #                    BOTÕES
        # ====================================================

        botao_alimentacao = Button(
            text='Alimentação',
            size_hint_y=None,
            height=50
        )

        # O texto continua exatamente "Cuidados Básicos"
        botao_Cuidados = Button(
            text='Cuidados Básicos',
            size_hint_y=None,
            height=50
        )

        botao_sono = Button(
            text='Sono e Rotina',
            size_hint_y=None,
            height=50
        )

        botao_seguranca = Button(
            text='Segurança',
            size_hint_y=None,
            height=50
        )

        botao_desenvolvimento = Button(
            text='Desenvolvimento Infantil',
            size_hint_y=None,
            height=50
        )

        botao_brincar = Button(
            text='Brincar e Estimular',
            size_hint_y=None,
            height=50
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=50
        )

        # ====================================================
        #              ADICIONANDO À TELA
        # ====================================================

        layout.add_widget(titulo)
        layout.add_widget(texto)

        layout.add_widget(botao_alimentacao)
        layout.add_widget(botao_Cuidados)
        layout.add_widget(botao_sono)
        layout.add_widget(botao_seguranca)
        layout.add_widget(botao_desenvolvimento)
        layout.add_widget(botao_brincar)

        layout.add_widget(botao_voltar)

        # ====================================================
        #                 FUNÇÕES DOS BOTÕES
        # ====================================================

        botao_alimentacao.bind(
            on_press=self.abrir_alimentacao
        )

        botao_Cuidados.bind(
            on_press=self.abrir_Cuidados
        )

        botao_sono.bind(
            on_press=self.abrir_sono
        )

        botao_seguranca.bind(
            on_press=self.abrir_seguranca
        )

        botao_desenvolvimento.bind(
            on_press=self.abrir_desenvolvimento
        )

        botao_brincar.bind(
            on_press=self.abrir_brincar
        )

        botao_voltar.bind(
            on_press=self.voltar
        )

        # ====================================================
        #                SCROLLVIEW
        # ====================================================

        scroll.add_widget(layout)

        self.add_widget(scroll)

    # ======================================================
    #                    NAVEGAÇÃO
    # ======================================================

    def abrir_alimentacao(self, instance):
        self.manager.current = 'alimentacao'

    def abrir_Cuidados(self, instance):
        self.manager.current = 'cuidados'

    def abrir_sono(self, instance):
        self.manager.current = 'sono'

    def abrir_seguranca(self, instance):
        self.manager.current = 'seguranca'

    def abrir_desenvolvimento(self, instance):
        self.manager.current = 'desenvolvimento'

    def abrir_brincar(self, instance):
        self.manager.current = 'brincar'

    def voltar(self, instance):
        self.manager.current = 'home'


# ==========================================================
#                  TELA ALIMENTAÇÃO
# ==========================================================

class AlimentacaoScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(
            orientation='vertical',
            spacing=15,
            padding=30
        )

        titulo = Label(
            text='Alimentação',
            font_size=40,
            size_hint_y=None,
            height=70
        )

        # --------------------------------------------------
        # ÁREA DE ROLAGEM
        # --------------------------------------------------

        self.scroll = ScrollView()

        self.conteudos_layout = BoxLayout(
            orientation='vertical',
            spacing=15,
            padding=10,
            size_hint_y=None
        )

        self.conteudos_layout.bind(
            minimum_height=self.conteudos_layout.setter('height')
        )

        self.scroll.add_widget(
            self.conteudos_layout
        )

        # --------------------------------------------------
        # BOTÃO VOLTAR
        # --------------------------------------------------

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        botao_voltar.bind(
            on_press=self.voltar
        )

        # --------------------------------------------------
        # ADICIONANDO OS ELEMENTOS
        # --------------------------------------------------

        self.layout.add_widget(titulo)

        self.layout.add_widget(
            self.scroll
        )

        self.layout.add_widget(
            botao_voltar
        )

        self.add_widget(
            self.layout
        )

    # ======================================================
    #       CARREGAR CONTEÚDOS AO ABRIR A TELA
    # ======================================================

    def on_pre_enter(self, *args):

        self.carregar_conteudos()

    # ======================================================
    #              BUSCAR CONTEÚDOS
    # ======================================================

    def carregar_conteudos(self):

        # Limpa o que estava aparecendo anteriormente
        self.conteudos_layout.clear_widgets()

        # Busca no banco somente conteúdos de Alimentação
        resultados = buscar_conteudos(
            'Alimentação'
        )

        # --------------------------------------------------
        # SE NÃO EXISTIR CONTEÚDO
        # --------------------------------------------------

        if not resultados:

            mensagem = Label(
                text='Ainda não existem conteúdos cadastrados.',
                font_size=18,
                size_hint_y=None,
                height=80
            )

            self.conteudos_layout.add_widget(
                mensagem
            )

            return

        # --------------------------------------------------
        # MOSTRAR OS CONTEÚDOS
        # --------------------------------------------------

        for titulo, texto in resultados:

            titulo_label = Label(
                text=titulo,
                font_size=25,
                size_hint_y=None,
                height=60
            )

            texto_label = Label(
                text=texto,
                font_size=18,
                size_hint_y=None,
                height=150
            )

            self.conteudos_layout.add_widget(
                titulo_label
            )

            self.conteudos_layout.add_widget(
                texto_label
            )

    # ======================================================
    #                    VOLTAR
    # ======================================================

    def voltar(self, instance):

        self.manager.current = 'guia'

# ==========================================================
#                  TELA CUIDADOS BÁSICOS
# ==========================================================

class CuidadosScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='Cuidados Básicos',
            font_size=40
        )

        texto = Label(
            text='Aqui ficarão as informações sobre '
                 'Cuidados Básicos.'
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        layout.add_widget(titulo)
        layout.add_widget(texto)
        layout.add_widget(botao_voltar)

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'guia'


# ==========================================================
#                   TELA SONO
# ==========================================================

class SonoScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='Sono e Rotina',
            font_size=40
        )

        texto = Label(
            text='Aqui ficarão as informações sobre '
                 'sono e rotina infantil.'
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        layout.add_widget(titulo)
        layout.add_widget(texto)
        layout.add_widget(botao_voltar)

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'guia'


# ==========================================================
#                   TELA SEGURANÇA
# ==========================================================

class SegurancaScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='Segurança',
            font_size=40
        )

        texto = Label(
            text='Aqui ficarão as informações sobre '
                 'segurança infantil.'
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        layout.add_widget(titulo)
        layout.add_widget(texto)
        layout.add_widget(botao_voltar)

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'guia'


# ==========================================================
#                TELA DESENVOLVIMENTO INFANTIL
# ==========================================================

class DesenvolvimentoScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='Desenvolvimento Infantil',
            font_size=40
        )

        texto = Label(
            text='Aqui ficarão as informações sobre '
                 'desenvolvimento infantil.'
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        layout.add_widget(titulo)
        layout.add_widget(texto)
        layout.add_widget(botao_voltar)

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'guia'


# ==========================================================
#               TELA BRINCAR E ESTIMULAR
# ==========================================================

class BrincarScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='Brincar\n'
                 'e\n'
                 'Estimular',
            font_size=40
        )

        texto = Label(
            text='Brincadeiras e estímulos',
            font_size=30
        )

        texto2 = Label(
            text='Aqui encontrará opções\n'
                 'para se aproximar e estimular o crescimento!'
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        layout.add_widget(titulo)
        layout.add_widget(texto)
        layout.add_widget(texto2)
        layout.add_widget(botao_voltar)

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'guia'


# ==========================================================
#                  TELA PROFISSIONAIS
# ==========================================================

class ProfissionaisScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='Profissionais Responsáveis',
            font_size=40
        )

        texto = Label(
            text='Informações sobre profissionais responsáveis.'
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        layout.add_widget(titulo)
        layout.add_widget(texto)
        layout.add_widget(botao_voltar)

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'home'


# ==========================================================
#                       TELA CURSOS
# ==========================================================

class CursosScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='Cursos Disponíveis',
            font_size=40
        )

        texto = Label(
            text='Aqui serão disponibilizados cursos importantes.'
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        layout.add_widget(titulo)
        layout.add_widget(texto)
        layout.add_widget(botao_voltar)

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):
        self.manager.current = 'home'

# ==========================================================
#                TELA GERENCIAR CONTEÚDOS
# ==========================================================

class GerenciarConteudosScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=15,
            padding=30
        )

        titulo = Label(
            text='Gerenciar Conteúdos',
            font_size=35,
            size_hint_y=None,
            height=60
        )

        texto_explicativo = Label(
            text='Adicione novos conteúdos ao Guia de Cuidados.',
            font_size=16,
            size_hint_y=None,
            height=50
        )

        categoria = Spinner(
            text='Selecione uma categoria',
            values=(
                'Alimentação',
                'Cuidados Básicos',
                'Sono e Rotina',
                'Segurança',
                'Desenvolvimento Infantil',
                'Brincar e Estimular'
            ),
            size_hint_y=None,
            height=50
        )

        titulo_input = TextInput(
            hint_text='Digite o título do conteúdo',
            multiline=False,
            size_hint_y=None,
            height=50
        )

        texto_input = TextInput(
            hint_text='Digite o conteúdo aqui...',
            multiline=True
        )

        botao_salvar = Button(
            text='Salvar Conteúdo',
            size_hint_y=None,
            height=55
        )

        mensagem = Label(
            text='',
            size_hint_y=None,
            height=40
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=50
        )

        layout.add_widget(titulo)
        layout.add_widget(texto_explicativo)
        layout.add_widget(categoria)
        layout.add_widget(titulo_input)
        layout.add_widget(texto_input)
        layout.add_widget(botao_salvar)
        layout.add_widget(mensagem)
        layout.add_widget(botao_voltar)

        botao_salvar.bind(
            on_press=lambda instance: self.salvar_conteudo(
                categoria,
                titulo_input,
                texto_input,
                mensagem
            )
        )

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def salvar_conteudo(
        self,
        categoria,
        titulo_input,
        texto_input,
        mensagem
    ):

        categoria_escolhida = categoria.text
        titulo = titulo_input.text.strip()
        texto = texto_input.text.strip()

        if categoria_escolhida == 'Selecione uma categoria':
            mensagem.text = 'Selecione uma categoria.'
            return

        if titulo == '':
            mensagem.text = 'Digite um título.'
            return

        if texto == '':
            mensagem.text = 'Digite o conteúdo.'
            return

        data = datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S'
        )

        conexao = sqlite3.connect('cuidare.db')

        cursor = conexao.cursor()

        cursor.execute(
            '''
            INSERT INTO conteudos
            (categoria, titulo, texto, data_criacao)
            VALUES (?, ?, ?, ?)
            ''',
            (
                categoria_escolhida,
                titulo,
                texto,
                data
            )
        )

        conexao.commit()

        conexao.close()

        mensagem.text = 'Conteúdo salvo com sucesso!'

        titulo_input.text = ''
        texto_input.text = ''
        categoria.text = 'Selecione uma categoria'

    def voltar(self, instance):

        self.manager.current = 'home'



# ==========================================================
#                    APLICATIVO
# ==========================================================




class CuidareApp(App):

    def build(self):

        gerenciador = ScreenManager()

        # ----------------------------------------------------
        # Tela inicial
        # ----------------------------------------------------

        gerenciador.add_widget(
            HomeScreen(name='home')
        )

        # ----------------------------------------------------
        # S.O.S
        # ----------------------------------------------------

        gerenciador.add_widget(
            SosScreen(name='sos')
        )

        # ----------------------------------------------------
        # Guia
        # ----------------------------------------------------

        gerenciador.add_widget(
            GuiaScreen(name='guia')
        )

        # ----------------------------------------------------
        # Alimentação
        # ----------------------------------------------------

        gerenciador.add_widget(
            AlimentacaoScreen(name='alimentacao')
        )

        # ----------------------------------------------------
        # Cuidados Básicos
        # ----------------------------------------------------

        gerenciador.add_widget(
            CuidadosScreen(name='cuidados')
        )

        # ----------------------------------------------------
        # Sono
        # ----------------------------------------------------

        gerenciador.add_widget(
            SonoScreen(name='sono')
        )

        # ----------------------------------------------------
        # Segurança
        # ----------------------------------------------------

        gerenciador.add_widget(
            SegurancaScreen(name='seguranca')
        )

        # ----------------------------------------------------
        # Desenvolvimento Infantil
        # ----------------------------------------------------

        gerenciador.add_widget(
            DesenvolvimentoScreen(name='desenvolvimento')
        )

        # ----------------------------------------------------
        # Brincar e Estimular
        # ----------------------------------------------------

        gerenciador.add_widget(
            BrincarScreen(name='brincar')
        )

        # ----------------------------------------------------
        # Profissionais
        # ----------------------------------------------------

        gerenciador.add_widget(
            ProfissionaisScreen(name='profissionais')
        )

        # ----------------------------------------------------
        # Cursos
        # ----------------------------------------------------

        gerenciador.add_widget(
            CursosScreen(name='cursos')
        )

        #NOVA TELA  
        gerenciador.add_widget(
            GerenciarConteudosScreen(name='gerenciar')
        )

        return gerenciador


# ==========================================================
#                    EXECUTAR APLICATIVO
# ==========================================================

criar_banco()

CuidareApp().run()