# coding: utf-8


import ass
from ass.document import Color
import os
import sys

en_font_name = '微软雅黑'
en_font_size = 'fs14'

def main(path):
    path = path or "."
    for f in list_dir(path):
        if f and f.endswith('.ass'):
            if f == 'ok':
                continue
            
            print ''
            print f
            with open(f, 'r') as f_:
                doc = ass.parse(f_)
                print '    fn:', doc.styles[0].fontname
                print '    fs:', doc.styles[0].fontsize
                print '    bold:', doc.styles[0].bold
                print '    shadow:', doc.styles[0].shadow
                print '    border_style:', doc.styles[0].border_style
                print '    primary_color: ', doc.styles[0].primary_color

                for i in range(len(doc.styles)):
                    doc.styles[i].fontname  = 'Microsoft YaHei Light'
                    doc.styles[i].fontsize = 13
                    doc.styles[i].bold = -1
                    doc.styles[i].shadow = 0
                    doc.styles[i].outline = 0
                    doc.styles[i].border_style = 0
                    doc.styles[i].primary_color = Color(r=0xff, g=0xff, b=0xff, a=0x30)

                ok_path = os.path.join(path, 'ok')
                if not os.path.exists(ok_path):
                    os.mkdir(ok_path)

                new_path = f.replace(path, os.path.join(path, 'ok'))
                print new_path
                with open(new_path, 'w') as nf:
                    doc.dump_file(nf)

                with open(new_path, 'r') as nf:
                    txt = nf.read().replace(en_font_name, 'Microsoft YaHei Light').replace(en_font_size, 'fs11')

                with open(new_path, 'w') as nf:
                    nf.write(txt)


def list_dir(path):
    file_list = []
    for f in os.listdir(path):
        if f == 'ok':
            continue
        _path = os.path.join(path, f)
        if os.path.isdir(_path):
            list_dir(f)
        else:
            file_list.append(_path)

    return file_list


if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    main(path)
