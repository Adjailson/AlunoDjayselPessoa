class Comparacao:

    escolhaMenu = str
    resposta = str
    
    def opComparacao(self,escolhaMenu):
        self.escolhaMenu = escolhaMenu

        print("---------------------------------------------------------------------------------------------------")

        print("\nEscolha abaixo qual Operador de Comparação você deseja aprender:\n","\n1 - Igual [==]\n2 - Diferente [!=]\n3 - Maior que [>]\n4 - Menor que [<]\n5 - Maior ou igual [>=]\n6 - Menor ou igual [<=]\n7 - Voltar\n")
        self.escolhaMenu = str(input("Escolha uma opção: "))

        try:
            if self.escolhaMenu == "1":
                print("\nCom o operador Igual [==] podemos verificar se os valores de dois operandos são iguais. Se sim a condição se torna verdadeira.")
                print("numero1 = 2 -> numero2 = 3")
                print("If numero1 == numero2:")
                print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                self.resposta = str(input("S para sim, N para não: "))
                
                if self.resposta == 'S' or self.resposta == 's':
                    print("\nResposta incorreta! Os dois valores são diferentes!")
                    self.opComparacao(self.escolhaMenu)
                elif self.resposta == 'N' or self.resposta == 'n':
                    print("\nResposta correta! Os valores são diferentes!")
                    self.opComparacao(self.escolhaMenu)
                else:
                    print("\nCaractere inválido! REINICIANDO!")
                    self.opComparacao(self.escolhaMenu)
            elif self.escolhaMenu == "2":
                print("\nCom o operador Diferente [!=] podemos verificar se os valores de dois operandos são distintos. Se sim a condição se torna verdadeira.\n")
                print("numero1 = 5 -> numero2 = 3")
                print("If numero1 != numero2:")
                print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                self.resposta = str(input("S para sim, N para não: "))
                if self.resposta == 'S' or self.resposta == 's':
                    print("\nResposta correta! Os valores são diferentes!")
                    self.opComparacao(self.escolhaMenu)
                elif self.resposta == 'N' or self.resposta == 'n':
                    print("\nResposta incorreta! Os dois valores são diferentes!")
                    self.opComparacao(self.escolhaMenu)
                else:
                    print("\nCaractere inválido! REINICIANDO!")
                    self.opComparacao(self.escolhaMenu)
            elif self.escolhaMenu == "3":
                print("\nCom o operador Maior que [>] podemos verificar se o valor de um operando é maior que de outro operando. Se sim a condição se torna verdadeira.\n")
                print("numero1 = 5 -> numero2 = 3")
                print("If numero1 > numero2:")
                print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                self.resposta = str(input("S para sim, N para não: "))
                if self.resposta == 'S' or self.resposta == 's':
                    print("\nResposta correta! numero1 é maior que numero2")
                    self.opComparacao(self.escolhaMenu)
                elif resposta == 'N' or resposta == 'n':
                    print("\nResposta incorreta! numero1 é maior que numero2")
                    self.opComparacao(self.escolhaMenu)
                else:
                    print("\nCaractere inválido! REINICIANDO!")
                    self.opComparacao(self.escolhaMenu)
            elif self.escolhaMenu == "4":
                print("\nCom o operador Menor que [<] podemos verificar se o valor de um operando é menor que de outro operando. Se sim a condição se torna verdadeira.\n")
                print("numero1 = 3 -> numero2 = 3")
                print("If numero1 < numero2:")
                print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                self.resposta = str(input("S para sim, N para não: "))
                if self.resposta == 'S' or self.resposta == 's':
                    print("\nResposta incorreta! numero1 é igual numero2")
                    self.opComparacao(self.escolhaMenu)
                elif self.resposta == 'N' or self.resposta == 'n':
                    print("\nResposta correta! numero1 não é menor que o numero2, eles são iguais.")
                    self.opComparacao(self.escolhaMenu)
                else:
                    print("\nCaractere inválido! REINICIANDO!")
                    self.opComparacao(self.escolhaMenu)
            elif self.escolhaMenu == "5":
                print("\nCom o operador Maior ou igual [>=] podemos verificar se o valor de um operando é maior que de outro operando ou também se é igual. Se sim a condição se torna verdadeira.\n")
                print("numero1 = 3 -> numero2 = 3")
                print("If numero1 >= numero2:")
                print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                self.resposta = str(input("S para sim, N para não: "))
                if self.resposta == 'S' or self.resposta == 's':
                    print("\nResposta correta! numero1 não é maior mas é igual ao numero2")
                    self.opComparacao(self.escolhaMenu)
                elif self.resposta == 'N' or self.resposta == 'n':
                    print("\nResposta incorreta! numero1 é igual numero2, só não é maior.")
                    self.opComparacao(self.escolhaMenu)
                else:
                    print("\nCaractere inválido! REINICIANDO!")
                    self.opComparacao(self.escolhaMenu)
            elif self.escolhaMenu == "6":
                print("\nCom o operador Menor ou igual [<=] podemos verificar se o valor de um operando é menor que de outro operando ou se é igual. Se sim a condição se torna verdadeira.\n")
                print("numero1 = 3 -> numero2 = 3")
                print("If numero1 <= numero2:")
                print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                self.resposta = str(input("S para sim, N para não: "))
                if self.resposta == 'S' or self.resposta == 's':
                    print("\nResposta correta! numero1 não é menor mas é igual ao numero2")
                    self.opComparacao(self.escolhaMenu)
                elif self.resposta == 'N' or self.resposta == 'n':
                    print("\nResposta incorreta! numero1 é igual numero2, só não é menor.")
                    self.opComparacao(self.escolhaMenu)
                else:
                    print("\nCaractere inválido! REINICIANDO!")
                    self.opComparacao(self.escolhaMenu)
            elif self.escolhaMenu == "7":
                print("\nSempre procure soluções, se não encontrar procure mais!\n")
                return ""
            else:
                raise ValueError("\nInformação incorreta!")

        except ValueError as e:
            print("\nopção inexistente -", e)

objCom = Comparacao()
