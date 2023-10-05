import re


class Telefone:
    def __init__(self, telefone):
        telefone = str(telefone)
        if self.validar_telefone(telefone):
            self._telefone = telefone
        else:
            raise ValueError("Número inválido")

    def __str__(self):
        return self.formatar_telefone()

    def padrao_telefone(self):
        return "([0-9]{2})?([0-9]{2})([9]{0,1})?([0-9]{4})([0-9]{4})"

    def validar_telefone(self, telefone):
        resposta = re.findall(self.padrao_telefone(), telefone)

        if resposta:
            return True
        else:
            return False

    def formatar_telefone(self):
        resposta = re.search(self.padrao_telefone(), self._telefone)
        return f"+{resposta.group(1)}({resposta.group(2)}){resposta.group(3)}{resposta.group(4)}-{resposta.group(5)}"
