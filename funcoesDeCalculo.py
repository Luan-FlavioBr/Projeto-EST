def medianaF(lista):
    tamanho = len(lista)
    if tamanho % 2 == 0:
        metadeInteira = tamanho // 2
        primeiraParte = metadeInteira - 1
        segundaParte = metadeInteira

        mediana = (lista[primeiraParte] + lista[segundaParte]) / 2
        return mediana
    else:
        metadeInteira = tamanho // 2
        primeiraParte = metadeInteira
        mediana = lista[primeiraParte]
        return mediana


def media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media


def moda(lista):
    quantidade = list()
    indexNumeros = list()
    numerosNaoRepetidos = list(set(lista))
    for numerosSet in numerosNaoRepetidos:
        quantidade.append(lista.count(numerosSet)) 
    
    maiorQuantidade = max(quantidade) # Maior número da lista que mostra quantiade de vezes
    indexMaiorQuantidade = quantidade.index(maiorQuantidade)
    quantidadeMaiorNumero = quantidade.count(maiorQuantidade)

    if quantidadeMaiorNumero == 1:
       return numerosNaoRepetidos[indexMaiorQuantidade]
    elif quantidadeMaiorNumero == 2:
        vezes = 0
        for numero in quantidade:
            if numero == maiorQuantidade:
                indexNumeros.append(quantidade.index(numero))
                vezes = quantidade[quantidade.index(numero)]
                quantidade[quantidade.index(numero)] = 0
        return [numerosNaoRepetidos[indexNumeros[0]], numerosNaoRepetidos[indexNumeros[1]]]
    else:
        quantidadeDeNumerosModais = 0;
        for numero in quantidade:
            if numero == maiorQuantidade:
                indexNumeros.append(quantidade.index(numero))
                quantidade[quantidade.index(numero)] = 0
                quantidadeDeNumerosModais += 1

        if quantidadeDeNumerosModais != len(lista):
            modas = list()

            for i, indexNumero in enumerate(indexNumeros):
                if indexNumero == indexNumeros[-1]:
                    modas.append(numerosNaoRepetidos[indexNumeros[i]])
                else:
                    modas.append(numerosNaoRepetidos[indexNumeros[i]])
            print()
            return modas
        else:
            return []


def central(lista):
    mediaS = media(lista)
    mediana = medianaF(lista)
    modaS = moda(lista)
    return mediaS, mediana, modaS
