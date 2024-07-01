import random

pedra_papel_tesoura = ['🪨', '📄', '✂️']
maquina = random.choice(pedra_papel_tesoura)
# print(maquina)
print('*** Joquempô Game ***')
print('Escolha sua opção')
print('1-> 🪨 ')
print('2-> 📄 ')
print('3-> ✂️  ')
player = int(input('\nDigite sua opção: '))

if player == 1:
    player = '🪨'
elif player == 2:
    player = '📄'
else:
    player = '✂️'

if player == maquina:
    print(f"{player} vs {maquina} >>> Empatou")
elif (player == "🪨" and maquina == "✂️") or \
     (player == "✂️" and maquina == "📄") or \
     (player == "📄" and maquina == "🪨"):
    print(f"{player} vs {maquina} >>> Ganhou")
else:
    print(f"{player} vs {maquina} >>> Perdeu")