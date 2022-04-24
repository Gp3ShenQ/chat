
def read(filename):
    lines = []
    with open (filename, 'r' , encoding ='utf-8-sig') as file:
        for line in file:
            lines.append(line.strip())
    return lines


def convert(lines):
    person = None  #假如對話紀錄沒有人名開頭  以防程式當掉  先宣告一個沒有裝東西的值
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name =='Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('Allen說了', allen_word_count, '個字, 傳了', allen_sticker_count , '個貼圖' , allen_image_count , '個圖片')
    print('Viki說了', viki_word_count, '個字, 傳了', viki_sticker_count , '個貼圖' , viki_image_count, '個圖片')


def write_file(filename, lines):
    with open (filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read('LINE-Viki.txt')
    lines = convert(lines)
    # write_file('output.txt' , lines)

main()
