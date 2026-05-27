# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

# import time

# andar, total, max_cap = 0, 10, 5

# print("=== SIMULADOR DE ELEVADOR ===")

# while input("\nDeseja chamar o elevador? (S/N): ").strip().upper() == 'S':
#     try:
#         origem = int(input(f"Seu andar (0-{total}): "))
#         pessoas = int(input(f"Quantas pessoas (Máx {max_cap}): "))
#         destino = int(input(f"Destino (0-{total}): "))

#         if not (0 <= origem <= total and 0 <= destino <= total and 0 < pessoas <= max_cap and origem != destino):
#             print("Dados inválidos! Verifique os limites e tente novamente.")
#             continue

#         # Movimento até a origem e depois até o destino
#         for alvo, acao in [(origem, "Buscando passageiros"), (destino, "Indo ao destino")]:
#             if andar != alvo:
#                 print(f"\n--- {acao} ---")
#                 passo = 1 if alvo > andar else -1
#                 for andar in range(andar + passo, alvo + passo, passo):
#                     time.sleep(0.5)
#                     print(f"[Status] Andar Atual: {andar}")
        
#         print("\nPassageiros desembarcaram. Elevador livre.")

#     except ValueError:
#         print("Erro: Digite apenas números válidos.")

# print("Simulador encerrado.")
