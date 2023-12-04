from os import system, name
import time
import mysql.connector
db1 = mysql.connector.connect(
	  host='localhost',
	  user='root',
	  passwd='',
      database='personal_fin'
	)

c1=db1.cursor()
def mainmenu():
    print("Enter 1 for add transaction")
    print("Enter 2 for edit transaction")
    print("Enter 3 for delete transaction")
    print("Enter 4 for list transaction")
    print("Enter 5 for Adding New Acccounts")
    print("Enter 6 for  All Balances")
    print("Enter 7 for List of Transactions")
    option=int(input("Enter the type of transcation : "))
    
    match option:
        case 1:
            add_trans()
        case 2:
            edit_trans()
        case 3:
            del_trans()
        case 4:
            list_trans()
        case 5:
            add_account()
        case 6:
            list_all_bal()
        case 7:
            lst_all_trans()
        case _:
            print("Error, enter the correct option...")
            time.sleep(1)
            exit_fun()
           
            
def add_trans():
    print("Enter ai to add income")
    print("Enter ae to add expense")
    print("Enter at to add transfer")
    option1 = input("Enter the type of add transcation : ")
    match option1:
        case "ai":
            add_income()
        case "ae":
            add_expense()
        case "at":
            add_transfer()
        case _:
            print("Error...")
    
def add_income():
    print("Enter the target account number given below : ")
    print("Add income Transcation : ")  
    a1=int(input("Enter the target acc number : "))
    if acc_list(a1):  
        print("Account number exists")
    else:
        print("Enter Valid Account Number")
        add_income()
    a2=int(input("Enter the amount : "))
    a3=input("Enter the description : ")
    
              
    c2=db1.cursor()   
     
    my1 = "SELECT balance FROM accounts WHERE acc_no= %s"
    res1=(a1, )
    c2.execute(my1,res1)
    myr1 = c2.fetchall()
    for ait in myr1:
        print(ait)
        bal = ait[0]
    balance1 = bal + a2
    sql = "INSERT INTO transactions (target_acc, amount, description, category) VALUES (%s, %s, %s, %s)"
    val = (a1, a2, a3,"ADD_INCOME")
    c2.execute(sql,val)
    db1.commit()
    
    aitsql = "update accounts set balance = %s where acc_no = %s "
    aitval = (balance1, a1)
    c2.execute(aitsql, aitval)
    c2.close()
    db1.commit()
    mainmenu()
    
def add_expense():
    print("Enter the source account number given below : ")
    print("Add expense Transaction : ")
    a11=int(input("Enter the source acc number : "))
    if acc_list(a11):  
        print("Account number exists")
    else:
        print("Enter Valid Account Number")
        add_expense()
    a21=int(input("Enter the amount : "))
    a31=input("Enter the description : ")
    
    c3=db1.cursor()
    
    my2 = "SELECT balance FROM accounts WHERE acc_no=%s"
    res2 = (a11, )
    c3.execute(my2, res2)
    myr2 = c3.fetchall()
    for aet in myr2:
        #print(aet)
        bal2 = aet[0]
    balance2 = bal2 - a11    
    
    sql1 = "INSERT INTO transactions (source_acc, amount, description, category) VALUES (%s, %s, %s, %s)"
    val1 = (a11, a21, a31,"ADD_EXPENSE")
    c3.execute(sql1,val1)
    #db1.commit()
    #mainmenu()
    
    aetsql = "update accounts set balance = %s where acc_no = %s "
    aetval = (balance2, a11)
    c3.execute(aetsql, aetval)
    c3.close()
    db1.commit()
    mainmenu()
        
