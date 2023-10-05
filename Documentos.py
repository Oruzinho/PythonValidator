from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def criar_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de caracteres está incorreta")


class DocCpf:
    def __init__(self, documento):
        cpf = str(documento)
        if self.validar_cpf(cpf):
            self._cpf = cpf
        else:
            raise ValueError("CPF Inválido")

    def __str__(self):
        return self.formatar_cpf()

    def validar_cpf(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            return ValueError("Quantidade de dígitos inválida")

    def formatar_cpf(self):
        mask = CPF()
        return mask.mask(self._cpf)


class DocCnpj:
    def __init__(self, documento):
        cnpj = str(documento)
        if self.validar_cnpj(cnpj):
            self._cnpj = cnpj
        else:
            raise ValueError("CNPJ Inválido")

    def __str__(self):
        return self.formatar_cnpj()

    def validar_cnpj(self, cnpj):
        if len(cnpj) == 14:
            validador = CNPJ()
            return validador.validate(cnpj)
        else:
            return ValueError("Quantidade de dígitos inválida")

    def formatar_cnpj(self):
        mask = CNPJ()
        return mask.mask(self._cnpj)
