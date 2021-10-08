def multi_table(number):
    table = ''
    for i in range(1, 11):
        table += f'{i} * {number} = {number*i}\n'
    return table[:-1]