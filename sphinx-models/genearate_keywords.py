import jieba

output = open('output.txt', 'w')
with open("basic.txt") as f:
    for line in f:
        seg_list = jieba.cut(line)
        seg_list_with_split = " ".join(seg_list)
        output.write(seg_list_with_split)

output.close()
