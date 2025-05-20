def ajustar_dificuldade(estatisticas):
    if estatisticas["fracassos"] > estatisticas["sucessos"]:
        return "fácil"
    elif estatisticas["sucessos"] > 3:
        return "difícil"
    else:
        return "normal"
