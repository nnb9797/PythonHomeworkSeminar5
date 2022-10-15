# 2). Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encoding(text: str) -> str:
    text_encoded = ''
    count = 1
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            count += 1
        else:
            if count > 0:
                text_encoded = text_encoded + str(count) + text[i]
            else:
                text_encoded = text_encoded + text[i]
            count = 1
    if count > 1:
        text_encoded = text_encoded + str(count) + text[i]
    else:
        text_encoded = text_encoded + text[i+1]
    return text_encoded

def rle_decoding(text: str) -> str:
    text_decoded = ''
    number = ''
    for i in range(len(text)):
        if text[i].isdigit():
            number += text[i]
        else:
            if not number == '':
                text_decoded = text_decoded + int(number) * text[i]
            else:
                text_decoded = text_decoded + text[i]
            number = ''
    return text_decoded


with open("input.txt", "r") as data:
    text_str = data.read()

text_encoded = rle_encoding(text_str)

print(f"Входные данные:{text_str}")
print(f"Сжатые данные:{text_encoded}")

text_initial = rle_decoding(text_encoded)
print(f"Восстановленные данные: {text_initial}")

with open("output.txt", "w") as data:
     text_initial = data.write(text_encoded)
