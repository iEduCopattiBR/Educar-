from kivy.app import App

from kivy.uix.behaviors import button
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

#==========================
#=======Tela inicial=======
#==========================

class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #-------------------
        #visual tela inicial
        #-------------------
        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='Cuidarê',
            font_size=62
        )

        subtitulo = Label(
            text='Cuidar é responsabilidade. Conhecer é parte dela',
            font_size=16
        )

        subtitulo2 = Label(
            text =' Cuidarê reúne informações práticas e conteúdos elaborados com profissionais para ajudar quem cuida de crianças e oferecer um cuidado mais seguro e consciente',
            font_size=16,
            size_hint_x=0.7,
            size_hint_y=None,
            height=60,
            pos_hint={'center_x': 0.5}
            )

        subtitulo3 = Label(
            text='Conhecimento para quem cuida!',
            font_size=16
        )

        botao_sos = Button(
            text='S.O.S',
            size_hint_x=0.7,
            size_hint_y=None,
            height=60,
            pos_hint={'center_x': 0.5}
            )

        botao_guia = Button(
            text='Guia de Cuidados',
            size_hint_x=0.7,
            size_hint_y=None,
            height=60,
            pos_hint={'center_x': 0.5}
            )

        botao_cursos = Button(
            text='Cursos',
            size_hint_x=0.7,
            size_hint_y=None,
            height=60,
            pos_hint={'center_x': 0.5}
            )

        botao_profissionais = Button(
            text='Profissionais',
            size_hint_x=0.7,
            size_hint_y=None,
            height=60,
            pos_hint={'center_x': 0.5}
        )

        #======================
        #====Cor dos Botões====
        #======================

        botao_sos.background_color = (1, 0, 0, 1)

        botao_cursos.background_color = (0, 1, 0, 1)

        botao_profissionais.background_color = (0, 0, 1, 1)

        botao_guia.background_color = (0, 0, 1, 1)

        #==========================
        #===Chamada tela inicial===
        #==========================

        layout.add_widget(titulo)
        layout.add_widget(subtitulo)
        layout.add_widget(subtitulo2)
        layout.add_widget(subtitulo3)
        #layout.add_widget(subtitulo4)
        layout.add_widget(botao_sos)
        layout.add_widget(botao_guia)
        layout.add_widget(botao_cursos)
        layout.add_widget(botao_profissionais)

        #=======================
        #===função dos botoes===
        #=======================
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

        self.add_widget(layout)


        #==========================
        #======função voltar=======
        #==========================

    def abrir_sos(self, instance):

        self.manager.current = 'sos'

    def abrir_cursos(self, instance):

        self.manager.current = 'cursos'

    def abrir_profissionais(self, instance):

        self.manager.current = 'profissionais'

    def abrir_guia(self, instance):

        self.manager.current = 'guia'

        #=========================
        #=======Tela S.O.S========
        #=========================

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
            font_size=40
        )

        subtitulo = Label(
            text='Tela de contatos de emergência',
            font_size=18
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
            text='0800-722-6001 - Disque - introxicação',
            font_size=14
        )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=40
        )

        #==========================
        #===cores botoes S.O.S====
        #==========================

        titulo.color = (1, 0, 0, 1)
        botao_192.background_color = (0, 1, 0, 1)
        botao_193.background_color = (0, 0, 1, 1)
        botao_190.background_color = (1, 0, 0, 1)
        botao_0800_722_6001.background_color = (1, 1, 0, 1)

        #================================
        #===O que é adicionado na tela===
        #================================

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

        #===========================
        #===Tela Guia de Cuidados===
        #===========================

class GuiaScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='Guia do Cuidar',
            font_size=40
        )

        texto = Label(
            text='Aqui estão as informações sobre o guia do cuidar.'
        )

        botao_alimentação = Button(
            text='Alimentação',
            size_hint_y=None,
            height=60
            )

        botao_higiene = Button(
            text='Cuidados Básicos',
            size_hint_y=None,
            height=60
            )

        botao_sono = Button(
            text='Sono e Rotina',
            size_hint_y=None,
            height=60
            )

        botao_seguranca = Button(
            text='Segurança',
            size_hint_y=None,
            height=60
            )

        botao_desenvolvimento = Button(
            text='Desenvolvimento Infantil',
            size_hint_y=None,
            height=60
            )

        botao_brincar = Button(
            text='Brincar e estimular',
            size_hint_y=None,
            height=60
            )

        botao_voltar = Button(
            text='Voltar',
            size_hint_y=None,
            height=60
        )

        layout.add_widget(titulo)
        layout.add_widget(texto)
        layout.add_widget(botao_alimentação)
        layout.add_widget(botao_higiene)
        layout.add_widget(botao_sono)
        layout.add_widget(botao_seguranca)
        layout.add_widget(botao_desenvolvimento)
        layout.add_widget(botao_brincar)
        layout.add_widget(botao_voltar)

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):

        self.manager.current = 'home'

        #========================
        #===Tela Profissionais===
        #========================

class ProfissionaisScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        titulo = Label(
            text='Profissionais Responsaveis',
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

class CursosScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(
            orientation='vertical',
            spacing=20,
            padding=40
        )

        Titulo = Label(
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

        layout.add_widget(Titulo)
        layout.add_widget(texto)
        layout.add_widget(botao_voltar)

        botao_voltar.bind(
            on_press=self.voltar
        )

        self.add_widget(layout)

    def voltar(self, instance):

        self.manager.current = 'home'

        #=========================
        #=======Aplicativo========
        #=========================
class CuidareApp(App):

    def build(self):

        gerenciador = ScreenManager()

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
            ProfissionaisScreen(name='profissionais')
        )

        gerenciador.add_widget(
            CursosScreen(name='cursos')
        )

        return gerenciador


CuidareApp().run()