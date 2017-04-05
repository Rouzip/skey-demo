import hashlib

serverSave = ['']
cilentSave = 1022

# 使用md5来对密钥进行计算，计算出1024个值
def initKeys(key):
    md5 = hashlib.md5(key.encode('utf-8'))
    md5Data = md5.hexdigest()
    try:
        with open('keylist.txt','w') as fp: 
            # 设置hash链的长度为1024
            for i in range(1023):
                fp.write(md5Data + '\n')
                md5Data = hashlib.md5(md5Data.encode('utf-8')).hexdigest()
            else:
                # 最后一个值服务器进行保存
                serverSave[0] = md5Data
    except Exception as e:
        print('Something wrong: ')
        print(e)
    

# 服务器
def serverJudge(message:str)->bool:
    global serverSave
    hashMessage = hashlib.md5(message.strip().encode('utf-8')).hexdigest()
    if hashMessage == serverSave[0]:
        # 对传送过来的message进行hash计算，与储存的进行比较验证
        serverSave[0] = message.strip()
        return True
    else:
        return False


# 客户端
def cilentTrans():
    global cilentSave
    with open('keylist.txt','r') as fp:
        for num,line in enumerate(fp.readlines()):
            if num == cilentSave:
                cilentSave -= 1
                if cilentSave == 0:
                    print('hash链已经用完，请及时更换')
                return line
    return None


# 样例测试，对一组hash值进行测试
# 测试进行了三次，说明hash链都可以进行
if __name__ == '__main__':
    initKeys('you are my love~') 
    for i in range(3):
        cilent = cilentTrans()
        server = serverJudge(cilent)
        print(server)
