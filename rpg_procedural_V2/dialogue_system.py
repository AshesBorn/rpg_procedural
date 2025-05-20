import json
import random

with open("data/personalities.json", "r", encoding="utf-8") as f:
    personalities = json.load(f)

memoria_npcs = {}

def registrar_interacao(nome, resultado):
    memoria_npcs[nome] = resultado

def get_memoria_npc(nome):
    return memoria_npcs.get(nome, "novo")

def gerar_dialogo(personalidade, topico, memoria):
    estilo = personalities.get(personalidade, personalities["neutro"])
    
    if memoria == "ajudou":
        saudacao = "Ah, é você novamente, meu herói!"
    elif memoria == "falhou":
        saudacao = "Espero que dessa vez você não me decepcione..."
    elif memoria == "ignorou":
        saudacao = "Você me ignorou da última vez, lembra?"
    else:
        saudacao = "Olá, viajante."

    frase = random.choice(estilo["frases"]).replace("{topico}", topico)
    return f"{saudacao} {frase}"
