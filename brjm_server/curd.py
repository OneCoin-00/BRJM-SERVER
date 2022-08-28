import mysqlDB as mDB


def saveData(insert_query, insert_values):
    try:
        mDB.cursor.execute(insert_query, insert_values)
        mDB.db.commit()
        return "Success"
    except Exception as e:
        return "Failure"
    

def loadData(type, select_query):
    try:
        if type == 0:
            mDB.cursor.execute(select_query)
            records = mDB.cursor.fetchone()
            return str(records[0])
        else:
            mDB.cursor.execute(select_query)
            records = mDB.cursor.fetchone()
            return records
    except Exception as e:
        return "Failure"
    

def deleteData(delete_query):
    try:
        mDB.cursor.execute(delete_query)
        mDB.db.commit()
        return "Success"
    except Exception as e:
        print("Error while inserting the new recod : ", repr(e))
        return "Failure"
        