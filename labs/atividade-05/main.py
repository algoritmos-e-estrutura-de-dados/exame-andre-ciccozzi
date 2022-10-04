def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
    trocas = 0
    menorFigurinha = figurinhas_da_maria if len(figurinhas_da_maria) <= len(figurinhas_do_joao) else figurinhas_do_joao
    maiorFigurinha = figurinhas_da_maria if len(figurinhas_da_maria) >= len(figurinhas_do_joao) else figurinhas_do_joao

    for index, numeroFigurinha in enumerate(menorFigurinha):
        if not numeroFigurinha in maiorFigurinha:
            for n in range(index, len(maiorFigurinha)):
                if numeroFigurinha != maiorFigurinha[n]:
                    aux = maiorFigurinha[n]
                    maiorFigurinha[n] = numeroFigurinha
                    menorFigurinha[index] = aux
                    trocas = trocas + 1
                    break
    return trocas



if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)
