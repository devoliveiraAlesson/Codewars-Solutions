def points(games):
    resultado = 0
    for game in games:
        teste = int(game[0]) - int(game[-1])
        resultado += [0,1,3][(teste > 0)+(teste >= 0)]
    return resultado