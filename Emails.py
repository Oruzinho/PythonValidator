import re


class Email:
    def __init__(self, email):
        if self.validar_email(email):
            self._email = email
        else:
            raise ValueError("Email inválido")

    def __str__(self):
        return self._email

    def validar_email(self, email):
        padrao = "\w{5,64}@[a-z]{3,10}.com.br"
        resposta = re.findall(padrao, email)

        if resposta:
            return True
        else:
            return False
