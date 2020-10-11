import os
import re
import bisect

def calc(path,file):

    dateList = getDate(path)

    ranking = getRanking(dateList)

    wirteFile('%s\\%s'%(path,file),ranking)


def getDate(path):
    '''获取日期并排序'''
    dateList = []
    for file in os.listdir(path):
        if re.match('[0-9]{8}.txt', file):
            i = bisect.insort_left(dateList,int(file.split('.')[0]))
    return dateList

def getRanking(dateList):
    '''获取所有成绩并排名'''
    grade = []
    res = []
    for date in dateList:
        file_path = '%s.txt'%date
        with open(file_path, 'rb') as f:
            for item in f.readlines():
                item = item.strip().decode().split('，')
                i = bisect.bisect_right(grade,int(item[-1]))
                grade.insert(i,int(item[-1]))
                res.insert(i,item)
    return res

def wirteFile(path,ranking):
    '''写入文件'''
    rank = 1
    p = None
    with open(path,'wb') as f:
        for item in ranking[::-1]:
            if p != None and int(item[2]) < p:
                rank += 1
            p = int(item[2])
            f.write(('%s，%s，%s，%s\n'%(rank,item[0],item[1],item[2])).encode())


if __name__ == '__main__':
    calc('C:\\后端工程师-上机题目\\成绩统计数据','最终成绩.txt')