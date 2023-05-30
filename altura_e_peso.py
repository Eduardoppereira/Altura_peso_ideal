def calcular_peso_ideal():
    altura = float(input("Informe sua altura em metros: "))
    genero = input("Informe seu gênero (M para masculino, F para feminino): ")
    
    if genero.upper() == 'M':
        peso_ideal = (72.7 * altura) - 58
    elif genero.upper() == 'F':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Gênero inválido. Por favor, insira M para masculino ou F para feminino.")
        return
    
    print("Seu peso ideal é:", peso_ideal, "kg")


calcular_peso_ideal()
