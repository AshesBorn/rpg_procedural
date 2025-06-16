import random

# Memória e Emoção do NPC
memoria_npcs = {}

def inicializar_npc(npc_id):
    memoria_npcs[npc_id] = {
        "emocao": random.choice(["neutro", "grato", "hostil", "ressentido"]),
        "confianca": 0
    }

# Saudação inicial
def saudacao(npc_id):
    npc = memoria_npcs[npc_id]
    if npc["emocao"] == "hostil":
        return "Saia daqui, não quero papo."
    elif npc["emocao"] == "grato":
        return "Ah, é você. Já me ajudou antes."
    elif npc["emocao"] == "ressentido":
        return "Eu ainda não confio em você."
    else:
        return "Quem é você? Diga o que quer."

# Resposta adaptativa pela abordagem
def interagir(npc_id, abordagem):
    npc = memoria_npcs[npc_id]
    respostas = ""

    if abordagem == "educado(a)":
        respostas = "Aprecio sua educação."
        npc["confianca"] += 1
    elif abordagem == "direta":
        respostas = "Você é objetivo, mas ainda não me convenceu."
        npc["confianca"] += 0
    elif abordagem == "arrogante":
        respostas = "Não gosto desse tom. Cuidado."
        npc["confianca"] -= 1
    
    # Ajustes baseados na emoção
    if npc["emocao"] == "grato":
        npc["confianca"] += 1
    elif npc["emocao"] == "ressentido":
        npc["confianca"] -= 1
    elif npc["emocao"] == "hostil":
        npc["confianca"] -= 2

    return respostas

# Geração de missão
def gerar_missao():
    locais = ["floresta", "caverna", "vilarejo", "montanha"]
    objetivos = ["segredo", "artefato", "desaparecimento", "selo antigo"]
    obstaculos = ["monstro", "armadilha", "enigma", "guerreiro"]

    return {
        "local": random.choice(locais),
        "objetivo": random.choice(objetivos),
        "obstaculo": random.choice(obstaculos)
    }

# Sistema de combate simplificado
def combate_monstro():
    hp_jogador = 10
    hp_monstro = random.randint(6, 12)
    print("\n Monstro surgiu!")

    while hp_jogador > 0 and hp_monstro > 0:
        print(f"Seu HP: {hp_jogador} | HP do Monstro: {hp_monstro}")
        acao = input("Ação: (a) Atacar, (d) Defender, (f) Fugir: ").lower()

        if acao == 'a':
            dano = random.randint(2, 5)
            hp_monstro -= dano
            print(f"Você causou {dano} de dano!")
        elif acao == 'd':
            print("Você se defendeu, reduzindo dano.")
        elif acao == 'f':
            if random.random() > 0.5:
                print("Você fugiu com sucesso!")
                return True
            else:
                print("Falha ao fugir!")
        else:
            print("Ação inválida.")

        # Monstro ataca
        if hp_monstro > 0:
            dano = random.randint(1, 4)
            if acao == 'd':
                dano = max(0, dano - 2)
            hp_jogador -= dano
            print(f"Monstro causou {dano} de dano!")

    if hp_jogador <= 0:
        print("Você foi derrotado!")
        return False
    else:
        print("Vitória!")
        return True

# Jogo principal
def jogar():
    stats = {"sucessos": 0, "fracassos": 0}

    for i in range(3):
        npc_id = f"NPC_{i}"
        inicializar_npc(npc_id)
        missao = gerar_missao()

        print(f"\nInteragindo com {npc_id}")
        print("NPC:", saudacao(npc_id))

        # 1 única rodada de diálogo com 3 abordagens
        print("\nComo deseja falar?")
        print("1. Educado(a)")
        print("2. Direta")
        print("3. Arrogante")

        escolha = input("Escolha: ")
        if escolha == '1':
            print(interagir(npc_id, "educado(a)"))
        elif escolha == '2':
            print(interagir(npc_id, "direta"))
        elif escolha == '3':
            print(interagir(npc_id, "arrogante"))
        else:
            print("Abordagem inválida.")

        # Decisão do NPC
        if memoria_npcs[npc_id]["confianca"] >= 2:
            print(f"\n Missão liberada: {missao['objetivo']} na {missao['local']} enfrentando {missao['obstaculo']}.")
            sucesso = combate_monstro()
            if sucesso:
                stats["sucessos"] += 1
            else:
                stats["fracassos"] += 1
        else:
            print("O NPC não confiou em você. Missão negada.")

    print("\nFim do jogo!")
    print(f"Sucessos: {stats['sucessos']} | Fracassos: {stats['fracassos']}")

if __name__ == "__main__":
    jogar()
