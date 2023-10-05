from Documentos import Documento
from Telefones import Telefone
from Emails import Email
from Datas import Data
from CEP import CEP

objeto_cpf = Documento.criar_documento(55032243450)
objeto_cnpj = Documento.criar_documento(79694395000120)
objeto_telefone = Telefone(5521981831028)
objeto_email = Email("victorgomes49@yahoo.com.br")
objeto_data = Data()
objeto_cep = CEP("01001000")
objeto_endereco = objeto_cep.formatar_endereco()

print("=" * 50)

print(f"CPF: {objeto_cpf}")

print("=" * 50)

print(f"CNPJ: {objeto_cnpj}")

print("=" * 50)

print(f"Telefone: {objeto_telefone}")

print("=" * 50)

print(f"E-mail: {objeto_email}")

print("=" * 50)

print(f"Data: {objeto_data}")

print("=" * 50)

print("Endereço")
print(f"CEP: {objeto_cep}", end="\n")
print(objeto_endereco)

print("=" * 50)
