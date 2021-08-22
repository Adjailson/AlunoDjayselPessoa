class Identidade:

    escolhaMenu = ""
    num1 = 2
    num2 = 3
    
    def opIdentidade(self,escolhaMenu):
        self.escolhaMenu = escolhaMenu
        print("---------------------------------------------------------------------------------------------------")

        print("\nEscolha abaixo qual Operador de identidade você deseja aprender:\n","\n1 - É [is]\n2 - Não é [is not]\n3 - Voltar\n")
        self.escolhaMenu = str(input("Escolha uma opção: "))

        try:
            if self.escolhaMenu == "1":
                print("\nO operador de Identidade [is] a primeira vista pode parecer funcionar igual ao operador de comparação [==].\nEntretanto, enquanto [==] compara valores o operador de identidade compara se apontam para o mesmo objeto na memória.")
                print("Em suma, o operador de identidade [is] não deve ser usado para substituir o operador de comparação [==] em nenhuma circunstância. Ex.:\n")
                print("numero1 = 2", id(self.num1), "\nnumero2 = 3", id(self.num2))
                print("Acima você está vendo que numero1 contém o valor 2, entretanto o seu identificador na memória é outro valor. O mesmo para o número 2.")
                self.opIdentidade(self.escolhaMenu)
            elif self.escolhaMenu == "2":
                print("\nO operador de Identidade [is not] também pode parecer funcionar igual ao operador de comparação [!=].\nEntretanto [!=] verifica se os valores são diferentes enquanto o operador de identidade compara se esses valores não apontam para o mesmo objeto na memória.")
                print("Em suma, o operador de identidade [is not] não deve ser usado para substituir o operador de comparação [!=] em nenhuma circunstância. Ex.:\n")
                print("numero1 = 2", id(self.num1), "\nnumero2 = 3", id(self.num2))
                print("Acima você está vendo que numero1 contém o valor 2, entretanto o seu identificador na memória é outro valor. O mesmo para o número 2.")
                self.opIdentidade(self.escolhaMenu)
            elif self.escolhaMenu == "3":
                print("\nSempre pergunte, não aceite a dúvida!\n")
                return ""
            else:
                raise ValueError("\nInformação incorreta!")

        except ValueError as e:
            print("\nopção inexistente -", e)

objId = Identidade()
