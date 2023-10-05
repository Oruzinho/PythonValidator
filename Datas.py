from datetime import datetime, timedelta


class Data:
    def __init__(self):
        self.data_cadastro = datetime.today()

    def __str__(self):
        return self.formata_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "",
            "Janeiro",
            "Fevereiro",
            "Março",
            "Abril",
            "Maio",
            "Junho",
            "Julho",
            "Agosto",
            "Setembro",
            "Outubro",
            "Novembro",
            "Dezembro",
        ]
        return meses_do_ano[self.data_cadastro.month]

    def dia_semana_cadastro(self):
        dias_semana = [
            "",
            "Segunda",
            "Terça",
            "Quarta",
            "Quinta",
            "Sexta",
            "Sábado",
            "Domingo",
        ]
        return dias_semana[self.data_cadastro.weekday()]

    def formata_data(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.data_cadastro
        return tempo_cadastro
