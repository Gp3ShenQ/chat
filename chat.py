
def read(filename):
    lines = []
    with open (filename, 'r' , encoding ='utf-8-sig') as file:
        for line in file:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None  #假如對話紀錄沒有人名開頭  以防程式當掉  先宣告一個沒有裝東西的值
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person :
            new.append(person + ':' + line)
    return new

def write_file(filename, lines):
    with open (filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    lines = read('input.txt')
    lines = convert(lines)
    write_file('output.txt' , lines)

main()
