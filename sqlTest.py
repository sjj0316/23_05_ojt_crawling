import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='1234')

curser = db.cursor()

curser.execute("select * from crawler.danawacrawler d ") # query 값을 가져오는 문
result = curser.fetchall()  # ()내부 값 만큼 값을 가져오는 역할
print(result)

sql = "insert into crawler.danawacrawler " \
      "(name, price, `option`) values (%s, %s, %s)"  # 값을 지정 가능

# curser.execute(sql, ("테스트2", 50000, "옵션2"))  # 값을 집어넣음
# db.commit()

updateSQL = "UPDATE crawler.danawacrawler SET " \
            "name='테스트3', price='50000', `option`='옵션3' WHERE idx=1;"  # 위의 값처럼 %s를 넣어 사용도 가능
curser.execute(updateSQL)
db.commit()