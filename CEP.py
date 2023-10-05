import requests as rq


class CEP:
    def __init__(self, cep):
        cep = str(cep)
        if self.verificar_cep_valido(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido")

    def __str__(self):
        return self.formatar_cep()

    def verificar_cep_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formatar_cep(self):
        r = rq.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        return r.json()["cep"]

    def consultar_cep(self):
        r = rq.get(f"https://viacep.com.br/ws/{self.cep}/json/")
        r = r.json()
        return r["logradouro"], r["bairro"], r["localidade"], r["uf"]

    def formatar_endereco(self):
        logradouro, bairro, cidade, estado = self.consultar_cep()
        return f"Logradouro: {logradouro} \nBairro: {bairro} \nCidade: {cidade} \nEstado: {estado}"