def add_transfer():
    print("Enter the target and source account number given below : ")
    acc_list()
    print("Add transfer Transaction : ")  
    a12=int(input("Enter the target acc number : "))
    if acc_list(a12):  
        print("Account number exists")
    else:
        print("Enter Valid Target Account Number")
        add_transfer()
    a22=int(input("Enter the source acc number : "))
    if acc_list(a22):  
        print("Account number exists")
    else:
        print("Enter Valid Source Account Number")
        add_transfer()
    a32=int(input("Enter the amount : "))
    a42=input("Enter the description : ")
   
    c4=db1.cursor()
    
    my3 = "SELECT balance FROM accounts WHERE acc_no=%s"
    res3 = (a12, )
    c4.execute(my3,res3)
    myr3 = c4.fetchall()
    for att in myr3:
        #print(att)
        bal3 = att[0]
    balance3 = bal3 + a12
    
    my31 = "SELECT balance FROM accounts WHERE acc_no=%s"
    res31 = (a22, )
    c4.execute(my31,res31)
    myr31 = c4.fetchall()
    for att in myr31:
        #print(att)
        bal3 = att[0]
    balance3 = bal3 - a22
    
    sql2 = "INSERT INTO transactions (target_acc,source_acc, amount, description, category) VALUES (%s, %s, %s, %s, %s)"
    val2 = (a12, a22, a32,a42, "ADD_TRANSFER")
    c1.execute(sql2,val2)
    #db1.commit()
    #mainmenu()
    
    attsql1 = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
    attval1 = (balance3, a12)
    c4.execute(attsql1, attval1)
    
    attsql2 = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
    attval2 = (balance3, a22)
    c4.execute(attsql2, attval2)
    
    c4.close()
    db1.commit()
    mainmenu()

def edit_trans():
    print("Enter ei to edit income")
    print("Enter ee to edit expense")
    print("Enter et to edit transfer")
    option2 = input("Enter the type of edit transaction : ")
    match option2:
        case "ei":
            edit_income()
        case "ee":
            edit_expense()
        case "et":
            edit_transfer()
        case _:
            print("Error...")  
    
def edit_income():

    c5 = db1.cursor()
    
    print("Edit income transcation : ")
    #e1=int(input("Enter the target acc number : "))
    e2=int(input("Enter the transaction id : "))
    e3 = int(input("Enter the amount : "))
    #e4 = input("Enter the description : ")
    #sql4 = "UPDATE transactions SET target_acc = %s, amount=%s, description=%s WHERE id = %s"
    #val4 = (e2, e3, e4)
    #c5.execute(sql4, val4)
    #db1.commit()
    #mainmenu()
    
    my4 = "SELECT * FROM transactions WHERE id = %s"
    res4 = (e2, )
    c5.execute(my4,res4)
    myr4 = c5.fetchall()
    for eit in myr4:
        print(eit)
        oldamount1 = eit[4] 
        target_acc1 = eit[1]
    
    accbal1 = "SELECT balance FROM accounts WHERE acc_no = %s"
    accval1 = (target_acc1, ) 
    c5.execute(accbal1,accval1)
    myr5 = c5.fetchall()
    for acc_balance in myr5:
        print(acc_balance)
        
    eitsql = "UPDATE transactions SET amount = %s WHERE id = %s"
    eitval = (e3, e2)
    c5.execute(eitsql,eitval)
    
    newbalance1 = acc_balance[0] - oldamount1 + e3
      
    editsql1 = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
    editval1 = (newbalance1, target_acc1 )
    c5.execute(editsql1, editval1)
    c5.close()
    db1.commit()
    mainmenu()
                                                     
