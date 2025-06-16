import random

# Definição de estados emocionais e memória
EMOCOES = ["neutro", "hostil", "amigável", "grato", "ressentido"]
memoria_npcs = {}

# Inicialização da memória
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

# Implementação da Behavior Tree simplificada
def construir_fala(npc_id, topico):
    if npc_id not in memoria_npcs:
        registrar_interacao(npc_id, "novo")

    npc = memoria_npcs[npc_id]
    npc["topicos_recentes"].append(topico)
    interacoes = npc["interacoes"]
    desconfiante = len(npc["topicos_recentes"]) > 3

    # Árvore de comportamento
    if npc["emocao"] == "hostil":
        return "Não confio em você. Não tenho nada a dizer."
    
    elif npc["emocao"] == "ressentido":
        return f"Ainda estou irritado com você. Sobre '{topico}', não espere muita ajuda."

    elif desconfiante:
        return "Você está fazendo perguntas demais... Isso está me deixando desconfortável."

    elif npc["emocao"] == "grato":
        return f"Agradeço sua ajuda anterior. Sobre '{topico}', vou colaborar."

    elif interacoes < 2:
        return f"É nossa primeira conversa. Posso considerar falar sobre '{topico}'."

    else:
        return f"Não tenho certeza se devo confiar em você para falar sobre '{topico}'."

# Gerador de missões (mantemos como está)
locais = ["floresta encantada", "caverna sombria", "vilarejo abandonado", "montanha nevada"]
objetivos = ["descobrir o segredo", "resgatar o artefato", "investigar o desaparecimento", "destruir o selo antigo"]
obstaculos = ["guardado por uma criatura", "escondido por armadilhas", "protegido por um enigma", "esquecido no tempo"]

def gerar_missao():
    return {
        "local": random.choice(locais),
        "objetivo": random.choice(objetivos),
        "obstaculo": random.choice(obstaculos)
    }

# Ajuste de dificuldade permanece igual
def ajustar_dificuldade(stats):
    if stats["fracassos"] > stats["sucessos"]:
        return "fácil"
    elif stats["sucessos"] >= 2:
        return "difícil"
    return "normal"

# Loop do jogo
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
        print("\n NPC:", fala)

        escolha = input("Você aceita a missão? (s/n): ").strip().lower()
        if escolha == "s":
            sucesso = random.random() < 0.7
            if sucesso:
                print("Sucesso na missão!")
                stats["sucessos"] += 1
                stats["reputacao"] += 1
                registrar_interacao(npc_id, "ajudou")
            else:
                print("Você falhou.")
                stats["fracassos"] += 1
                stats["reputacao"] -= 1
                registrar_interacao(npc_id, "falhou")
        else:
            print("Você recusou a missão.")
            registrar_interacao(npc_id, "ignorou")

        mostrar_status(stats)

    print("\nFim do jogo.")
    mostrar_status(stats)

if __name__ == "__main__":
    jogar()
