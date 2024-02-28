



import pymysql

def prideti_nauja_studenta(studento_info):
    db = pymysql.connect(host='3.121.198.11',  port=3306, user='airanas', password="airanas", db='airanas')

   
    mysql_cursor = db.cursor()

    
    sql = "INSERT INTO `Studentai` VALUES {}".format(studento_info)

    
    try:
        mysql_cursor.execute(sql)
        
        db.commit()
        print("Naujas studentas įrašytas sėkmingai!")
    except Exception as e:
        
        db.rollback()
        print("Klaida įrašant naują studentą į duomenų bazę:", e)

    
    db.close()


studento_info = "('11', 'Leonavicius', 'Airanas', 'ER-1', '22222222', b'1')"
prideti_nauja_studenta(studento_info)
