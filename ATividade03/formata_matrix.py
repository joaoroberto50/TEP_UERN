def write_file(file):
    with open('Dist110_clean.dat', 'w') as fp:
        for item in file:
            fp.write(item)
    return True


def set_index(file):
    index = []
    for i in range(0, 17):
        index.append(f'V{i}')
    file.pop(0)
    for j in range(0, 17):
        file[j] = f'{index[j]}\t' + file[j]
    index.insert(0, '?')
    header = ''
    for i in index:
        header += i
        header += '\t'
    header[:-1]
    header += '\n'
    file.insert(0, header)
    print(file[0])
    print('\n')
    print(file[1])
    return write_file(file)


def clean(file):
    for i in range(0, len(file)):
        file[i] = file[i].replace('9999', '-')
        file[i] = file[i][:-4]
        file[i] += '\n'
    return set_index(file)


def load_file(name):
    file = []
    with open(name) as fp:
        for item in fp:
            file.append(item)
    return clean(file)



status = load_file('./Gr17.dat')
if status == True:
    print("OK.")
