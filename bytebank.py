from cpf_cnpj import Documento
from validate_docbr import CPF, CNPJ

#cpf_um = Cpf("15316264754")
#print(cpf_um)

#cnpj = CNPJ()
#print(cnpj.validate(exemplo_cnpj))

#exemplo_cnpj = "35379838000112"
exemplo_cpf = "15316264754"
documento = Documento.cria_documento(exemplo_cpf) 

print(documento)