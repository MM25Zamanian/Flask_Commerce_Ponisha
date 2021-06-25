from db.settings import mydb
from colorama import init, Fore as f

init()
mycursor = mydb.cursor()


def CREATE_TABLE(table_name: str, table_fields: list):
    command = "CREATE TABLE {} ({})".format(
        table_name,
        str(table_fields).replace('[', '').replace(']', '').replace("'", "")
    )
    mycursor.execute(command)
    print(f.GREEN + "'{}' Table Success Created".format(table_name) + f.RESET)


def SHOW_TABLES():
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)


def INSERT(table_name: str, table_fields: dict):
    values = tuple()
    keys = tuple()
    for _ in table_fields.values():
        values += (_,)
    for _ in table_fields:
        keys += (_,)
    command = "INSERT INTO {} {} VALUES ({})".format(
        table_name,
        keys,
        str("%s ,"*len(table_fields))[:-1]
    )
    mycursor.execute(str(command).replace("'", ''), values)
    mydb.commit()
    print(f.GREEN + "Success Inserted" + f.RESET)


def SELECT(table_name: str, table_fields: list):
    command = 'SELECT {} FROM {}'.format(str(table_fields).replace(
        '[', '').replace(']', '').replace("'", ""), table_name)
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    myresult2 = []

    for x in myresult:
        dic = dict()
        for i in range(len(x)):
            dic.update({table_fields[i]: x[i]})
        myresult2.append(dic)

    return myresult2


def DROP_TABLES(table_name: str):
    command = "DROP TABLE {}".format(table_name)
    mycursor.execute(command)
    print(f.RED + "'{}' Table Success Droped".format(table_name) + f.RESET)


def SELECT_WHERE(table_name: str, table_fields: list, table_field_search: str, table_value_search: str):
    command = "SELECT {} FROM {} WHERE {} ='{}'".format(
        str(table_fields).replace('[', '').replace(']', '').replace("'", ""),
        table_name,
        table_field_search,
        table_value_search
    )
    mycursor.execute(command)
    myresult = mycursor.fetchall()
    myresult2 = []

    for x in myresult:
        dic = dict()
        for i in range(len(x)):
            dic.update({table_fields[i]: x[i]})
        myresult2.append(dic)

    return myresult2


x = SELECT_WHERE('products', [
    'id',
    'name',
    'category',
    'description',
],
    'category',
    'climbing'
)
print(x)
