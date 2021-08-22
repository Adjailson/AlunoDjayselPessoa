class Aritmetico:
    escolhaMenu = str
    num1 = 0
    num2 = 0
    def opAritimetico(self,escolhaMenu):
        self.escolhaMenu = escolhaMenu
        print("---------------------------------------------------------------------------------------------------")

        print("\nOperadores Aritméticos:\n","\n1 - Adição [+]\n2 - Subtração [-]\n3 - Multiplicação [*]\n4 - Divisão [/]\n5 - Divisão Inteira [//]\n6 - Módulo [%]\n7 - Exponenciação [**]\n8 - Voltar\n")
        self.escolhaMenu = str(input("Escolha uma opção: "))

        try:
            if self.escolhaMenu == "1":
                print("A adição junta valores de mesmo tipo. ")
                num1 = int(input("Informe um número inteiro: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"{self.num1} + {self.num2} -> ", num1 + num2)
                print("As operações básicas sem parênteses seguem prioridades específicas durante a execução.\nA prioridade da soma é igual da subtração tendo assim a menor prioridade durante a execução do cálculo.\n")
                self.opAritimetico(escolhaMenu)
            elif self.escolhaMenu == "2":
                print("A subtração retira o valor da direita do valor da esquerda. ")
                num1 = int(input("Informe um número inteiro: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"{self.num1} - {self.num2} -> ", num1 - num2)
                print("A prioridade da subtração é igual a da soma, sendo computado por último.\n")
                self.opAritimetico(escolhaMenu)
            elif self.escolhaMenu == "3":
                print("A multiplicação faz com que o número da esquerda seja somado por ele mesmo.\nA quantidade de vezes que isso ocorre é o número da direita.\n")
                num1 = int(input("Informe um número inteiro: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"{self.num1} * {self.num2} -> ", num1 * num2)
                print("A prioridade da multiplicação é igual a da divisão e maior que a soma e subtração.\n")
                self.opAritimetico(escolhaMenu)
            elif self.escolhaMenu == "4":
                print("A divisão faz com que o número da esquerda seja repartido na quantidade exata do número da direita, gerando, dependendo do caso, casas decimais.\n")
                num1 = int(input("Informe um número inteiro: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"{num1} / {num2} -> ", num1 / num2)
                print("A prioridade da divisão é igual a da multiplicação e portanto maior que a soma e subtração.\n")
                self.opAritimetico(escolhaMenu)
            elif escolhaMenu == "5":
                print("A divisão inteira faz com que o número da esquerda seja repartido na quantidade exata do número da direita, entretanto mesmo que gere casas decimais elas são ignoradas.\n")
                num1 = int(input("Informe um número inteiro: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"{self.num1} // {self.num2} -> ", num1 // num2)
                print("A prioridade da divisão inteira é a mesma da divisão normal.\n")
                self.opAritimetico(escolhaMenu)
            elif self.escolhaMenu == "6":
                print("O operador módulo também divide os valores, entretanto o valor obtido é o valor do resto.\n")
                num1 = int(input("Informe um número inteiro: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"{self.num1} % {self.num2} -> ", num1 % num2)
                print("A prioridade do módulo é a mesma da divisão e multiplicação.\n")
                self.opAritimetico(escolhaMenu)
            elif self.escolhaMenu == "7":
                print("O operador de exponenciação/potenciação multiplica o valor da esquerda por ele mesmo na quantidade de vezes do número da direita.\n")
                num1 = int(input("Informe um número inteiro: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"{self.num1} ** {self.num2} -> ", num1 ** num2)
                print("A prioridade deste operador é maior de todas, desde que não tenha nada dentro de parênteses.\n")
                self.opAritimetico(escolhaMenu)
            elif self.escolhaMenu == "8":
                print("\nlembre-se sempre de colocar espaço antes e depois de qualquer operador!\n")
                return ""
            else:
                raise ValueError("\nInformação incorreta!")

        except ValueError as e:
            print("\nopção inexistente -", e)

objArt = Aritmetico()

