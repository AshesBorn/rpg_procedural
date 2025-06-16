import random

# Configuração de personalidades (TRAITS)
TRAITS = ["covarde", "ganancioso", "paranoico", "manipulador", "honesto"]
EMOCOES = ["neutro", "grato", "hostil", "ressentido"]

# Memória Global de mundo
memoria_mundo = {
    "reputacao_global": 0,
    "historico_npcs": {}
}

def inicializar_npc(npc_id):
    memoria_mundo["historico_npcs"][npc_id] = {
        "trait": random.choice(TRAITS),
        "emocao": random.choice(EMOCOES),
        "confianca": 0,
        "interacoes": 0
    }

# Saudação inicial baseada na personalidade
def saudacao(npc_id):
    npc = memoria_mundo["historico_npcs"][npc_id]
    base = f"[{npc['trait'].upper()}] "
    
    if npc["emocao"] == "hostil":
        return base + "Não quero conversa."
    elif npc["emocao"] == "grato":
        return base + "Ah, você já me ajudou antes."
    elif npc["emocao"] == "ressentido":
        return base + "Ainda não confio em você."
    else:
        return base + "Diga logo o que quer."

# Modificador de confiança baseado no TRAIT
def ajustar_confianca(npc_id, abordagem):
    npc = memoria_mundo["historico_npcs"][npc_id]
    delta = 0

    # Baseado na abordagem
    if abordagem == "educado(a)":
        delta += 1
    elif abordagem == "direta":
        delta += 0
    elif abordagem == "arrogante":
        delta -= 1

    # Modificador pela personalidade
    if npc["trait"] == "covarde" and abordagem == "arrogante":
        delta -= 2
    elif npc["trait"] == "manipulador" and abordagem == "arrogante":
        delta += 1
    elif npc["trait"] == "honesto" and abordagem == "educado(a)":
        delta += 1
    elif npc["trait"] == "paranoico":
        delta -= 1
    elif npc["trait"] == "ganancioso" and abordagem == "direta":
        delta += 1

    # Emoção ainda interfere
    if npc["emocao"] == "grato":
        delta += 1
    elif npc["emocao"] == "ressentido":
        delta -= 1
    elif npc["emocao"] == "hostil":
        delta -= 2

    npc["confianca"] += delta
    npc["interacoes"] += 1

    return delta

# Geração procedural de missões
def gerar_missao():
    locais = ["floresta", "caverna", "vilarejo", "montanha"]
    objetivos = ["segredo", "artefato", "desaparecimento", "selo antigo"]
    obstaculos = ["monstro", "armadilha", "enigma", "guerreiro"]

    return {
        "local": random.choice(locais),
        "objetivo": random.choice(objetivos),
        "obstaculo": random.choice(obstaculos)
    }

# Combate medieval
def combate_monstro():
    hp_jogador = 10
    hp_monstro = random.randint(6, 12)
    print("\n Monstro surgiu!")

    while hp_jogador > 0 and hp_monstro > 0:
        print(f"Seu HP: {hp_jogador} | Monstro: {hp_monstro}")
        acao = input("(a) Atacar, (d) Defender, (f) Fugir: ").lower()

        if acao == 'a':
            dano = random.randint(2, 5)
            hp_monstro -= dano
            print(f"Você causou {dano}.")
        elif acao == 'd':
            print("Você se defende.")
        elif acao == 'f':
            if random.random() > 0.5:
                print("Você fugiu.")
                return True
            else:
                print("Falha ao fugir!")
        else:
            print("Ação inválida.")

        if hp_monstro > 0:
            dano = random.randint(1, 4)
            if acao == 'd':
                dano = max(0, dano - 2)
            hp_jogador -= dano
            print(f"O monstro causou {dano} de dano!")

    if hp_jogador <= 0:
        print("Derrota!")
        return False
    else:
        print("Vitória!")
        return True

# Loop principal do jogo
def jogar():
    stats = {"sucessos": 0, "fracassos": 0}
    num_npcs = 3

    for i in range(num_npcs):
        npc_id = f"NPC_{i}"
        inicializar_npc(npc_id)
        missao = gerar_missao()

        print(f"\nInteragindo com {npc_id}")
        print("NPC:", saudacao(npc_id))

        while True:
            print("\nComo deseja interagir?")
            print("1. Educado(a)")
            print("2. Direta")
            print("3. Arrogante")
            print("4. Encerrar conversa")

            escolha = input("Escolha: ")
            if escolha == '1':
                delta = ajustar_confianca(npc_id, "educado(a)")
            elif escolha == '2':
                delta = ajustar_confianca(npc_id, "direta")
            elif escolha == '3':
                delta = ajustar_confianca(npc_id, "arrogante")
            elif escolha == '4':
                print("Conversa encerrada.")
                break
            else:
                print("Escolha inválida.")
                continue

            print(f"Confianca atual: {memoria_mundo['historico_npcs'][npc_id]['confianca']}")

            if memoria_mundo["historico_npcs"][npc_id]["confianca"] >= 2:
                print(f"\n Missão liberada: {missao['objetivo']} na {missao['local']} com obstáculo {missao['obstaculo']}.")
                sucesso = combate_monstro()
                if sucesso:
                    stats["sucessos"] += 1
                    memoria_mundo["reputacao_global"] += 1
                else:
                    stats["fracassos"] += 1
                    memoria_mundo["reputacao_global"] -= 1
                break

    print("\nFim do jogo!")
    print(f"Sucessos: {stats['sucessos']} | Fracassos: {stats['fracassos']}")
    print(f"Reputação Global: {memoria_mundo['reputacao_global']}")

if __name__ == "__main__":
    jogar()
