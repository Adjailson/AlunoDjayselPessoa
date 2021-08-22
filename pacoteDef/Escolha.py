from pacoteEscolha.Programa import objInfor
from pacoteEscolha.Aritmetico import objArt
from pacoteEscolha.Associacao import objAss
from pacoteEscolha.Atribuicao import objAtr
from pacoteEscolha.Comparacao import objCom
from pacoteEscolha.Identidade import objId
from pacoteEscolha.Logico import objLog

'''
Não precisa o comando 'return' seu método tem que ser do tipo void,
ou seja, ele não retorna nada e sim outras funções ou chamadas.
'''
class Escolha:
    
    escolhaOp = str

    def escolha(self,escolhaOp):
        self.escolhaOp = escolhaOp
        try:
            if self.escolhaOp == "1":
                objArt.opAritimetico(self.escolhaOp)
            elif self.escolhaOp == "2":
                objAtr.opAtribuicao(self.escolhaOp)
            elif self.escolhaOp == "3":
                objCom.opComparacao(self.escolhaOp)
            elif self.escolhaOp == "4":
                objLog.oplogico(self.escolhaOp)
            elif self.escolhaOp == "5":
                objId.opIdentidade(self.escolhaOp)
            elif self.escolhaOp == "6":
                objAss.opAssociacao(self.escolhaOp)
            elif self.escolhaOp == "7":
                objInfor.sobrePrograma()
            else:
                raise ValueError("\nInformação incorreta!")

        except ValueError as e:
            print("\nopção inexistente -", e)

obj = Escolha()
