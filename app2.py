import random
from google.colab import output
import time
#                       0.   1.    2.
pedra_papel_tesoura = ['🗿', '📄', '✁']
maquina = random.choice(pedra_papel_tesoura)
placar = {'player':0, 'maquina':0}
# Mapeamento das combinações vencedoras
vitorias = {
      "🗿": "✁",  # Pedra ganha de Tesoura
      "✁": "📄",  # Tesoura ganha de Papel
      "📄": "🗿"   # Papel ganha de Pedra
}

# mensagens iniciais
while True:
  output.clear()
  print('Bem vindo ao jogo de Pedra, Papel e Tesoura!')
  print(f'Placar: {placar["player"]} - {placar["maquina"]}')
  print('\nEscolha uma opção:')
  print('1 - Pedra    🗿')
  print('2 - Papel    📄')
  print('3 - Tesoura  ✁')
  print('4 - Sair')

  player = int(input('\nSua escolha: '))
  if player == 4:
      print('\nObrigado por jogar!')
      break
  player = pedra_papel_tesoura[player - 1]

  # print(f'\nVocê escolheu {player}')
  # print(f'A máquina escolheu {maquina}')

  if player == maquina:
      resultado = "Empatou"
  elif vitorias.get(player) == maquina:
      resultado = "Ganhou"
      placar["player"] += 1
  else:
      resultado = "Perdeu"
      placar["maquina"] += 1

  print(f"{player} vs {maquina} >>> {resultado}")
  time.sleep(3)