def edit_expense():
    print("Edit expense transcation : ") 
    #e11=int(input("Enter the source acc number : "))
    e21=int(input("Enter the amount : "))
    #e31=input("Enter the description : ")
    e41=int(input("Enter id : "))
    
    c6 = db1.cursor()
    
    #sql5 = "UPDATE transactions SET source_acc= %s, amount= %s, description=%s WHERE id= %s"
    #val5 = (e11, e21, e31, e41)
    #c6.execute(sql5,val5)
    
    my5 = "SELECT * FROM transactions WHERE id = %s"
    res5 = (e41, )
    c6.execute(my5, res5)
    myr6 = c6.fetchall()
    for eet in myr6:
        print(eet)
        oldamount2 = eet[4]
        source_acc1 = eet[2]
        
    accbal2 = "SELECT balance FROM accounts WHERE acc_no =%s"    
    accval2 = (source_acc1, )
    c6.execute(accbal2,accval2)
    myr7 = c6.fetchall()
    for acc_balance2 in myr7:
        print(acc_balance2)
        
    eetsql = "UPDATE transactions SET amount = %s WHERE id = %s"   
    eetval = (e21, e41)    
    c6.execute(eetsql,eetval)
    
    newbalance2 = acc_balance2[0] + oldamount2 - e21
    
    editsql2 = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
    editval2 = (newbalance2, source_acc1)
    c6.execute(editsql2, editval2)
    c6.close()    
    db1.commit()
    mainmenu()

def edit_transfer():
    print("Edit transfer transcation : ") 
    #e12=int(input("Enter the target acc number : "))
    #e22=int(input("Enter the source acc number : "))
    e32=int(input("Enter the amount : "))
    #e42=input("Enter the description : ")
    e52=int(input("Enter id : "))
    
    c7 = db1.cursor()
    
    #sql6 = "UPDATE transactions SET target_acc=%s, source_acc=%s, amount=%s,description=%s WHERE id=%s"
    #val6 = (e12, e22, e32,e42,e52 )
    #c1.execute(sql6,val6)
    
    my6 = "SELECT * FROM transactions WHERE id = %s"
    res6 = (e52, )
    c7.execute(my6, res6)
    myr8 = c7.fetchall()
    for ett in myr8:
        print(ett)
        oldamount3 = ett[4]
        target_acc2 = ett[1]
        source_acc2 = ett[2]
    
    accbal3 = "SELECT balance FROM accounts WHERE acc_no =%s"    
    accval3 = (target_acc2, )
    c7.execute(accbal3,accval3)
    myr9 = c7.fetchall()
    for acc_balance3 in myr9:
        print(acc_balance3)
        
    accbal4 = "SELECT balance FROM accounts WHERE acc_no =%s"    
    accval4 = (source_acc2, )
    c7.execute(accbal4,accval4)
    myr10 = c7.fetchall()
    for acc_balance4 in myr10:
        print(acc_balance4)    
        
    ettsql = "UPDATE transactions SET amount = %s WHERE id = %s"   
    ettval = (e32, e52)    
    c7.execute(ettsql,ettval)    
    
    newbalance3 = acc_balance3[0] - oldamount3 + e32
    
    newbalance4 = acc_balance4[0] + oldamount3 - e32
    
    editsql3 = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
    editval3 = (newbalance3, target_acc2)
    c7.execute(editsql3, editval3)
    
    editsql4 = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
    editval4 = (newbalance4, source_acc2)
    c7.execute(editsql4, editval4)
    c7.close()        
    db1.commit()
    mainmenu()

    
def del_trans():
    print("Enter di to delete income")
    print("Enter de to delete expense")
    print("Enter dt to delete transfer")
    option3 = input("Enter the type of delete transcation : ")
    match option3:
        case "di":
            del_income()
        case "de":
            del_expense()
        case "dt":
            del_transfer()
        case _:
            print("Error...")
            
def del_income():

    print("Delete income Transcation : ")
    lst_all_trans()  
    c8 = db1.cursor()  
    d1=int(input("Enter id : "))
    ditsql1 = "SELECT * FROM transactions WHERE id =%s"  
    ditval1 = (d1, )
    c8.execute(ditsql1,ditval1)
    myr11 = c8.fetchall()
    for di1 in myr11:
        print(di1)
        target_acc3 = di1[1]
        print(target_acc3)
        oldamount4 = di1[4]
        
    ditsql2 = "SELECT balance FROM accounts WHERE acc_no =%s"    
    ditval2 = (target_acc3, ) 
    c8.execute(ditsql2,ditval2)  
    myr12 = c8.fetchall()
    for di2 in myr12:
        print(di2)
        
    sql7= "DELETE FROM transactions WHERE id =%s "
    val7 = [d1]
    c8.execute(sql7, val7)
    
    newbalance5 = di2[0] - oldamount4  
    
    ditsql3 = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
    ditval3 = (newbalance5,target_acc3 )
    c8.execute(ditsql3,ditval3)
    c8.close()
    db1.commit()
    mainmenu()            
    
