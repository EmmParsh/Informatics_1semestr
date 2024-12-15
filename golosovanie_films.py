
n = int(input()) #число голосовавших
voices = dict()
i_max = -1
first_film = ''
for i in range(n):
    name_of_film = input()
    if voices.get(name_of_film) is None:
        voices[name_of_film] = 1
    else:
        voices[name_of_film] += 1
    if voices[name_of_film] > i_max:
        i_max = voices[name_of_film]
        first_film = name_of_film

print(first_film)