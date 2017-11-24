# 引入mysql库
import mysql.connector
# 处理数据库连接报错异常
from mysql.connector import errorcode

# 数据库链接信息
config = {
    'user': 'root',
    'password': '123456',
    'host': '23.106.147.11',
    'database': 'test',
    'raise_on_warnings': True,
    'use_pure': True,  # 是否使用 Connector/Python C Extension
}
try:
    # 调用connect()连接数据库
    cnx = mysql.connector.connect(**config)
    print("连接成功")

    # 建立连接光标
    cursor = cnx.cursor()

    # 插入insert
    add = ("insert into user  "
           "(name,age)"
           "values(%s,%s)"
           )
    data = ('Stephanie', '22')
    # cursor.execute(add, data)
    # 确保数据提交至数据库
    cnx.commit()

    query = (' select * from user ')
    cursor.execute(query)
    for (id, name, age) in cursor:
        print("{},{},{}".format(id, name, age))


except mysql.connector.Error as err:  # 处理异常信息，注意缩进
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor.close()
    cnx.close()