def del_expense(): 
    print("Delete expense transcation : ") 
    lst_all_trans() 
    #d11=int(input("Enter the source acc number : "))
    #d21=int(input("Enter the amount : "))
    #d31=input("Enter the description : ")
    d41 = int(input("Enter id : "))
    #sql8 = "INSERT INTO transactions (source_acc, amount, description, category) VALUES (%s, %s, %s, %s)"
    #val8 = (d11, d21, d31,"EDIT_EXPENSE")
    #c1.execute(sql8,val8)
    
    c9 = db1.cursor()
    detsql1 = "SELECT * FROM transactions WHERE id =%s"  
    detval1 = (d41, )
    c9.execute(detsql1,detval1)
    myr13 = c9.fetchall()
    for de1 in myr13:
        print(de1)
        source_acc3 = de1[1]
        oldamount5 = de1[4]
    
    detsql2 = "SELECT balance FROM accounts WHERE acc_no =%s"    
    detval2 = (source_acc3, ) 
    c9.execute(detsql2,detval2)  
    myr14 = c9.fetchall()
    for de2 in myr14:
        print(de2)
        
    sql14= "DELETE FROM transactions WHERE id =%s "
    val14 = [d41]
    c9.execute(sql14, val14)

    newbalance6 = de2[0] + oldamount5

    detsql3 = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
    detval3 = (newbalance6,source_acc3 )
    c9.execute(detsql3,detval3)
    c9.close()
    db1.commit()
    mainmenu()      
    
def del_transfer():
    lst_all_trans() 
    print("Delete transfer transcation : ") 
    #d12=int(input("Enter the target acc number : "))
    #d22=int(input("Enter the source acc number : "))
    #d32=int(input("Enter the amount : "))
    #d42=input("Enter the description : ")
    d52=int(input("Enter id : "))
   
    #sql9 = "INSERT INTO transactions (target_acc,source_acc, amount, description, category) VALUES (%s, %s, %s, %s, %s)"
    #val9 = (d12, d22, d32, d42, "EDIT_TRANSFER")
    #c1.execute(sql9,val9)
    #db1.commit()
    #mainmenu()    
    
    c11 = db1.cursor()
    
    dttsql1 = "SELECT * FROM transactions WHERE id =%s"  
    dttval1 = (d52, )
    c11.execute(dttsql1,dttval1)
    myr15 = c11.fetchall()
    for dt1 in myr15:
        print(dt1)
        target_acc4 = dt1[1]
        source_acc4 = dt1[2]
        oldamount6 = dt1[4]
        
    dttsql2 = "SELECT balance FROM accounts WHERE acc_no =%s"    
    dttval2 = (target_acc4, ) 
    c11.execute(dttsql2,dttval2)  
    myr16 = c11.fetchall()
    for dt2 in myr16:
        print(dt2)    
    
    dttsql3 = "SELECT balance FROM accounts WHERE acc_no =%s"    
    dttval3 = (source_acc4, ) 
    c11.execute(dttsql3,dttval3)  
    myr17 = c11.fetchall()
    for dt3 in myr17:
        print(dt3) 
    
    sql15 = "DELETE FROM transactions WHERE id =%s "
    val15 = [d52]
    c11.execute(sql15, val15)
    
    newbalance7 = dt2[0] - oldamount6
    newbalance8 = dt3[0] + oldamount6
    
    dttsql4 = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
    dttval4 = (newbalance7, target_acc4)
    c11.execute(dttsql4,dttval4)
    
    dttsql5 = "UPDATE accounts SET balance = %s WHERE acc_no = %s"
    dttval5 = (newbalance7,source_acc4)
    c11.execute(dttsql5,dttval5)
 
    c11.close()
    db1.commit()
    mainmenu()  
    
 
