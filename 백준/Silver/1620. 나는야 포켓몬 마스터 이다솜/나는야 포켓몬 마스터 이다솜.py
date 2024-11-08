import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pokemon = [0]
pokemon_dict = {}
output = []

for i in range(N):
    mon = input().strip()
    pokemon.append(mon)
    pokemon_dict[mon] = i + 1

for _ in range(M):
    Q = input().strip()

    if Q.isdigit():
        output.append(pokemon[int(Q)])
    else:
        output.append(pokemon_dict[Q])

for i in output:
    print(i)