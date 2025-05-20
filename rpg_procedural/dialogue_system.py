import json
import random

with open("data/personalities.json", "r", encoding="utf-8") as f:
    personalities = json.load(f)

def gerar_dialogo(personalidade, topico):
    estilo = personalities.get(personalidade, personalities["neutro"])
    frase_base = random.choice(estilo["frases"])
    return frase_base.replace("{topico}", topico)
