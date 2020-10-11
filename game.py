import random


def game(chessboard,O_status,X_status):
    '''
    开始游戏
    :param chessboard: 棋盘
    :param O_status: O的状态（1为玩家，0位电脑）
    :param X_status: X的状态（1为玩家，0位电脑）
    :return:
    '''

    # 获取棋牌长度
    len_chessboard = len(chessboard)

    grade_O=grade_X=1 # O和X的分数
    possession = 'O' # 当前到谁下 'O'为O,'X'为X
    new_footwork_O = (len_chessboard-1,0) #记录O最新的步法坐标
    new_footwork_X = (0,len_chessboard-1) #记录X最新的步法坐标
    stepNumX = stepNumO = 0 # 记录每回合O和X玩家选择走的步数

    while True:
        # 打印棋盘
        print('分数：O %s - %s X'%(grade_O,grade_X))
        print('----------------')
        for i in range(len_chessboard):
            print(len_chessboard-i,end='|')
            for j in range(len_chessboard):
                print(chessboard[i][j] if chessboard[i][j] != 0 else ' ',end='|')
            print()
        print('----------------')
        # 生成底部坐标
        print(' ', end='|')
        for i in range(len_chessboard):
            print(chr(65+i),end='|')
        print()

        if possession == 'O': # 到O下棋
            if stepNumO == 0: # 若O没有可走步数，则获取步数
                stepNumO = stepNum(O_status)
            ret = footwork(chessboard, possession, new_footwork_O,O_status)
            if not ret: # 游戏结束
                print('分数：O %s-%s X\n游戏结束,%s获胜'%(grade_O,grade_X, 'O' if grade_O > grade_X else 'X'))
                break
            status, new_footwork_O = ret # 赋值状态和新坐标
            if status == 1: # 若是击杀状态
                grade_X -= 1 # 分数减一
                chessboard[new_footwork_O[0]][new_footwork_O[1]] = '\\' # 填入'\'
            else:
                chessboard[new_footwork_O[0]][new_footwork_O[1]] = 'O'
            grade_O += 1 # 分数加一
            stepNumO -= 1 # 可走步数减一
            if stepNumO == 0: # 步数为零切换对方
                possession = 'X'
        else:
            if stepNumX == 0:
                stepNumX = stepNum(X_status)
            ret = footwork(chessboard, possession, new_footwork_X,X_status)
            if not ret:
                print('分数：O %s-%s X\n游戏结束,%s获胜' % (grade_O, grade_X, 'X' if grade_X > grade_O else 'O'))
                break
            status, new_footwork_X = ret
            if status == 1:  # 若是击杀状态
                grade_O -= 1
                chessboard[new_footwork_X[0]][new_footwork_X[1]] = '\\'
            else:
                chessboard[new_footwork_X[0]][new_footwork_X[1]] = 'X'
            grade_X += 1
            stepNumX -= 1
            if stepNumX == 0:
                possession = 'O'

def stepNum(status):
    '''选择要走的步数'''
    if status == 1: # 玩家
        try:
            num = int(input('选择你要走的步数：1、2、3\n你的选择：'))
            if num not in [1,2,3]:
                num = 1
                print('输入的步数有误，默认1步')
        except:
            num = 1
            print('输入的步数有误，默认1步')
    else: # 人机
        num = random.randint(1,3)
        print('选择了%s步'%num)
    return num


def footwork(chessboard, possession, new_footwork, status):
    '''t的下一步的步法'''
    x,y = new_footwork # 获取坐标
    can_footwork = [] # 存储可走步法
    # 查询周围可走步法
    for i in [(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y+1)]:
        try:
            if chessboard[i[0]][i[1]] == possession or chessboard[i[0]][i[1]] == '\\' or i[0] < 0 or i[1] < 0:
                continue
            can_footwork.append('%s%s'%(chr(65+i[1]),len(chessboard)-i[0]))
        except:
            continue

    # 若没有可走的路，则返回True
    if not can_footwork:
        return False

    if status:
        # 获取用户输入的位置
        while True:
            sel = input('您可走的位置有：%s\n%s：'%(' '.join(can_footwork),possession))
            if sel in can_footwork:
                break
            print('--输入位置有误！请重新输入--')
    else:
        # 人机随机下一步
        sel = random.choice(can_footwork)
        print('您可走的位置有：%s\n%s：%s'%(' '.join(can_footwork),possession,sel))
    # 执行下一步步法
    new_footwork = (len(chessboard)-int(sel[1:]),ord(sel[0])-65)
    status = -1 # 返回状态，1为击杀
    # 若不为零则击杀
    if chessboard[new_footwork[0]][new_footwork[1]] != 0:
        status = 1
    # 返回新坐标
    return status,new_footwork



def create_chessboard(num):
    '''创建棋牌'''
    chessboard = [[0 for j in range(num)] for i in range(num)]
    chessboard[0][num-1] = 'X'
    chessboard[num-1][0] = 'O'
    return chessboard

def main():
    while True:
        gameType = input('选择游戏模式\n1.1v1\n2.1v人机\n你的选择：')
        # 玩家选择棋牌大小
        sel = input('1.6*6\n2.7*7\n3.8*8\n选择棋盘大小：')
        # 生成棋牌
        if sel == '1':
            chessboard = create_chessboard(6)
        elif sel == '2':
            chessboard = create_chessboard(7)
        elif sel == '3':
            chessboard = create_chessboard(8)
        else:
            print('输入异常,游戏重启')
            continue
        if gameType == '1':
            # 进入游戏
            game(chessboard,1,1)
        elif gameType == '2':
            # 根据选择阵营进入游戏
            camp = input('阵营选择\n1.O阵营\n2.X阵营\n3.随机阵营\n你的选择：')
            if camp == '1':
                game(chessboard, 1, 0)
            elif camp == '2':
                game(chessboard, 0, 1)
            elif camp == '3':
                game(chessboard, 1, 0) if random.randint(0,1) else game(chessboard, 0, 1)
            else:
                print('输入异常,游戏重启')
                continue



if __name__ == '__main__':
    main()

