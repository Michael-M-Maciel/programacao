lista_tupla = [('Flamengo', [10, 23]),
               ('Palmeiras', [10, 50]),
               ('Redbull', [5, 21]),
               ('Cruzeiro', [17, 20]),
               ('Vasco', [188, 5])
]


media = []
media_times = []

for time, pontos in lista_tupla:
    if pontos:
        media_f = sum(pontos) / len(pontos)
        media.append(media_f)
        

    print(f'o time do {time} fez {sum(pontos)} pontos e sua média é {media_f}')