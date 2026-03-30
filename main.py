from functions import distance, translate_text, language

filename = "MyData.txt"

def read_data():
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

        A = list(map(float, lines[0].split()))
        B = list(map(float, lines[1].split()))
        lang = lines[2].strip()

        return A, B, lang


def write_data(A, B, lang):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{A[0]} {A[1]}\n")
        f.write(f"{B[0]} {B[1]}\n")
        f.write(lang)


def main():
    try:
        A, B, lang = read_data()
    except:
        A = list(map(float, input("Введіть координати точки А (x, y): ").split()))
        B = list(map(float, input("Введіть координати точки В (x, y): ").split()))
        lang = input("Введіть мову інтерфейсу: ")

        write_data(A, B, lang)
        print(f"Дані збережено в файл {filename}")
        return

    print(translate_text("Мова:", lang), language(lang))
    print(translate_text("Точка A (x, y):", lang), A[0], A[1])
    print(translate_text("Точка B (x, y):", lang), B[0], B[1])

    dA = distance(A[0], A[1])
    dB = distance(B[0], B[1])

    print(translate_text("Відстань до A:", lang), f"{dA:.3f}")
    print(translate_text("Відстань до B:", lang), f"{dB:.3f}")

    if dA > dB:
        print(translate_text("Відстань до точки А більша.", lang))
    else:
        print(translate_text("Відстань до точки В більша.", lang))


if __name__ == "__main__":
    main()