from Database import Database


class Student(object):
    # 定义用户名和密码
    user = None
    password = None

    # 录入学生
    def addstudent(self):
        studentNumber = int(input('请输入录入的学生人数：'))
        for i in range(studentNumber):
            sno = input('请输入学号：')
            if not Database.determinestudent(Database, self.user, self.password, sno):
                sname = input("请输入姓名：")
                sex = input("请输入性别：")
                birthday = input("请输入年龄：")
                phone = input("请输入电话：")
                dorm = input("请输入宿舍号：")
                Database.addstudent(Database, self.user, self.password, sno, sname, sex, birthday, phone, dorm)
                print("加入学生成功！！！\n")

    # 输出学生
    def showstudent(self):
        print("学生信息输出如下：")
        Database.showstudent(Database, self.user, self.password)

    # 删除学生
    def deletestudent(self):
        sno = input("请输入删除学生学号：")
        Database.deletestudent(Database, self.user, self.password, sno)

    # 查询学生
    def selectstudent(self):
        sno = input("请输入查询学生的学号：")
        Database.seletestudent(Database, self.user, self.password, sno)

    # 修改学生
    def changestudent(self):
        sno = input("请输入修改学生的学号：")
        if Database.seletestudent(Database, self.user, self.password, sno):
            sname = input("请输入姓名：")
            sex = input("请输入性别：")
            birthday = input("请输入年龄：")
            phone = input("请输入电话：")
            dorm = input("请输入宿舍号：")
            Database.updatestudent(Database, self.user, self.password, sno, sname, sex, birthday, phone, dorm)

    # 界面打印
    @staticmethod
    def printui():
        print("**************************")
        print("**  输入：0  --退出程序--  **")
        print("**  输入：1  --录入学生--  **")
        print("**  输入：2  --输出学生--  **")
        print("**  输入：3  --删除学生--  **")
        print("**  输入：4  --查询学生--  **")
        print("**  输入：5  --修改学生--  **")
        print("**  输入：6  --另存学生--  **")
        print("**************************")

    # 登录界面
    def ui(self):
        print("*********************************")
        print("**     欢迎使用学生信息管理系统    **")
        print("**   请输入用户名和密码以进入系统   **")
        print("*********************************")
        self.user = input("请输入用户名：")
        self.password = input("请输入密码：")

    # 保存程序
    def data(self):
        Database.savestudent(Database, self.user, self.password)

    # 程序调用
    def run(self):
        while True:
            Student.ui(Student)
            if Database.condatabase(Database, self.user, self.password):
                print("登陆成功！！！")
                self.printui()
                number = input("请输入功能前面的代码：")
                # 无限循环
                while True:
                    if int(number) == 1:
                        self.addstudent()
                        self.printui()
                        number = input('请输入功能前面的代码：')
                    elif int(number) == 2:
                        self.showstudent()
                        self.printui()
                        number = input("请输入功能前面的代码：")
                    elif int(number) == 3:
                        self.deletestudent()
                        self.printui()
                        number = input("请输入功能前面的代码：")
                    elif int(number) == 4:
                        self.selectstudent()
                        self.printui()
                        number = input("请输入功能前面的代码：")
                    elif int(number) == 5:
                        self.changestudent()
                        self.printui()
                        number = input("请输入功能前面的代码：")
                    elif int(number) == 6:
                        self.data()
                        self.printui()
                        number = input("请输入功能前面的代码：")
                    elif int(number) == 0:
                        break
                    else:
                        print("您输入的序号不对！\n请重新输入！")
                        self.printui()
                        number = input("请输入功能前面的代码：")
                print("感谢使用!!!\n再见!!!")
                exit()

            elif self.user == "exit":
                exit()
            else:
                print("用户名或密码错误！！！\n请重新输入！！！\n用户名输入 exit 退出程序！！！")