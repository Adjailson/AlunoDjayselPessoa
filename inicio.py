from pacoteDef.Escolha import obj

print("\n----PYTHON FOR NOOBS----\n")

while True:
    try:
        print("\n-----------------------------------------------------------------------------PFN-------DjPESSÔA----")

        print("\nAbaixo estão todos os tipos de operadores:\n","\n1 - Operadores Aritméticos\n2 - Operadores de Atribuição\n3 - Operadores de Comparação\n4 - Operadores Lógicos\n5 - Operadores de Identidade\n6 - Operadores de Associação\n7 - Sobre o programa\n8 - Sair\n","\n")
        escolhaOp = str(input("Escolha qual destes tipos de operadores você deseja estudar: "))
        if (escolhaOp == '8') or (escolhaOp == 'sair'):
            print("Finalizado!")
            break
        else:
            obj.escolha(escolhaOp)

    except ValueError as e:
        print("Erro", e)
