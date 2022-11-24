def get_keys():
    key1 = input('Введите 1 ключ --> ')
    key2 = input('Введите 2 ключ --> ')
    return key1, key2


def show_matrix(matrix):                                             
    print('-' * 40)
    for row in matrix:
        print(*row, sep=' ', end='\n')
    print('-' * 40)


def transpose(matrix):                                              
    new_matrix = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp += [matrix[j][i]]
        new_matrix.append(temp)
    return new_matrix


def is_valid_keys(key1, key2, required_length):            
    return len(key1) * len(key2) >= required_length

choice  = int(input('Введите 1 если хотите зашифровать, 2 если дешифровать --> '))

text = input('Введите текст --> ')
key1, key2 = get_keys()
while not is_valid_keys(key1, key2, len(text)):
    print('Слишком короткие ключи!')
    key1, key2 = get_keys()

n = 0
m = 0
symbols_matrix = []

if choice == 1:
    symbols_matrix.append(key1)

    for i in range(len(key2)):                  
        temp = ''
        for j in range(len(key1)):
            if n < len(text):
                if text[n] != ' ':
                    temp += text[n]
                else:
                    temp += '_'
            else:
                temp += '_'
            n += 1
        m = max(m, len(temp))
        symbols_matrix.append(temp)
else:
    symbols_matrix.append(sorted(key2))

    for i in range(len(key1)):
        temp = ''
        for j in range(len(key2)):
            if n < len(text):
                if text[n] != ' ':
                    temp += text[n]
                else:
                    temp += '_'
            else:
                temp += '_'
            n += 1
        m = max(m, len(temp))
        symbols_matrix.append(temp)


for i in range(len(symbols_matrix)):                     
    symbols_matrix[i] = list(symbols_matrix[i])
print()
show_matrix(symbols_matrix[1:])

if choice == 1:
    symbols_matrix = transpose(sorted(transpose(symbols_matrix)))
    symbols_matrix.pop(0)
    symbols_matrix = transpose(symbols_matrix)
    symbols_matrix.insert(0, list(key2))
    symbols_matrix = transpose(symbols_matrix)
    symbols_matrix = sorted(symbols_matrix)
    symbols_matrix = transpose(symbols_matrix)
    symbols_matrix.pop(0)
else:

    for m in range(len(key2)):
        for n in range(len(key2)):
            if symbols_matrix[0][n] == key2[m]:
                for y in range(len(key1) + 1):
                    symbols_matrix[y][m], symbols_matrix[y][n] = symbols_matrix[y][n], symbols_matrix[y][m]

    symbols_matrix.pop(0)
    symbols_matrix = transpose(symbols_matrix)
    symbols_matrix.insert(0, list(sorted(key1)))

    for m in range(len(key1)):
        for n in range(len(key1)):
            if symbols_matrix[0][n] == key1[m]:
                for y in range(len(key2) + 1):
                    symbols_matrix[y][m], symbols_matrix[y][n] = symbols_matrix[y][n], symbols_matrix[y][m]
    symbols_matrix.pop(0)


result = ''                                               
for row in symbols_matrix:
    result += ''.join(row)


space_symbol = '+'                                          
t = space_symbol * ((len(result) - len('Шифр')) // 2)
print(t + 'Шифр' + t)
print(result)
print(t + t + len('Шифр') * space_symbol)

input()