from pacoteEscolha.Browser import objBrowser

class Programa:

    texto = str
    
    def sobrePrograma(self):
        try:
            #Pode ser assim também em vez de varios print
            self.texto = ""
            self.texto += "--------------------------------------------------"
            self.texto +="\nOlá!\n"
            self.texto +="\nEspero que tenha gostado deste aplicativo PYTHON FOR NOOBS!\nEsta primeira versão é bem básica e utiliza somente o terminal para acesso.\n"
            self.texto +="Futuramente outras funcionalidades e provavelmente outra cara será dada à esse pequeno projeto.\nO objetivo deste programa é servir de consulta, mas de nenhum modo deve ser utilizado sozinho.\n"
            self.texto +="Sendo assim abaixo disponibilizo os links das fontes de onde essas informações sairam.\nPerceba também que com a evolução da linguagem algumas coisas podem deixar de funcionar como exposto aqui.\n"
            self.texto +="De todo modo agradeço sua paciência e espero que tenha gostado!\n"
            self.texto +="\nDjayselPessôa - programador/idealizador\n"
            print(self.texto)

            print("---------------------------------------------------------------------------------------------------")
            print("\nhttps://stackoverflow.com/questions/22125114/how-to-insert-links-in-python\n")
            print("https://isolution.pro/pt/t/python/membership-operators-example/exemplo-de-operadores-de-associacao-python\n") 
            print("https://realpython.com/python-is-identity-vs-equality/\n")
            print("https://acervolima.com/python-3-operadores-logicos/\n")
            print("http://excript.com/python/operador-de-atribuicao-python.html\n")
            print("http://cristiancechinel.pro.br/my_files/algorithms/bookhtml/node39.html\n")
            print("https://isolution.pro/pt/t/python3/python-basic-operators/python-3-operadores-basicos\n")
            print("https://www.devmedia.com.br/operadores-no-python/40693\n")
            print("---------------------------------------------------------------------------------------------------\n")

            escolha = str(input("Para abrir todas as páginas acima no browser digite S. Para Voltar digite V:  "))

            if escolha == "S" or escolha == "s":
                objBrowser.abrirBrowser()
            elif escolha == "V" or escolha == "v":
                return None
            else:
                raise ValueError("Erro!")
        except ValueError as e:
            print("Dado informado incorreto!", e)

objInfor = Programa()
