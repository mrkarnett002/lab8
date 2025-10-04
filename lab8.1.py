# lab8_6_1.py

# Ввід рядка від користувача
s = input("Введіть рядок символів: ")

# Створюємо словник для підрахунку
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1   # збільшуємо лічильник
    else:
        freq[ch] = 1    # перша поява символа

# Вивід результатів
print("Частота символів у рядку:")
for ch, count in freq.items():
    print(f"'{ch}' : {count}")
