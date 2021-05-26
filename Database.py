import pymysql

class Database:
    db = None
    cursor = None

    # 连接数据库
    def condatabase(self, user, password):
        # 打开数据库连接
        try:
            self.db = pymysql.connect(host='localhost', user=user, password=password,database='mydatabase')
            # 使用 cursor()方法创建一个游标对象 cursor
            self.cursor = self.db.cursor()
            return True
        except:
            return False

    # 加入学生

    def addstudent(self, user, password, sno, sname, sex, birthday, phone, dorm):
        self.condatabase(self, user, password)
        sql = 'insert into student values ' \
            '(%s, %s, %s, %s, %s, %s)' % (repr(sno), repr(sname), repr(sex), repr(birthday), repr(phone), repr(dorm))
        try:
            # 使用 execute() 方法执行sql
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        # 关闭数据库连接
        self.db.close()

    # 输出学生
    def showstudent(self, user, password):
        self.condatabase(self, user, password)
        sql = "select * from student"
        try:
            self.cursor.execute(sql)
            student = self.cursor.fetchall()
            for row in student:
                print("学号：%s  姓名：%s  性别：%s  年龄：%s  电话：%s  宿舍号：%s" % (row[0], row[1], row[2], row[3], row[4], row[5]))
        except:
            self.db.rollback()
        self.db.close()

    # 查询学生
    def seletestudent(self, user, password, sno):
        self.condatabase(self, user, password)
        sql = 'select * from student where sno = %s' % repr(sno)
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()  #获取游标下一行的数据
            print('学号：%s 姓名：%s 性别：%s 年龄：%s 电话：%s 宿舍号：%s' % (row[0], row[1], row[2], row[3], row[4], row[5]))
            return True
        except:
            self.db.rollback()
            print("未查询到当前学生！！")
            return False
        self.db.close()

    # 删除学生
    def deletestudent(self, user, password, sno):
        self.condatabase(self, user, password)
        sql = 'delete from student where sno = %s' % repr(sno)
        try:
            self.cursor.execute(sql)
            self.db.commit() #原数据库实现删除 提交数据
            print('删除成功！！！')
        except:
            self.db.rollback()
            print('不存在当前学生!!!')
        self.db.close()

    # 修改学生
    def updatestudent(self, user, password, sno, sname, sex, birthday, phone, dorm):
        self.condatabase(self, user, password)
        sql = "update student " \
              "set sname = %s ," \
              "sex = %s ," \
              "birthday = %s ," \
              "phone = %s ," \
              "dorm = %s" \
              "where sno = %s" % (repr(sname), repr(sex), repr(birthday), repr(phone), repr(dorm), repr(sno))
        try:
            self.cursor.execute(sql)
            self.db.commit()
            print('更新学生信息成功!!!')
        except:
            self.db.rollback()
            print('更新学生信息失败！！！')
        self.db.close()


    # 另存学生信息
    def savestudent(self, user, password):
        # 以追加的形式添加
        dataFile = open('E:\\text.txt', 'a')
        self.condatabase(self, user, password)
        sql = 'select * from student'
        try:
            self.cursor.execute(sql)
            student = self.cursor.fetchall()
            for row in student:
                dataFile.write("学号：" + row[0] + "  姓名：" + row[1] + " 性别：" + row[2] + "  年龄" + row[3] + "  电话：" + row[
                    4] + "  宿舍号：" + row[5] + "\n")
                print('保存成功！！！')
        except:
            self.db.rollback()
            print('保存失败!!!')
        self.db.close()
        dataFile.close()

    # 判断学号重复
    def determinestudent(self, user, password, sno):
        self.condatabase(self, user, password)
        sql = "select * from student where sno = %s" % repr(sno)
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            if row is not None:
                print("学号重复！！！\n重复学生为：")
                print(
                    "学号：%s  姓名：%s  性别：%s  年龄：%s  电话：%s  宿舍号：%s" % (row[0], row[1], row[2], row[3], row[4], row[5]))
                return True
        except:
            self.db.rollback()
            return False
        self.db.close()
