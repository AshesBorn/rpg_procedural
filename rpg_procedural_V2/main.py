from world_generator import gerar_missao
from dialogue_system import gerar_dialogo, registrar_interacao, get_memoria_npc
from experience_adapter import ajustar_dificuldade
import random

def exibir_menu():
    print("\nEscolha uma ação:")
    print("1. Falar com NPC")
    print("2. Aceitar missão")
    print("3. Recusar missão")
    print("4. Ver status")
    print("0. Sair do jogo")

def mostrar_status(stats):
    print(f"\n Status do Jogador:")
    print(f"Sucessos: {stats['sucessos']} | Fracassos: {stats['fracassos']} | Reputação: {stats['reputacao']}")

def jogar():
    stats = {"sucessos": 0, "fracassos": 0, "reputacao": 0}
    memoria_npc = {}

    for i in range(3):
        print(f"\n=========================")
        print(f" Missão {i+1}")
        missao = gerar_missao()
        dificuldade = ajustar_dificuldade(stats)

        print(f"Local: {missao['local']}")
        print(f"Objetivo: {missao['objetivo']}")
        print(f"Obstáculo: {missao['obstaculo']} [{dificuldade.upper()}]")

        npc_nome = f"NPC_{i}"
        personalidade = random.choice(["impulsivo", "meticuloso", "desconfiado"])
        fala = gerar_dialogo(personalidade, missao["objetivo"], get_memoria_npc(npc_nome))

        while True:
            exibir_menu()
            escolha = input("Digite sua escolha: ").strip()

            if escolha == "1":
                print(f"\n {npc_nome} diz: {fala}")
            elif escolha == "2":
                sucesso = random.random() < 0.7
                if sucesso:
                    print(" Missão concluída com sucesso!")
                    stats["sucessos"] += 1
                    stats["reputacao"] += 1
                    registrar_interacao(npc_nome, "ajudou")
                else:
                    print(" Você falhou na missão.")
                    stats["fracassos"] += 1
                    stats["reputacao"] -= 1
                    registrar_interacao(npc_nome, "falhou")
                break
            elif escolha == "3":
                print("Você recusou a missão.")
                registrar_interacao(npc_nome, "ignorou")
                break
            elif escolha == "4":
                mostrar_status(stats)
            elif escolha == "0":
                print("Saindo do jogo...")
                return
            else:
                print("Opção inválida. Tente novamente.")

    print("\n Fim do jogo!")
    mostrar_status(stats)

if __name__ == "__main__":
    jogar()
