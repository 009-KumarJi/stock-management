#                           STOCK MANAGEMENT PROGRAM MADE BY-
##################################################################################
#                                "KRISHNA KUMAR"  



import os
import mysql.connector as myconnect
import datetime
now = datetime.datetime.now()

def connect_check(con):
   try:
      print("connection checking...")
      myconnect.connect(host=con[2].strip("\n"),
                        port=int(con[0]),
                        user=con[3],
                        passwd=con[1].strip("\n") )
      print ("database connected...")
      correction = con
      return correction
   except:
      print ("error, in connecting database...")
      correct_con=mysql_c_o_nnect(sys=False)
      return(connect_check(correct_con))
 
def file_formation():
   try:
      path="e:\stock\data"
      os.makedirs(path)
      file = open("e:\stock\data\data.txt", "w")
      file.close()
      mysql_c_o_nnect()
   except FileExistsError:
      print ("please remove the file named 'stock' from the e drive")
      input("enter a key to countinue...")
      file_formation()
      
def mysql_c_o_nnect(sys=True):
   try:
      path=r"e:\stock\data\data.txt"
      with open(path,"r") as my1:
         lst1=my1.readlines()
         if (  (len(lst1)!= 4)  or  (sys==False)  ):
            with open(r"e:\stock\data\data.txt","w") as my:
               print("enter the correct credentials of mysql sever ")
               pr=int(input("enter port number: "))
               pa=input("enter password: ")
               hs=input("enter hostname: ")
               us=input("enter username: ")
               my.write(str(pr))
               my.write("\n"+pa)
               my.write("\n"+hs)
               my.write("\n"+us)
               return ([pr,pa,hs,us])
         else:
            return (lst1)
   except:
      file_formation()
def product_mgmt(con):
   while True :
      print("\t\t\t 1. Add New Product")
      print("\t\t\t 2. List Product")
      print("\t\t\t 3. Update Product")
      print("\t\t\t 4. Delete Product")
      print("\t\t\t 5. Back (Main Menu)")
      p=int (input("\t\tEnter Your Choice :"))
      if p==1:
         add_product(con)
      elif p==2:
         search_product(con)
      elif p==3:
         update_product(con)
      elif p==4:
         delete_product(con)
      elif p== 5 :
         break
      else:
         print ("wrong choice enter again!!!")

def purchase_mgmt(con ):
   while True :
      print("\t\t\t 1. Add Order")
      print("\t\t\t 2. List Order")
      print("\t\t\t 3. Back (Main Menu)")
      o=int (input("\t\tEnter Your Choice :"))
      if o==1 :
         add_order(con)
      elif o==2 :
         list_order(con)
      elif o== 3 :
         break
      else:
         print ("wrong choice enter again!!!")

def sales_mgmt(con ):
   while True :
      print("\t\t\t 1. Sale Items")
      print("\t\t\t 2. List Sales")
      print("\t\t\t 3. Back (Main Menu)")
      s=int (input("\t\tEnter Your Choice :"))
      if s== 1 :
        sale_product(con)
      elif s== 2 :
        list_sale(con)
      elif s== 3 :
        break
      else:
         print ("wrong choice enter again!!!")

def user_mgmt( con):
   while True :
      print("\t\t\t 1. Add user")
      print("\t\t\t 2. List user")
      print("\t\t\t 3. Back (Main Menu)")
      u=int (input("\t\tEnter Your Choice :"))
      if u==1:
         add_user(con)
      elif u==2:
         list_user(con)
      elif u==3:
         break
      else:
         print ("wrong choice enter again!!!")

def create_database(con,recreate=False):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"))
   mycursor=mydb.cursor()
   if recreate:
      print("recreating...")
      mycursor.execute("drop database stock;")
   print (" Adding database name...")
   sql = "create database if not exists stock;"
   mycursor.execute(sql)
   mycursor.execute("use stock;")
   print(" Creating PRODUCT table")
   sql = "CREATE TABLE if not exists product (\
          pcode int(4) PRIMARY KEY,\
          pname varchar(30) NOT NULL,\
          pprice float(8,2) ,\
          pqty int(10) ,\
          pcat varchar(30));"
   mycursor.execute(sql)
   print(" Creating ORDER table")
   sql = "CREATE TABLE if not exists orders (\
          orderid int(4) PRIMARY KEY ,\
          orderdate DATE ,\
          pcode char(30) NOT NULL , \
          pprice float(8,2) ,\
          pqty int(10) ,\
          supplier varchar(50),\
          pcat varchar(30));"
   mycursor.execute(sql)
   print(" ORDER table created")

   print(" Creating SALES table")
   sql = "CREATE TABLE if not exists sales (\
          salesid int(4) PRIMARY KEY ,\
          salesdate DATE ,\
          pcode varchar(30) references product(pcode), \
          pprice float(10,2) ,\
          pqty int(4) ,\
          Total double(30,2)\
          );"
   
   mycursor.execute(sql)
   print(" SALES table created")
   sql = "CREATE TABLE if not exists user (\
          uid varchar(30) PRIMARY KEY,\
          uname varchar(30) NOT NULL,\
          upwd varchar(30));"
   mycursor.execute(sql)
   print(" USER table created")
   print(" Database created...")
   
