from world_generator import gerar_missao
from dialogue_system import gerar_dialogo
from experience_adapter import ajustar_dificuldade
import random

def jogar():
    stats = {"sucessos": 0, "fracassos": 0}

    for i in range(3):
        missao = gerar_missao()
        dificuldade = ajustar_dificuldade(stats)

        print(f"\n--- Missão {i+1} [{dificuldade.upper()}] ---")
        print(missao["descricao"])

        personalidade_npc = ["impulsivo", "meticuloso", "desconfiado"]
        npc = gerar_dialogo(random.choice(personalidade_npc), missao["objetivo"])
        print(f"NPC: {npc}")

        escolha = input("Você deseja aceitar a missão? (s/n): ").strip().lower()
        if escolha == "s":
            sucesso = random.random() < 0.7
            if sucesso:
                print("✅ Você teve sucesso!")
                stats["sucessos"] += 1
            else:
                print("❌ Você falhou.")
                stats["fracassos"] += 1
        else:
            print("Você recusou a missão.")

    print(f"\nFim do jogo. Sucessos: {stats['sucessos']} | Fracassos: {stats['fracassos']}")

if __name__ == "__main__":
    jogar()
