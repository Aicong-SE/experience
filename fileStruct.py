import os

def struct(path,retract,i=1):
    '''
    打印当前目录中产生的目录和文件系统树结构
    :param path: 路径
    :param i: 文件层级
    :return:
    '''

    for file in os.listdir(path): # 遍历路径下的文件名
        file_path = os.path.join(path, file) # 生成文件路径
        print((retract * i) + file) # 打印文件名
        if os.path.isdir(file_path): # 判断文件是不是目录
            struct(file_path,retract,i+1) # 递归进入目录

if __name__ == '__main__':
    path = './' # 默认当前目录
    print(path)
    struct(path,'--')