def list_database(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   sql="show tables;"
   mycursor.execute(sql)
   print ("here's your database components:")
   for i in mycursor:
      print(i)

def add_order(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   now = datetime.datetime.now()
   sql="INSERT INTO orders(orderid,orderdate,pcode,pprice,pqty,supplier,pcat)\
        values (%s,%s,%s,%s,%s,%s,%s)"
   code=int(input("Enter product code :"))
   oid=now.year+now.month+now.day+now.hour+now.minute+now.second
   qty=int(input("Enter product quantity : "))
   price=float(input("Enter Product unit price: "))
   cat=input("Enter product category: ")
   supplier=input("Enter Supplier details: ")
   val=(oid,now,code,price,qty,supplier,cat)
   mycursor.execute(sql,val)
   mydb.commit()

def list_order(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   sql="SELECT * from orders"
   mycursor.execute(sql)
   clrscr()
   print("\t\t\t\t\t\t\t ORDER DETAILS")
   print("-"*85)
   print("orderid    Date    Product code    price     quantity      Supplier      Category")
   print("-"*85)
   for i in mycursor:
      print(i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t",i[4],"\t     ",i[5],"\t",i[6])
   print("-"*85)


def db_mgmt(con):
   while True :
      print("\t\t\t 1. Database creation")
      print("\t\t\t 2. List Database")
      print("\t\t\t 3. Want to check mannually the connection of database")
      print("\t\t\t 4. Recreate database")
      print("\t\t\t 5. Back (Main Menu)")
      p=int (input("\t\tEnter Your Choice :"))
      if p ==1 :
         create_database(con)
      elif p ==2 :
         list_database(con)
      elif p== 5 :
         break
      elif p==3 :
         program()
      elif p==4:
         create_database(con,recreate=True)
      else:
         print ("wrong input enter again...")
         
def add_product(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   sql="INSERT INTO product(pcode,pname,pprice,pqty,pcat) values (%s,%s,%s,%s,%s)"
   code=int(input("\t\tEnter product code :"))
   search="SELECT count(*) FROM product WHERE pcode=%s;"
   val=(code,)
   mycursor.execute(search,val)
   for x in mycursor:
      cnt=x[0]
   if cnt==0:
      name=input("\t\tEnter product name :")
      qty=int(input("\t\tEnter product quantity :"))
      price=float(input("\t\tEnter product unit price :"))
      cat=input("\t\tEnter Product category :")
      val=(code,name,price,qty,cat)
      mycursor.execute(sql,val)
      mydb.commit()
   else:
      print("\t\t Product already exist")
def update_product(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   code=int(input("Enter the product code :"))
   qty=int(input("Enter the quantity :"))
   sql="UPDATE product SET pqty=pqty+%s WHERE pcode=%s;"
   val=(qty,code)
   mycursor.execute(sql,val)
   mydb.commit()
   print("\t\t Product details updated")

def delete_product(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   code=int(input("Enter the product code :"))
   sql="DELETE FROM product WHERE pcode = %s;"
   val=(code,)
   mycursor.execute(sql,val)
   mydb.commit()
   print(mycursor.rowcount," record(s) deleted")

def search_product(con):
   while True :
      print("\t\t\t 1. List all product")
      print("\t\t\t 2. List product code wise")
      print("\t\t\t 3. List product categoty wise")
      print("\t\t\t 4. Back (Main Menu)")
      s=int (input("\t\tEnter Your Choice :"))
      if s == 1 :
         list_product(con)
      elif s== 2 :
          code=int(input(" Enter product code :"))
          list_prcode(code,con)
      elif s== 3 :
          cat=input("Enter category :")
          list_prcat(cat,con)
      elif s== 4 :
         break
      else:
         print ("wrong input recieved...proceed with right one...")
         
def list_product(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   sql="SELECT * from product"
   mycursor.execute(sql)
   clrscr()
   print("\t\t\t\t PRODUCT DETAILS")
   print("\t\t","-"*47)
   print("\t\t code    name    price   quantity      category")
   print("\t\t","-"*47)
   for i in mycursor:
      print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t",i[4])
   print("\t\t","-"*47)

def list_prcode(code,con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   sql="SELECT * from product WHERE pcode=%s"
   val=(code,)
   mycursor.execute(sql,val)
   clrscr()
   print("\t\t\t\t PRODUCT DETAILS")
   print("\t\t","-"*47)
   print("\t\t code    name    price   quantity      category")
   print("\t\t","-"*47)
   for i in mycursor:
      print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
   print("\t\t","-"*47)


def sale_product(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   pcode=input("Enter product code: ")
   sql="SELECT count(*) from product WHERE pcode=%s;"
   val=(pcode,)
   mycursor.execute(sql,val)
   for x in mycursor:
        cnt=x[0]
   if cnt !=0 :
      sql="SELECT * from product WHERE pcode=%s;"
      val=(pcode,)
      mycursor.execute(sql,val)
      for x in mycursor:
         print(x)
         price=int(x[2])
         pqty=int(x[3])
         qty=int(input("Enter no of quantity :"))
         if qty <= pqty:
            total=qty*price
            print ("Collect  Rs. ", total)
            sql="INSERT into sales values(%s,%s,%s,%s,%s,%s)"
            val=(int(cnt)+1,datetime.datetime.now(),pcode,price,qty,total)
            mycursor.execute(sql,val)
            sql="UPDATE product SET pqty=pqty-%s WHERE pcode=%s"
            val=(qty,pcode)
            mycursor.execute(sql,val)
            mydb.commit()
         else:
           print(" Quantity not Available")
   else:
      print(" Product is not avalaible")

def list_sale(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   sql="SELECT * FROM sales"
   mycursor.execute(sql)
   print(" \t\t\t\tSALES DETAILS")
   print("-"*80)
   print("Sales id  Date    Product Code     Price             Quantity           Total")
   print("-"*80)
   for x in mycursor:
      print(x[0],"\t",x[1],"\t",x[2],"\t   ",x[3],"\t\t",x[4],"\t\t",x[5])
   print("-"*80)


def list_prcat(cat,con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   print (cat)
   sql="SELECT * from product WHERE pcat =%s"
   val=(cat,)
   mycursor.execute(sql,val)
   clrscr()
   print("\t\t\t\t PRODUCT DETAILS")
   print("\t\t","-"*47)
   print("\t\t code    name    price   quantity      category")
   print("\t\t","-"*47)
   for i in mycursor:
      print("\t\t",i[0],"\t",i[1],"\t",i[2],"\t   ",i[3],"\t\t",i[4])
   print("\t\t","-"*47)

def add_user(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   mycursor=mydb.cursor()
   uid=input("Enter emaid id :")
   name=input(" Enter Name :")
   paswd=input("Enter Password :")
   sql="INSERT INTO user values (%s,%s,%s);"
   val=(uid,name,paswd)
   mycursor.execute(sql,val)
   mydb.commit()
   print(mycursor.rowcount, " user created")


def list_user(con):
   mydb=myconnect.connect(host=con[2].strip("\n"),
                          port=int(con[0]),
                          user=con[3],
                          passwd=con[1].strip("\n"),database="stock")
   sql="SELECT uid,uname from user"
   mycursor=mydb.cursor()
   mycursor.execute(sql)
   clrscr()
   print("\t\t\t\t USER DETAILS")
   print("\t\t","-"*27)
   print("\t\t UID        name    ")
   print("\t\t","-"*27)
   for i in mycursor:
      print("\t\t",i[0],"\t",i[1])
   print("\t\t","-"*27)

def clrscr():
   print("\n"*5)

def program():
   try:
      while True:
         clrscr()
         connection = mysql_c_o_nnect()
         connec = connect_check(connection)
         print("\t\t\t STOCK MANAGEMENT")
         print("\t\t\t ****************\n")
         print("\t\t 1. PRODUCT MANAGEMENT")
         print("\t\t 2. PURCHASE MANAGEMENT")
         print("\t\t 3. SALES MANAGEMENT")
         print("\t\t 4. USER MANAGEMENT")
         print("\t\t 5. DATABASE SETUP") 
         print("\t\t 6. CHANGE SQL CREDENTIALS") 
         print("\t\t 7. EXIT\n")
         n=int(input("Enter your choice :"))
         if n== 1:
            product_mgmt(connec)
         elif n== 2:
            os.system('cls')
            purchase_mgmt(connec)
         elif n== 3:
            sales_mgmt(connec)
         elif n== 4:
            user_mgmt(connec)
         elif n==5 :
            db_mgmt(connec)
         elif n== 7:
            print("goodbye!!!")
            break 
         elif n==6:
            mysql_c_o_nnect(sys=False)
         else:
            print ("wrong input given... enter again...")
   except:
      print("program crashed due to some undefined error ...\n\n\n program is restarting..")
      print ("maybe database setup is not fullfilled here!!! ")
      print(" program is restarting..")
      program()


################################_main_###########################################################

program()

#****************************************************************************************************
#****************************************************************************************************
