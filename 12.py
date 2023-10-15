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
                (id int primary key auto_increment,name varchar(30),number int,club varchar(30),
                position text,nationality varchar(25))""")
    Con.commit()
    cur.execute(f"describe {table_name}")
    for x in cur.fetchall():
        print(x)

def insert_data(database_name,table_name):
    Con=con.connect(user='root',password='root',host='localhost',database=f"{database_name}")
    cur=Con.cursor()
    sql=f"""Insert Into {table_name}(name,number,club,position,nationality) VALUES (%s,%s,%s,%s,%s)"""
    value=("Pedri",10,'Barselona','Central Forward','Spain')
    cur.execute(sql,value)
    Con.commit()
    print("Bazaga ma'lumot qo'shildi!")
def show_data(database_name,table_name):
    Con=con.connect(user='root',password='root',host='localhost',database=f"{database_name}")
    cur=Con.cursor()
    cur.execute(f"SELECT* from {table_name}")
    for x in cur.fetchall():
        print(f"Player id:  {x[0]}")
        print(f"Name:       {x[1]}")
        print(f"Number:     {x[2]}")
        print(f"Club:       {x[3]}")
        print(f"Amplus:     {x[4]}")
        print(f"Country:    {x[5]}")
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
  

#insert_data("Player","player1")
#update_data("Player","player1","Nasaf",4)
# create_table("Player","player1")
create_database("Player")
#show_data("Player","player1")