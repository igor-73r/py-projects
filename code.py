def do_matrix(s):
    l = len(s)
    k = 0
    for i in range(2, 11):
        if l % i == 0:
            k = i
            break
        else:
            k = 1
    matrix = []
    for i in range(k):
        matrix.append([int(x) for x in s[i * (l // k): (i + 1) * (l // k)]])
    return matrix, l, k


def code(s):
    matrix, l, k = do_matrix(s)
    num_of_chet = ''

    for i in range(k): 
        if (matrix[i][:l // k].count(1)) % 2 == 0:
            num_of_chet += '0'
        else:
            num_of_chet += '1'
            
    for i in range(l // k): 
        summ = 0
        for j in range(k):
            summ += matrix[j][i]
        if summ % 2 == 0:
            num_of_chet += '0'
        else:
            num_of_chet += '1'
    result = s + ' ' + num_of_chet
    return result


def decode(s):
    mtx, col, strc = do_matrix(s.split(' ')[0])
    cols = col // strc
    normal_num = s.split(' ')[1]
    errored_num = code(s.split(' ')[0]).split(' ')[1]
    position_of_error = []
    for i in range(len(errored_num)):
        if normal_num[i] != errored_num[i]:
            if i >= strc:
                position_of_error.append(i - strc)
            else:
                position_of_error.append(i)

    er_col = []
    er_str = []
    for i in range(len(position_of_error)):
        if i < ((len(position_of_error)) // 2):
            er_str.append(position_of_error[i])
        else:
            er_col.append(position_of_error[i])

    for i in range((len(position_of_error)) // 2):
        if mtx[er_str[i]][er_col[i]] == 0:
            mtx[er_str[i]][er_col[i]] = 1
        else:
            mtx[er_str[i]][er_col[i]] = 0

    new_num = ''
    for i in range(0, strc):
        for j in range(0, cols):
            new_num += str(mtx[i][j])
    return new_num

def if_correct(num, s):
    added_num = s.split(' ')[1]
    if added_num == code(num).split(' ')[1]:
        return True
    else:
        return False


s = input('Введит двоичное число: ') 
todo = int(input('Если хотите закодировать введите 1 иначе 2: '))

if todo == 1:
    print(code(s))

if todo == 2:
    s_orig, added_num = s.split(' ')
    if added_num == code(s_orig).split(' ')[1]:
        print('Ошибок не обнаружено\nЗакодированное число =', s_orig)
    else:
        if if_correct(decode(s), s) == True:
            print('Ошибки обнаружены и успешно исправленны, число = ', (decode(s)))
        else:
            print('Число слишком сильно искажено, восстановление не возможно')