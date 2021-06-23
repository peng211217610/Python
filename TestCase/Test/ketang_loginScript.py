# password = ["admin = "123321","user1" = "123456"]
username = input("请输入用户名：")
userlist = ['123321']
while username not in userlist:
    username = input("请输入正确的用户名")
    continue
else:
    errorTime = 0
    while errorTime < 3:
        psw = input("请输入密码：")
        if psw == '123456':
            #print("登陆成功")
            break
        else:
            errorTime += 1
            if errorTime >= 3:
                print("密码输入错误%s次，程序结束" % errorTime)
                exit()
            print("密码输入错误请重新输入！")
print("登陆成功")


# password = {'admin':'123321','user1':'123456'}
# userName = input('请输入用户名：').strip()
# input_errorCnt = 3
# while True:
#     if userName not in password:
#         userName = input('请输入用户名：').strip()
#     psw = input('请输入密码：').strip()
#     if (userName,psw) in password.items():
#         print('欢迎用户：{}，登陆成功！'.format(userName))
#         break
#     else:
#         input_errorCnt -= 1
#         if input_errorCnt == 0:
#             print('错误次数达到三次，请明天再试！')
#             break
#         print('密码错误，你还有{}次机会，请再次输入！'.format(input_errorCnt))











