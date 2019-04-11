import pymysql
connection = pymysql.connect(host='127.0.0.1',
                             user='sqlsql',
                             password='password',
                             db='CDW_SAPP',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
print ("connect successful!!")

try:
    with connection.cursor() as cursor:
        # SQL
        sql = "SELECT * FROM CDW_SAPP_BRANCH;"
        # Execute query.
        cursor.execute(sql)
        print ("cursor.description: ", cursor.description)
        print()
        for row in cursor:
            print(row)
finally:
    # Close connection.
    connection.close()
