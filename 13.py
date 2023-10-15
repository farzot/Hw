import os
import mysql.connector as con
os.system("cls")

def create_database(database_name):
    Con=con.connect(user='root',password='root',host='localhost')
    cur=Con.cursor()
    cur.execute(f"Create database if not exists {database_name};")
    if cur:
        print("Database yaratildi")

def create_table(database_name,table_name):
    Con=con.connect(user="root",password='root',host='localhost',database=f"{database_name}")
    cur=Con.cursor()
    cur.execute(f"""Create table if not exists {table_name} 
                (id int primary key auto_increment,name varchar(30),price varchar(15),company varchar(30),
                memory text,date varchar(25))""")
    Con.commit()
    cur.execute(f"describe {table_name}")
    # for x in cur.fetchall():
    #     print(x)

def insert_data(database_name,table_name):
    Con=con.connect(user='root',password='root',host='localhost',database=f"{database_name}")
    cur=Con.cursor()
    sql=f"""Insert Into {table_name}(name,price,company,memory,date) VALUES (%s,%s,%s,%s,%s)"""
    value=("Nokia 6300",'15','Nokia','0.5',"2009.10.07")
    cur.execute(sql,value)
    Con.commit()
    print("Bazaga ma'lumot qo'shildi!")

def show_data(database_name,table_name):
    Con=con.connect(user='root',password='root',host='localhost',database=f"{database_name}")
    cur=Con.cursor()
    cur.execute(f"SELECT* from {table_name}")
    for x in cur.fetchall():
        print(f"Kompyuter id:  {x[0]}")
        print(f"Name:       {x[1]}")
        print(f"Price:     {x[2]}")
        print(f"Company:       {x[3]}")
        print(f"Memory:     {x[4]}")
        print(f"Date:    {x[5]}")
        print("\n\t***************************\n")

def update_data(database_name,table_name,club_name,id):
    Con=con.connect(user='root',password='root',host='localhost',database=f"{database_name}")
    cur=Con.cursor()
    sql=f"""UPdate {table_name} set club = "{club_name}" where id ={id}"""
    cur.execute(sql)
    Con.commit()
    print("Bazada ma'lumot o'zgardi!")
 
def delete_data(database_name,table_name,name):
    Con=con.connect(user='root',password='root',host='localhost',database=f"{database_name}")
    cur=Con.cursor()
    cur.execute("""Delete from {} where name= "{} """.format(table_name,name))
    Con.commit()
    print(f"{name} bazadan o'chirildi!")
  

#insert_data("Phone","phone")
#update_data("Phone","phone","iphone",4)
#create_table("Phone","phone")
create_database("Phone")
#show_data("Phone","phone")