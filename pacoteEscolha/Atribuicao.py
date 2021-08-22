class Atribuicao:

    escolhaMenu = ""
    num1 = 0
    num2 = 0

    def opAtribuicao(self,escolhaMenu):
        self.escolhaMenu = escolhaMenu
        print("---------------------------------------------------------------------------------------------------")

        print("\nOperadores de Atrubuição:\n","\n1 - Atribuição simples [=]\n2 - Incremento [+=]\n3 - Decremento [-=]\n4 - Dividido igual [/=]\n5 - Vezes igual [*=]\n6 - Módulo igual [%=]\n7 - Voltar\n")
        self.escolhaMenu = str(input("Escolha uma opção: "))

        try:
            if self.escolhaMenu == "1":
                print("O operador de atribuição simples faz com que os valores do lado direito do operador sejam atribuido ao que estiver do lado esquerdo, normalmente uma variável.")
                self.num1 = int(input("Informe um número inteiro: "))
                self.num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo = {self.num1} + {self.num2}; variavelExemplo possui ou representa o valor {self.num1 + self.num2}\n")
                self.opAtribuicao(self.escolhaMenu)
            elif self.escolhaMenu == "2":
                print("O operador de incremento faz com que os valores da variável do lado esquerdo seja somada ao valores do lado direito e por fim reatribuído à variável.\n")
                self.num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                self.num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo += {self.num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo + {self.num2}. A variavelExemplo ao final possuirá o valor {self.num1 + self.num2}")
                self.opAtribuicao(self.escolhaMenu)
            elif self.escolhaMenu == "3":
                print("O operador de decremento faz com que os valores da variável do lado esquerdo seja subtraída pelo valor do lado direito e por fim reatribuído à variável.\n")
                num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo -= {self.num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo - {self.num2}. A variavelExemplo ao final possuirá o valor {self.num1 - self.num2}")
                self.opAtribuicao(self.escolhaMenu)
            elif self.escolhaMenu == "4":
                print("O operador dividido igual faz com que os valores da variável do lado esquerdo seja dividido pelo valor do lado direito e por fim reatribuído à variável\n")
                self.num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                self.num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo /= {self.num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo / {self.num2}. A variavelExemplo ao final possuirá o valor {self.num1 / self.num2}")
                self.opAtribuicao(self.escolhaMenu)
            elif self.escolhaMenu == "5":
                print("O operador vezes igual faz com que os valores da variável do lado esquerdo seja multiplicado pelo valor do lado direito e por fim reatribuído à variável\n")
                self.num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                self.num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo *= {self.num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo * {self.num2}. A variavelExemplo ao final possuirá o valor {self.num1 * self.num2}")
                self.opAtribuicao(self.escolhaMenu)
            elif self.escolhaMenu == "6":
                print("O operador módulo igual faz com que os valores da variável do lado esquerdo receba o resto da divisão pelo valor do lado direito e por fim reatribuído à variável\n")
                self.num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                self.num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo %= {self.num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo % {self.num2}. A variavelExemplo ao final possuirá o valor {self.num1 % self.num2}")
                self.opAtribuicao(self.escolhaMenu)
            elif self.escolhaMenu == "7":
                print("\nMelhor forma de aprender é testando!\n")
            else:
                raise ValueError("\nInformação incorreta!")

        except ValueError as e:
            print("\nopção inexistente -", e)

objAtr = Atribuicao()
