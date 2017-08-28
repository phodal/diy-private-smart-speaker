#!/usr/bin/python
# -*- coding: <encoding name> -*-

new_dict = open('new.dic', 'w',  encoding='UTF-8')
origin_dicts = open('TAR0287/0287.dic', encoding='UTF-8')
with origin_dicts as origin_file:
    print(origin_file)
    for origin_dict in origin_file:
        origin_key = origin_dict.split("\t")[0]
        with open("zh_broadcastnews_utf8.dic", encoding='UTF-8') as f:
            for line in f:
                split = line.split(" ")
                if len(split) >= 2:
                    key = split[0]
                    value = split[1]
                    if key == origin_key:
                        new_line = origin_key + "\t" + line[len(key) + len(" "):]
                        new_dict.write(new_line)

origin_dicts.close()
new_dict.close()