def list_trans():
    print("Enter li to list income")
    print("Enter le to list expense")
    print("Enter lt to list transfer")
    option4 = input("Enter the type of list transcation : ")
    match option4:
        case "li":
            lst_income()
        case "le":
            lst_expense()
        case "lt":
            lst_transfer()
        case _:
            print("Error...")

def lst_income():
    print("List income Transcation : ") 
    l1=int(input("Enter the target acc number : "))
    l2=int(input("Enter the amount : "))
    l3=input("Enter the description : ")
   
    sql10 = "INSERT INTO transactions (target_acc, amount, description, category) VALUES (%s, %s, %s, %s)"
    val10 = (l1, l2, l3,"LIST_INCOME")
    c1.execute(sql10,val10)
    db1.commit()
    mainmenu()
    
def lst_expense():
    print("List expense transcation : ") 
    l11=int(input("Enter the source acc number : "))
    l21=int(input("Enter the amount : "))
    l31=input("Enter the description : ")
   
    sql11 = "INSERT INTO transactions (source_acc, amount, description, category) VALUES (%s, %s, %s, %s)"
    val11 = (l11, l21, l31,"LIST_EXPENSE")
    c1.execute(sql11,val11)
    db1.commit()
    mainmenu()
    
def lst_transfer():
    print("List transfer transcation : ") 
    l12=int(input("Enter the target acc number : "))
    l22=int(input("Enter the source acc number : "))
    l32=int(input("Enter the amount : "))
    l42=input("Enter the description : ")
   
    sql12 = "INSERT INTO transactions (target_acc, source_acc, amount, description, category) VALUES (%s, %s, %s, %s, %s)"
    val12 = (l12, l22, l32, l42, "LIST_TRANSFER")
    c1.execute(sql12,val12)
    db1.commit()
    mainmenu()
        

def add_account():

    c12 = db1.cursor()
    
    print ("Add Your Account Details Here ")
    ano = int(input("Enter Account Number : "))
    aname = input("Enter Name of Account : ")
    abal = int(input("Enter the Initial Balance : "))
    
    add_acc_sql = "INSERT INTO accounts (acc_no,acc_name,balance) VALUES (%s,%s,%s)"
    add_acc_val = (ano,aname,abal)
    c12.execute(add_acc_sql,add_acc_val)
    c12.close()
    db1.commit()
    mainmenu()
   
def lst_all_trans():
    
    c10=db1.cursor()
    lstsql= "SELECT * FROM transactions"
    c10.execute(lstsql)
    mylst = c10.fetchall()
    for lst in mylst:
        print(lst)
    c10.close()
    db1.commit()
    
def list_all_bal():
    
    sql13= "SELECT * FROM accounts"
    c1.execute(sql13)
    myresult= c1.fetchall()
    for x in myresult:
        print("Account No: ",x[1], " Balance is - ", x[3])
    db1.commit() 

def acc_list(c):
    x = []
    z = c
    c13 = db1.cursor()
    acc_list_sql = "SELECT acc_no FROM accounts "
    c13.execute(acc_list_sql)
    myr18  = c13.fetchall()
    for acc_lst in myr18:
        #print(acc_lst[0])
        x.append(acc_lst[0])
        #print(type(acc_lst[0]))
    #print(x)  
    #y= x.len()
    
    # if a1 == x:
    #     print("Proceed")
    # else:
    #     return False   
     
    if z in x:
        print("Account number exists")
        return True
    
        

def exit_fun():
    exit()
    
    
def clearall():
    if name == 'nt':
        _=system('cls')
        
    else:
        _=system('clear')
  
    
mainmenu()    









    
