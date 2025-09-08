def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    else:
        dicionario = {12:"rock", 13:"scissors", 9:"paper"}
        
        return ["Player 2 won!","Player 1 won!"][p1 == dicionario[len(p1+p2)]]   