from datetime import datetime as d
import mysql.connector as c
con=c.connect(host='localhost', user='root',passwd='MySQLPSWD#1',database='TAJ_HOTEL')
cursor=con.cursor(buffered=True)


def roommenu():
    query="select S_NO,TYPE from rooms"
    cursor.execute(query)
    menu=cursor.fetchall()
    for i in menu:
        print(i)
def roomupdate():
    print("press 1 for adding a room")
    print("press 2 for deleting a room")
    print("press 3 for changing price")
    la=int(input("enter your choice"))
    if la==1:
        m=int(input("enter new s_no:"))
        n=input("enter new type")
        o=int(input("enter new price"))
        q="insert into rooms values({},'{}',{})".format(m,n,o)
        cursor.execute(q)
        con.commit()
    elif la==2:
        m=int(input("enter s_no of room to delete"))
        q="delete from rooms where S_NO={}".format(m)
    elif la==3:
        m=int(input("enter s_no of room you want to update price of:"))
        n=int(input("enter new price:"))
        q="update rooms set price={} where S_NO={}".format(n,m)
    else:
        print("invalid")
        
def ro_om():
    Sno=int(input("what type of room?:"))
    stay=int(input("for how many days would you like to stay?:"))
    q="select rent from rooms where S_NO={}".format(Sno)
    cursor.execute(q)
    t=cursor.fetchall()
    j=t[0]
    k=j[0]
    
    a=k*stay
    
    return a

#b=ro_om()
def restmenu():
    query="select R_NO,TYPE from RESTAURENT"
    cursor.execute(query)
    menu=cursor.fetchall()
    for i in menu:
        print(i)
def dishupdate():
    print("press 1 for adding a dish")
    print("press 2 for deleting a dish")
    print("press 3 for changing price")
    la=int(input("enter your choice"))
    if la==1:
        m=int(input("enter new r_no:"))
        n=input("enter new type")
        o=int(input("enter new price"))
        q="insert into restaurent values({},'{}',{})".format(m,n,o)
        cursor.execute(q)
        con.commit()
    elif la==2:
        m=int(input("enter r_no of dish to delete"))
        q="delete from restaurent where R_NO={}".format(m)
    elif la==3:
        m=int(input("enter s_no of dish you want to update price of:"))
        n=int(input("enter new price:"))
        q="update restaurent set price={} where R_NO={}".format(n,m)
    else:
        print("invalid")
    
def re_st():
    x=int(input("how diff kinds of dishes would you like to have?"))
    L1=[]
    b=0
    for la in range(0,x):
        Sno=int(input("what type of dish?:"))
        stay=int(input("quantity of same dish?"))
        q="select price from restaurent where R_NO={}".format(Sno)
        cursor.execute(q)
        t=cursor.fetchall()
        j=t[0]
        k=j[0]
        a=k*stay
        
        L1.append(a)
    for h in range(0,x):
        b=b+L1[h]
    return b
        
#a=re_st()





def recreation():
    query="select G_NO,TYPE from RECREATION"
    cursor.execute(query)
    menu=cursor.fetchall()
    for i in menu:
        print(i)
def re_cr():
    x=int(input("how diff kinds of recreational activities would ypu like to do?"))
    L1=[]
    b=0
    for la in range(0,x):
        Sno=int(input("what type of activity:"))
        stay=int(input("how many times would you do it?"))
        q="select price from recreation where G_NO={}".format(Sno)
        cursor.execute(q)
        t=cursor.fetchall()
        j=t[0]
        k=j[0]
        a=k*stay
        
        L1.append(a)
    for h in range(0,x):
        b=b+L1[h]
    return b
#c=re_cr()
#d=a+b+c
#print(d)




def addcustomer():
    global p
    p=int(input("enter cid:"))
    global q
    q=input("enter customer name")
    global r
    r=input("enter checkin date YYYY-MM-DD")
    global s
    s=input("enter checkout date ")
    queryy="insert into customer_1 values({},'{}','{}','{}')".format(p,q,r,s)
    cursor.execute(queryy)
    con.commit()
    
    
def showcustomers():
    queryy="select * from customer_1"
    cursor.execute(queryy)
    cdata=cursor.fetchall()
    for f in cdata:
        print(f)

#addcustomer()
#showcustomers()


def makemajor():
    global p
    global q
    global a
    global b
    global c
    jjj=a+b+c
    global r
    global s
    QUERY="insert into CUSTOMER values({},'{}','{}','{}',{},{},{},{})".format(p,q,r,s,c,a,b,jjj)
    cursor.execute(QUERY)
    con.commit()

def showmajor():
    quer="select * from CUSTOMER"
    cursor.execute(quer)
    majordata=cursor.fetchall()
    for i in majordata:
        print(i)

a=0
b=0
c=0
print("press one to add customer")
print("press 2 to show customer table")
print("press 3 to show room menu")
print("press 4 to update room menu")
print("press 5 to get total room rent")
print("press 6 to show recreation menu")
print("press 7 to get total recreation price")
print("press 8 to get restaurent menu")
print("press 9 to update restaurent menu")
print("press 10 to get total restaurent bill")
print("press 11 to get the whole record")
print("press 12 to get total bill")
print("press 13 to exit")
    
while True:
    choice=int(input("enter choice:"))
    if choice==1:
        addcustomer()
    elif choice ==2:
        showcustomers()
    elif choice==3:
        roommenu()
    elif choice==4:
        roomupdate()
    elif choice==5:
        b=(ro_om())
        print(b)
    elif choice==6:
        recreation()
    elif choice==7:
        a=(re_cr())
        print(a)
    elif choice==8:
        restmenu()
    elif choice==9:
        dishupdate()
    elif choice==10:
        c=(re_st())
        print(c)
    elif choice==11:
        makemajor()
        showmajor()
    elif choice==12:
        print(a+b+c)
    elif choice==13:
        break
    
    



'''
    qv="select CHECK_IN from customer_1"
    cursor.execute(qv)
    v=cursor.fetchall()
    vv=v[0]
    vvv=vv[0]
    qz="select CHECK_OUT from customer_1"
    cursor.execute(qz)
    z=cursor.fetchall()
    zz=z[0]
    zzz=zz[0]

    print(zz)
    qu="select C_ID from customer_1"
    cursor.execute(qu)
    u=cursor.fetchone()
    uu=u[0]
    
    qi="select NAME from customer_1"
    cursor.execute(qi)
    i=cursor.fetchall()
    ii=i[0]
    iii=ii[0]
'''










































        
    
