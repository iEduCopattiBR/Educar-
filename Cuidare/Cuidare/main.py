from kivy.app import App

from kivy.uix.screenmanager import Screen, ScreenManager

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


# ==========================================================
#                    TELA INICIAL
# ==========================================================

class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # --------------------------------------------------
        # Layout principal
        # --------------------------------------------------

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=45
        )

        # --------------------------------------------------
        # Título
        # --------------------------------------------------

        titulo = Label(
            text='Cuidarê',
            font_size=62,
            size_hint_y=None,
            height=80
        )

        # --------------------------------------------------
        # Subtítulo
        # --------------------------------------------------

        subtitulo = Label(
            text='Cuidar é responsabilidade.\n'
                 'Conhecer é parte dela.',
            font_size=16,
            size_hint_y=None,
            height=50
        )

        # --------------------------------------------------
        # Descrição
        # --------------------------------------------------

        descricao = Label(
            text='Cuidarê reúne informações práticas e conteúdos\n'
                 'elaborados com profissionais para ajudar quem cuida\n'
                 'de crianças e oferecer um cuidado mais seguro e consciente.',
            font_size=16,
            size_hint_y=None,
            height=100
        )

        # --------------------------------------------------
        # Frase final
        # --------------------------------------------------

        frase = Label(
            text='Conhecimento para quem cuida!',
            font_size=16,
            size_hint_y=None,
            height=40
        )

        # ==================================================
        #                    BOTÕES
        # ==================================================

        botao_sos = Button(
            text='S.O.S',
            font_size=18,
            size_hint_x=0.7,
            size_hint_y=None,
            height=60,
            pos_hint={'center_x': 0.5}
        )

        botao_guia = Button(
            text='Guia de Cuidados',
            font_size=18,
            size_hint_x=0.7,
            size_hint_y=None,
            height=60,
            pos_hint={'center_x': 0.5}
        )

        botao_cursos = Button(
            text='Cursos',
            font_size=18,
            size_hint_x=0.7,
            size_hint_y=None,
            height=60,
            pos_hint={'center_x': 0.5}
        )

        botao_profissionais = Button(
            text='Profissionais',
            font_size=18,
            size_hint_x=0.7,
            size_hint_y=None,
            height=60,
            pos_hint={'center_x': 0.5}
        )

        # ==================================================
        #                 CORES DOS BOTÕES
        # ==================================================

        botao_sos.background_color = (1, 0, 0, 1)

        botao_guia.background_color = (0, 0, 1, 1)

        botao_cursos.background_color = (0, 1, 0, 1)

        botao_profissionais.background_color = (0, 0, 1, 1)

        # ==================================================
        #              ADICIONANDO NA TELA
        # ==================================================

        layout.add_widget(titulo)
        layout.add_widget(subtitulo)
        layout.add_widget(descricao)
        layout.add_widget(frase)

        layout.add_widget(botao_sos)
        layout.add_widget(botao_guia)
        layout.add_widget(botao_cursos)
        layout.add_widget(botao_profissionais)

        # ==================================================
        #              FUNÇÕES DOS BOTÕES
        # ==================================================

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

        # --------------------------------------------------
        # Adiciona o layout à tela
        # --------------------------------------------------

        self.add_widget(layout)

    # ======================================================
    #                ABRIR TELA S.O.S
    # ======================================================

    def abrir_sos(self, instance):

        self.manager.current = 'sos'

    # ======================================================
    #              ABRIR TELA GUIA
    # ======================================================

    def abrir_guia(self, instance):

        self.manager.current = 'guia'

    # ======================================================
    #             ABRIR TELA CURSOS
    # ======================================================

    def abrir_cursos(self, instance):

        self.manager.current = 'cursos'

    # ======================================================
    #          ABRIR TELA PROFISSIONAIS
    # ======================================================

    def abrir_profissionais(self, instance):

        self.manager.current = 'profissionais'


# ==========================================================
#                     TELA S.O.S
# ==========================================================

class SosScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        # --------------------------------------------------
        # Título
        # --------------------------------------------------

        titulo = Label(
            text='S.O.S',
            font_size=40,
            size_hint_y=None,
            height=60
        )

        titulo.color = (1, 0, 0, 1)

        # --------------------------------------------------
        # Subtítulo
        # --------------------------------------------------

        subtitulo = Label(
            text='Contatos de emergência\nLigue apenas quando necessário!',
            font_size=18,
            
        )

        # --------------------------------------------------
        # Botões
        # --------------------------------------------------

        botao_192 = Button(
            text='192 - SAMU',
            font_size=16
        )

        botao_193 = Button(
            text='193 - Bombeiros',
            font_size=16
        )

        botao_190 = Button(
            text='190 - Polícia',
            font_size=16
        )

        botao_intoxicacao = Button(
            text='0800-722-6001\nDisque-Intoxicação',
            font_size=16
        )

        # --------------------------------------------------
        # Botão voltar
        # --------------------------------------------------

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=50
        )

        # --------------------------------------------------
        # Cores
        # --------------------------------------------------

        botao_192.background_color = (0, 1, 0, 1)

        botao_193.background_color = (0, 0, 1, 1)

        botao_190.background_color = (1, 0, 0, 1)

        botao_intoxicacao.background_color = (1, 1, 0, 1)

        # --------------------------------------------------
        # Adicionando widgets
        # --------------------------------------------------

        layout.add_widget(titulo)
        layout.add_widget(subtitulo)

        layout.add_widget(botao_192)
        layout.add_widget(botao_193)
        layout.add_widget(botao_190)
        layout.add_widget(botao_intoxicacao)

        layout.add_widget(botao_voltar)

        # --------------------------------------------------
        # Função voltar
        # --------------------------------------------------

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

        layout = BoxLayout(
            orientation='vertical',
            spacing=15,
            padding=40
        )

        # --------------------------------------------------
        # Título
        # --------------------------------------------------

        titulo = Label(
            text='Guia de Cuidados',
            font_size=40,
            size_hint_y=None,
            height=70
        )

        # --------------------------------------------------
        # Texto
        # --------------------------------------------------

        texto = Label(
            text='Informações importantes para quem cuida.',
            font_size=18,
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=60

        )

        # --------------------------------------------------
        # Categorias
        # --------------------------------------------------

        botao_alimentacao = Button(
            text='Alimentação',
            size_hint_y=None,
            height=55
        )

        botao_cuidados = Button(
            text='Cuidados Básicos',
            size_hint_y=None,
            height=55
        )

        botao_sono = Button(
            text='Sono e Rotina',
            size_hint_y=None,
            height=55
        )

        botao_seguranca = Button(
            text='Segurança',
            size_hint_y=None,
            height=55
        )

        botao_desenvolvimento = Button(
            text='Desenvolvimento Infantil',
            size_hint_y=None,
            height=55
        )

        botao_brincar = Button(
            text='Brincar e Estimular',
            size_hint_y=None,
            height=55
        )

        # --------------------------------------------------
        # Voltar
        # --------------------------------------------------

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=50
        )

        # --------------------------------------------------
        # Adicionando widgets
        # --------------------------------------------------

        layout.add_widget(titulo)
        layout.add_widget(texto)

        layout.add_widget(botao_alimentacao)
        layout.add_widget(botao_cuidados)
        layout.add_widget(botao_sono)
        layout.add_widget(botao_seguranca)
        layout.add_widget(botao_desenvolvimento)
        layout.add_widget(botao_brincar)

        layout.add_widget(botao_voltar)

        # --------------------------------------------------
        # Função voltar
        # --------------------------------------------------

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):

        self.manager.current = 'home'


# ==========================================================
#                    TELA DE CURSOS
# ==========================================================

class CursosScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        # --------------------------------------------------
        # Título
        # --------------------------------------------------

        titulo = Label(
            text='Cursos Disponíveis',
            font_size=40,
            size_hint_y=None,
            height=70
        )

        # --------------------------------------------------
        # Texto
        # --------------------------------------------------

        texto = Label(
            text=(
                'Aqui serão disponibilizados cursos importantes\n'
                'para quem trabalha com crianças.'
            ),
            font_size=18,
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=80
        )

        # --------------------------------------------------
        # Botão voltar
        # --------------------------------------------------

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        # --------------------------------------------------
        # Adicionando widgets
        # --------------------------------------------------

        layout.add_widget(titulo)
        layout.add_widget(texto)
        layout.add_widget(botao_voltar)

        # --------------------------------------------------
        # Função voltar
        # --------------------------------------------------

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):

        self.manager.current = 'home'


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

        # --------------------------------------------------
        # Título
        # --------------------------------------------------

        titulo = Label(
            text='Profissionais Responsáveis',
            font_size=40,
            size_hint_y=None,
            height=70
        )

        # --------------------------------------------------
        # Texto
        # --------------------------------------------------

        texto = Label(
            text=(
                'Aqui serão apresentados os profissionais\n'
                'responsáveis pelos conteúdos do Cuidarê.'
            ),
            font_size=18,
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=80
        )

        # --------------------------------------------------
        # Botão voltar
        # --------------------------------------------------

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        # --------------------------------------------------
        # Adicionando widgets
        # --------------------------------------------------

        layout.add_widget(titulo)
        layout.add_widget(texto)
        layout.add_widget(botao_voltar)

        # --------------------------------------------------
        # Função voltar
        # --------------------------------------------------

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):

        self.manager.current = 'home'


# ==========================================================
#                   APLICATIVO
# ==========================================================

class CuidareApp(App):

    def build(self):

        # --------------------------------------------------
        # Cria o gerenciador de telas
        # --------------------------------------------------

        gerenciador = ScreenManager()

        # --------------------------------------------------
        # Adiciona as telas
        # --------------------------------------------------

        gerenciador.add_widget(
            HomeScreen(name='home')
        )

        gerenciador.add_widget(
            SosScreen(name='sos')
        )

        gerenciador.add_widget(
            GuiaScreen(name='guia')
        )

        gerenciador.add_widget(
            CursosScreen(name='cursos')
        )

        gerenciador.add_widget(
            ProfissionaisScreen(name='profissionais')
        )

        # --------------------------------------------------
        # Define a tela inicial
        # --------------------------------------------------

        gerenciador.current = 'home'

        return gerenciador


# ==========================================================
#                INICIAR O APLICATIVO
# ==========================================================

CuidareApp().run()