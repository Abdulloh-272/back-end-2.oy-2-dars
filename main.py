
n = int(input("Bir son kiriting: "))
for i in range(n, 0, -1):
    print(i, end=', ' if i > 1 else '')

num = int(input("1 dan 10 gacha bir son kiriting: "))
if 1 <= num <= 10:
    for i in range(1, 101, num):
        print(i, end=', ' if i < 96 else '')

mevalar = input("5 ta meva nomini kiriting (vergul bilan ajrating): ").split(', ')
for meva in mevalar:
    if 'i' not in meva:
        print(meva)

