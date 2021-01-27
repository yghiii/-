import os, sys
list_name = []

def file_name(file_dir):
    os.chdir(file_dir)
    for root, dirs, files in os.walk(file_dir):
        print('files:', files)  # 当前路径下所有非目录子文件

    for name in files:
        head = name[:-7]
        tail = name[-7:]
        new_tail = '' # 需要添加的名称
        new_name = head + new_tail
        os.rename(name, new_name+tail)


file_name('D:\\MERGE_T2') # 文件路径


