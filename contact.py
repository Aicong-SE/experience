import sqlite3
import re


def save(cur):
    '''
    保存联系人
    :return: True
    '''

    # 获取信息
    name = input('请输入姓名：')
    familyName = input('请输入姓氏：')
    site = input('请输入地址：')
    phone = input('请输入电话号码：')
    email = input('请输入电子邮箱：')

    # 添加记录
    cur.execute("INSERT INTO contact(name,familyName,site,phone,email) "
                "VALUES ('%s','%s','%s','%s','%s')"%(name,familyName,site,phone,email))

    return True

def delete(cur):
    '''
    删除联系人
    :return:
    '''
    # 获取联系人ID
    ID = input('请输入联系人ID:')

    # 数据库删除联系人
    c = cur.execute('delete from contact where id = %s'%ID)

    return True

def update(cur):
    '''
    更新联系人
    :return:
    '''
    # 获取联系人ID
    ID = input('请输入联系人ID:')

    # 获取修改后的信息，不需要修改的信息不填数据
    data = {}
    name = input('新姓名：')
    if name:
        data['name'] = name
    familyName = input('新姓氏：')
    if familyName:
        data['familyName'] = familyName
    site = input('新地址：')
    if site:
        data['site'] = site
    phone = input('新电话号码：')
    if phone:
        data['phone'] = phone
    email = input('新电子邮箱：')
    if email:
        data['email'] = email

    # 生成修改信息的sql语句
    update_data = ''
    for k,v in data.items():
        update_data += "%s = '%s',"%(k,v)
    update_sql = 'update contact set %s where id = %s' % (update_data[:-1], ID)

    # 修改数据库 ，
    cur.execute(update_sql)

def select(cur):
    '''查看联系人'''
    # 选择查看方式
    sel = input('1.查看所有联系人\n2.查看重复的联系人\n3.查看有连续字符的联系人\n你的选择：')

    if sel == '1':
        all_contacts(cur)
    elif sel == '2':
        repetition(cur)
    elif sel == '3':
        re_contacts(cur)
    else:
        print('退出查看联系人')
        return

def all_contacts(cur):
    '''查看所有联系人'''
    cursor = cur.execute("SELECT *  from contact order by craetetime desc")
    # 遍历联系人
    for item in cursor:
        print('%s|%s|%s|%s|%s|%s|%s' % (item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

def repetition(cur):
    '''查看重复联系人'''
    cursor = cur.execute("select * from contact where name in (select name from contact group by name having count(name) > 1) order by craetetime desc")
    # 遍历联系人
    for item in cursor:
        print('%s|%s|%s|%s|%s|%s|%s' % (item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

def re_contacts(cur):
    '''正则查询含有连续字符的联系人'''
    cursor = cur.execute("SELECT *  from contact order by craetetime desc")
    # 遍历联系人
    for item in cursor:
        # 正则匹配是否含有连续字符
        if re.match(r'\S*([\u4e00-\u9fa5a-zA-Z])\1', item[1], flags=0):
            print('%s|%s|%s|%s|%s|%s|%s' % (item[0], item[1], item[2], item[3], item[4], item[5], item[6]))

def connect():
    '''
    连接数据库，若没有表则创建表
    :return: 数据库对象和游标
    '''

    # 连接数据库
    conn = sqlite3.connect('test.db')

    # 获取游标
    cur = conn.cursor()

    # 创建contact表，若存在跳过创建
    try:
        cur.execute('''create table contact(
                id INTEGER PRIMARY KEY,
                name char(50),
                familyName char(50),
                site varchar(100),
                phone char(11),
                email char(50),
                craetetime TIMESTAMP default (datetime('now', 'localtime')))''')
    except:
        pass

    return conn,cur

def main():
    '''
    程序启动
    :return:
    '''

    conn,cur = connect() # 连接数据库

    while True:
        # 打印选项
        sel = input('1:添加联系人\n2:删除联系人\n3:更新联系人\n4:查看联系人\n5:保存并退出\n您的选择：')

        if sel == '1':
            if save(cur):
                print('添加成功')

        elif sel == '2':
            if delete(cur):
                print('删除成功')

        elif sel == '3':
            if update(cur):
                print('修改成功')

        elif sel == '4':
            select(cur)

        elif sel == '5':
            break

        else:
            print('暂无此选项，请重新选择')

    conn.commit() # 保存
    conn.close() # 关闭数据库连接

if __name__ == '__main__':
    main()