import os

def find_dup(path,newPath):

    res = readFile(path)

    writeFile(res, path, newPath)


def readFile(path):
    '''读取文件数据'''
    res = {}
    for file in os.listdir(path):
        if file.split('.')[-1] == 'txt':
            file_path = os.path.join(path, file)
            with open(file_path, 'rb') as f:
                for line in f.readlines():
                    line = line.strip().decode()
                    if line in res and file not in res[line]:
                        res[line].append(file)
                    else:
                        res[line] = [file]
    return res

def writeFile(res,path,newPath):
    '''写入文件'''
    with open(newPath,'wb') as f:
        for k,v in res.items():
            if len(v) > 1:
                f.write(('%s\n'%k).encode())
                for i in v:
                    f.write(('--%s\n'%i).encode())




if __name__ == '__main__':
    find_dup('C:\\后端工程师-上机题目\\寻找重复行','C:\\后端工程师-上机题目')