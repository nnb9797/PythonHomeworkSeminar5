# 2). Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


with open("input.txt", "r") as data:
    my_text = data.read()

print(f"входные данные: {my_text}")

def encode_rle(inp_symbols):
    str_code = ""
    prev_char = ""
    count = 1
    for char in inp_symbols:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_code = encode_rle(my_text)
print(f"выходные данные: {str_code}")
new_data = str_code

with open("output.txt", "w") as data:
    data.write(new_data)