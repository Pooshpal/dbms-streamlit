import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="dbms"
)
c = mydb.cursor()

#==========================================================================================

def add_user(name:str,age:int,number:str,visits:int):
    c.execute("INSERT INTO User VALUES (%s,%s,%s,%s);",(name,age, number, visits))
    print("INSERT INTO User VALUES (%s,%s,%s,%s);",(name,age, number, visits))
    mydb.commit()
    
def add_product(name:str,price:int,supplier:str):
    c.execute("INSERT INTO Product VALUES (%s,%s,%s);",(name,price,supplier))
    print("INSERT INTO Product VALUES (%s,%s,%s);",(name,price,supplier))
    mydb.commit()

def add_reward(token:str,discount:int,username:str,date_allocated,date_claimed):
    c.execute("INSERT INTO Reward VALUES (%s,%s,%s,%s,%s);",(token,discount,username,date_allocated,date_claimed))
    print("INSERT INTO Reward VALUES (%s,%s,%s,%s,%s);",(token,discount,username,date_allocated,date_claimed))
    mydb.commit()

def add_cart(cartid:str,total:int,username:str,reward_allocated,reward_claimed):
    c.execute("INSERT INTO Cart VALUES (%s,%s,%s,%s,%s);",(cartid,total,username,reward_allocated,reward_claimed))
    print("INSERT INTO Cart VALUES (%s,%s,%s,%s,%s);",(cartid,total,username,reward_allocated,reward_claimed))
    mydb.commit()

def add_cartitem(quantity:int,subtotal:int,productName:str,cartid:str):
    c.execute("INSERT INTO CartItem VALUES (%s,%s,%s,%s);",(quantity,subtotal,productName,cartid))
    print("INSERT INTO CartItem VALUES (%s,%s,%s,%s);",(quantity,subtotal,productName,cartid))
    mydb.commit()

#==========================================================================================

def update_user(old_name,name:str,age:int,number:str,visits:int):
    c.execute("UPDATE User SET Name = %s, Age = %s, Number = %s, Visits = %s WHERE Name = %s;",(name,age, number, visits, old_name))
    print("UPDATE User SET Name = %s, Age = %s, Number = %s, Visits = %s WHERE Name = %s;",(name,age, number, visits, old_name))
    mydb.commit()
    
def update_product(old_name, name:str,price:int,supplier:str):
    c.execute("UPDATE Product SET Name = %s,Price = %s,Supplier = %s WHERE Name = %s;",(name,price,supplier,old_name))
    print("UPDATE Product SET Name = %s,Price = %s,Supplier = %s WHERE Name = %s;",(name,price,supplier,old_name))
    mydb.commit()

def update_reward(old_token, token:str,discount:int,username:str,date_allocated,date_claimed):
    c.execute("UPDATE Reward SET Token = %s, Discount = %s, User_Name = %s, Date_Allocated = %s, Date_Claimed = %s WHERE Token = %s;",(token,discount,username,date_allocated,date_claimed,old_token))
    print("UPDATE Reward SET Token = %s, Discount = %s, User_Name = %s, Date_Allocated = %s, Date_Claimed = %s WHERE Token = %s;",(token,discount,username,date_allocated,date_claimed,old_token))
    mydb.commit()

def update_cart(old_cartid, cartid:str,total:int,username:str,reward_allocated,reward_claimed):
    c.execute("UPDATE Cart SET CartID = %s, Total = %s, User_Name = %s, Reward_Allocated = %s, Reward_Claimed = %s WHERE CartID = %s;",(cartid,total,username,reward_allocated,reward_claimed,old_cartid))
    print("UPDATE Cart SET CartID = %s, Total = %s, User_Name = %s, Reward_Allocated = %s, Reward_Claimed = %s WHERE CartID = %s;",(cartid,total,username,reward_allocated,reward_claimed,old_cartid))
    mydb.commit()


#=======================================================================

def view_all_data(tabl:str):
    c.execute(str('SELECT * FROM '+tabl))
    data = c.fetchall()
    return data

