path = input("Введіть шлях до файлу:")
parts = path.split("\\")
print("шлях до файлу у встопчик")
for part in parts:[:-1]:
if p != "":
    print(part)
    filename = parts("\\")[-1]
    print("Назва файлу з розширенням:",filename)
    if "." in filename:
        name = filename.rsplit(".",1)
        print("Назва файлу", name)
        print("Розширення файлу",ext)
    else:
        print("Коли файл ен має розширення")