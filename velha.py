# coding=utf-8
jogar = True
while jogar:
    continuar = int(input("Digite 1 pra jogar e 2 pra sair:"))
    if continuar == 1:
        jogar = True
    if continuar == 2:
        break
    print("-=-"*10)
    print("BEM VINDO AO JOGO DA VELHA")
    print("-=-"*10)



    velha="""              Posições
   |   |      7 | 8 | 9
---+---+---  ---+---+---
   |   |      4 | 5 | 6
---+---+---  ---+---+---
   |   |      1 | 2 | 3
    """

    posicoes = [
           None,
          (5, 1),
          (5, 5),
          (5, 9),
          (3, 1),
          (3, 5),
          (3, 9),
          (1, 1),
          (1, 5),
          (1, 9),
        ]

    ganho = [
              [ 1, 2, 3], # Linhas
              [ 4, 5, 6],
              [ 7, 8, 9],
              [ 7, 4, 1], # Colunas
              [ 8, 5, 2],
              [ 9, 6, 3],
              [ 7, 5, 3], # Diagonais
              [ 1, 5, 9]
            ]

    tabuleiro = []
    for linha in velha.splitlines():
        tabuleiro.append(list(linha))
    jogador = "X" # Começa jogando com X
    jogando = True
    jogadas = 0

    # Contador de jogadas
    while True:
        for t in tabuleiro:
            print("".join(t))
        if not jogando:
            break
        if jogadas == 9:
            print("Deu velha! Ninguém ganhou.")
            break
        jogada = int(input("Digite a posição a jogar 1-9 (jogador %s):" % jogador))
        if jogada < 1 or jogada > 9:
            print("Posição inválida")
            continue
        if tabuleiro[posicoes[jogada][0]][posicoes[jogada][1]] != " ":
            print("Posição ocupada.")
            continue
        tabuleiro[posicoes[jogada][0]][posicoes[jogada][1]] = jogador
        # Verficar vencedor:
        for p in ganho:
            for x in p:
                if tabuleiro[posicoes[x][0]][posicoes[x][1]] != jogador:
                    break
            else:
                print("\nO jogador %s ganhou (%s): "%(jogador, p))
                jogando = False
                break
        jogador = "X" if jogador == "O" else "O"
