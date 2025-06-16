import random

# Emoções e memória
EMOCOES = ["neutro", "hostil", "grato", "ressentido"]
memoria_npcs = {}

def registrar_interacao(npc_id, resultado):
    if npc_id not in memoria_npcs:
        memoria_npcs[npc_id] = {
            "interacoes": 0,
            "emocao": "neutro",
            "topicos_recentes": []
        }
    npc = memoria_npcs[npc_id]
    npc["interacoes"] += 1

    if resultado == "ajudou":
        npc["emocao"] = "grato"
    elif resultado == "falhou":
        npc["emocao"] = "ressentido"
    elif resultado == "ignorou":
        npc["emocao"] = "hostil"

# PRIORITY SELECTOR (coração da BT)
def construir_fala(npc_id, topico):
    if npc_id not in memoria_npcs:
        registrar_interacao(npc_id, "novo")
    npc = memoria_npcs[npc_id]
    npc["topicos_recentes"].append(topico)
    interacoes = npc["interacoes"]
    perguntas_excesso = len(npc["topicos_recentes"]) > 3

    # PRIORIDADE 1 - Hostilidade extrema
    if npc["emocao"] == "hostil":
        return "Vá embora."

    # PRIORIDADE 2 - Ressentimento
    if npc["emocao"] == "ressentido":
        return f"Não conte comigo em '{topico}'."

    # PRIORIDADE 3 - Excesso de perguntas (desconfiança)
    if perguntas_excesso:
        return "Chega de perguntas."

    # PRIORIDADE 4 - Gratidão
    if npc["emocao"] == "grato":
        return f"Vou te ajudar com '{topico}'."

    # PRIORIDADE 5 - Neutro padrão
    if interacoes <= 1:
        return f"O que você quer saber sobre '{topico}'?"
    else:
        return f"Talvez eu diga algo sobre '{topico}' depois."

# Geração de missões
locais = ["floresta", "caverna", "vilarejo", "montanha"]
objetivos = ["segredo", "artefato", "desaparecimento", "selo antigo"]
obstaculos = ["criatura", "armadilhas", "enigma", "tempo"]

def gerar_missao():
    return {
        "local": random.choice(locais),
        "objetivo": random.choice(objetivos),
        "obstaculo": random.choice(obstaculos)
    }

# Ajuste de dificuldade
def ajustar_dificuldade(stats):
    if stats["fracassos"] > stats["sucessos"]:
        return "fácil"
    elif stats["sucessos"] >= 2:
        return "difícil"
    return "normal"

# Jogo principal
def mostrar_status(stats):
    print(f"Sucessos: {stats['sucessos']} | Fracassos: {stats['fracassos']} | Reputação: {stats['reputacao']}")

def jogar():
    stats = {"sucessos": 0, "fracassos": 0, "reputacao": 0}

    for i in range(3):
        print("\n=== Missão", i + 1, "===")
        missao = gerar_missao()
        dificuldade = ajustar_dificuldade(stats)
        npc_id = f"NPC_{i}"
        topico = missao["objetivo"]

        print("Local:", missao["local"])
        print("Objetivo:", topico)
        print("Obstáculo:", missao["obstaculo"])
        print("Dificuldade:", dificuldade)

        fala = construir_fala(npc_id, topico)
        print("\nNPC:", fala)

        escolha = input("Aceita a missão? (s/n): ").strip().lower()
        if escolha == "s":
            sucesso = random.random() < 0.7
            if sucesso:
                print("Sucesso!")
                stats["sucessos"] += 1
                stats["reputacao"] += 1
                registrar_interacao(npc_id, "ajudou")
            else:
                print("Falhou.")
                stats["fracassos"] += 1
                stats["reputacao"] -= 1
                registrar_interacao(npc_id, "falhou")
        else:
            print("Missão recusada.")
            registrar_interacao(npc_id, "ignorou")

        mostrar_status(stats)

    print("\nFim do jogo.")
    mostrar_status(stats)

if __name__ == "__main__":
    jogar()
