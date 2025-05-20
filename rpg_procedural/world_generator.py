import random

locais = ["vila esquecida", "floresta encantada", "caverna sombria", "ruínas antigas"]
objetivos = ["resgatar o artefato", "investigar o desaparecimento", "destruir o selo maligno"]
obstaculos = ["um dragão adormecido", "armadilhas mágicas", "um culto oculto"]

def gerar_missao():
    local = random.choice(locais)
    objetivo = random.choice(objetivos)
    obstaculo = random.choice(obstaculos)
    return {
        "local": local,
        "objetivo": objetivo,
        "obstaculo": obstaculo,
        "descricao": f"Em {local}, você deve {objetivo}, enfrentando {obstaculo}."
    }
