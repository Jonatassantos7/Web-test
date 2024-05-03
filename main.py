from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

import re

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='CPF ou Email:'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='Senha:'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label(text='A senha deve conter 6 dígitos'))  # Mensagem adicionada
        self.add_widget(Label())  # placeholder

        self.login_button = Button(text='Login')
        self.login_button.bind(on_press=self.login)
        self.add_widget(self.login_button)

        self.add_widget(Label(text='Ainda não tem uma conta?'))
        self.register_button = Button(text='Cadastrar')
        self.register_button.bind(on_press=self.switch_to_register)
        self.add_widget(self.register_button)

        # Adicionando widgets para exibir mensagens de erro ou confirmação
        self.error_label = Label(text='', color=(1, 0, 0, 1))
        self.add_widget(self.error_label)
        self.success_label = Label(text='', color=(0, 1, 0, 1))
        self.add_widget(self.success_label)

    def login(self, instance):
        cpf_email = self.username.text
        password = self.password.text

        # Verificar se o CPF ou email e a senha atendem aos critérios mínimos
        if self.is_valid_cpf_email(cpf_email) and self.is_valid_password(password):
            self.success_label.text = "Login realizado com sucesso!"
            self.error_label.text = ""
            # Chamar função para abrir nova tela após o login
            self.switch_to_menu()
        else:
            self.error_label.text = "CPF ou email inválido ou senha incorreta."
            self.success_label.text = ""

    def switch_to_register(self, instance):
        self.clear_widgets()
        self.add_widget(RegisterScreen())

    def is_valid_cpf_email(self, cpf_email):
        # Verificar se o CPF ou email estão no formato correto
        cpf_pattern = re.compile(r'^\d{11}$')  # padrão de CPF contendo 11 números
        email_pattern = re.compile(r'^[\w.-]+@[\w.-]+\.\w+$')  # padrão de email
        return bool(cpf_pattern.match(cpf_email) or email_pattern.match(cpf_email))

    def is_valid_password(self, password):
        # Verificar se a senha tem pelo menos 6 caracteres
        return len(password) >= 6

    def switch_to_menu(self):
        self.clear_widgets()
        self.add_widget(MenuScreen())

class RegisterScreen(GridLayout):
    def __init__(self, **kwargs):
        super(RegisterScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='CPF:'))
        self.cpf = TextInput(multiline=False)
        self.add_widget(self.cpf)

        self.add_widget(Label(text='Email:'))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.add_widget(Label(text='Nome:'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='Endereço:'))
        self.address = TextInput(multiline=False)
        self.add_widget(self.address)

        self.add_widget(Label())  # placeholder
        self.register_button = Button(text='Cadastrar')
        self.register_button.bind(on_press=self.register)
        self.add_widget(self.register_button)

        # Botão para voltar à tela de login
        self.back_to_login_button = Button(text='Voltar')
        self.back_to_login_button.bind(on_press=self.switch_to_login)
        self.add_widget(self.back_to_login_button)

        # Adicionando widgets para exibir mensagens de erro ou confirmação
        self.error_label = Label(text='', color=(1, 0, 0, 1))
        self.add_widget(self.error_label)
        self.success_label = Label(text='', color=(0, 1, 0, 1))
        self.add_widget(self.success_label)

    def register(self, instance):
        cpf = self.cpf.text
        email = self.email.text
        name = self.name.text
        address = self.address.text

        # Verificar se os campos atendem aos critérios mínimos
        if self.is_valid_cpf(cpf) and self.is_valid_email(email):
            self.success_label.text = "Novo usuário cadastrado!"
            self.error_label.text = ""
        else:
            self.error_label.text = "CPF ou email inválido."
            self.success_label.text = ""

    def switch_to_login(self, instance):
        self.clear_widgets()
        self.add_widget(LoginScreen())

    def is_valid_cpf(self, cpf):
        # Verificar se o CPF está no formato correto
        cpf_pattern = re.compile(r'^\d{11}$')  # padrão de CPF contendo 11 números
        return bool(cpf_pattern.match(cpf))

    def is_valid_email(self, email):
        # Verificar se o email está no formato correto
        email_pattern = re.compile(r'^[\w.-]+@[\w.-]+\.\w+$')  # padrão de email
        return bool(email_pattern.match(email))


class MenuScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Olá, seja bem-vindo!"))

        ministries_button = Button(text="Ministérios")
        ministries_button.bind(on_press=self.switch_to_ministries)
        self.add_widget(ministries_button)

        # Adicionando os botões do menu
        buttons = [
            "Aniversários do Mês",
            "Agenda",
            "Instagram",
            "Facebook",
            "Youtube",
            "Site da Igreja"
        ]

        for button_text in buttons:
            button = Button(text=button_text)
            self.add_widget(button)

    def switch_to_ministries(self, instance):
        self.clear_widgets()
        self.add_widget(MinistryScreen())

class MinistryScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MinistryScreen, self).__init__(**kwargs)
        self.cols = 1

        ministries = [
            "Infantil",
            "Adolescentes",
            "Casais",
            "Jovens",
            "Mídia",
            "Louvor",
            "Voluntários",
            "Oração"
        ]

        for ministry_name in ministries:
            button = Button(text=ministry_name)
            button.bind(on_press=self.on_ministry_selected)
            self.add_widget(button)

        # Botão para voltar à tela anterior
        self.back_button = Button(text='Voltar')
        self.back_button.bind(on_press=self.switch_to_previous_screen)
        self.add_widget(self.back_button)

    def on_ministry_selected(self, instance):
        ministry_name = instance.text
        # Aqui você pode adicionar lógica para exibir mais informações sobre o ministério selecionado
        print("Selecionado:", ministry_name)

    def switch_to_previous_screen(self, instance):
        self.clear_widgets()
        self.add_widget(MenuScreen())

class MyApp(App):
    def build(self):
        return LoginScreen()

if __name__ == '__main__':
    MyApp().run()

