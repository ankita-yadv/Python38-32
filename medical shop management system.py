
def menu2():
    print("----------------------MEDICINE SECTION----------------------------------")
    import mysql.connector as mycon
    mycon = mycon.connect(host='localhost',
                          user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
    cur = mycon.cursor()
    print('''\t\t\t 1-insert medicine details
                    2-delete a medicine
                    3-update a medicine
                    4-search a medicine''')
    
    x = int(input("enter choice:"))

    if x == 1:
        id = input("enter id:")
        name = input("enter name:")
        batchnumber = input("enter batchnumber:")
        manu_date = input("enter manufacture date:")
        import_date = input("enter import date:")
        expire_date = input("enter expiry date:")
        manufacture = input("enter manufacuter:")
        typ_e = input("enter the type (ml,strip,vial or tube:")
        med_unit = input("enter no. of medicine unit in stock:")
        med_cost = input("enter amount of one n unit of the medicine:")
        st = f'''insert into product values(
        '{id}','{name}','{batchnumber}','{manu_date}','{import_date}',
        '{expire_date}','{manufacture}','{typ_e}','{med_unit}','{med_cost}')'''
        cur.execute(st)
        mycon.commit()

    elif x == 2:
        from datetime import date
        dat = date.today()
        import mysql.connector as mycon
        mycon =mycon.connect(host='localhost',
                             user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
        cur = mycon.cursor()
        cur.execute("select expire_date from product")
        res = cur.fetchall()
        de = 0
        sd=str(dat)
        for x in res:
            print("the expiry dates are:",x[0])
            if str(x[0]) == sd:
                delt = f"delete from product where expire_date = '{sd}' "
                cur.execute(delt)
                mycon.commit()
                print(res)
            else:
                pass
    elif x == 3:
        import mysql.connector as mycon
        mycon =mycon.connect(host='localhost',
                             user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
        cur = mycon.cursor()
        b = input("enter field to input:")
        c = input("enter id of record to update:")
        d = input("enter new record:")
        upd = "update product set "+b+" = "+d+" where id = "+c
        cur.execute(upd)
        mycon.commit()
    elif x == 4:
        import mysql.connector as mycon
        mycon =mycon.connect(host='localhost',
                             user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
        cur = mycon.cursor()
        s = input("name of medicine to search:")
        cur.execute(f"select * from product where name = '{s}'")
        res = cur.fetchall()
        for i in res:
            print(i)
        else:
            print("invalid choice:")



def menu3():
    print("---------------------------SALES ENTRY SECTION------------------------------")
    import mysql.connector as mycon
    mycon =mycon.connect(host='localhost',
                         user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
    cur = mycon.cursor()
    
    print('''\t\t\t 1-insert sales detail
    2-delete sales detail
    3-update sales detail
    4-search sales detail''')

    x = int(input("enter coice:"))
    if x == 1:
        i_d = input("enter id:")
        order_date = input("enter date:")
        user_id = input("enter user id:")
        paymentmode = input("enter payment mode(cash,cheque):")
        amt_paid = input("enter amount paid:")
        unit_sold = input("enter no. of units sold:")
        med_name = input("enter medicine name:")
        sa = f"insert into salesvalues('{i_d}','{order_date}','{user_id}','{paymentmode}','{amt_paid}','{unit_sold}','{med_name}')"
        cur.execute(sa)
        mycon.commit()
    elif x == 2:
        a = input("enter field name:")
        b = input("enter record to delete:")
        det = f"delete from sales where '{a}' = '{b}'"
        cur.execute(det)
        mycon.commit()
    elif x == 3:
        import mysql.connector as mycon
        mycon =mycon.connect(host='localhost',
                             user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
        cur = mycon.cursor()
        b = input("enter field to input:")
        c = input("enter id of record to update:")
        d = input("enter new record:")
        upd = f"update sales set '{b}' = '{d}' where id = '{c}'"
        cur.execute(upd)
        mycon.commit()
    elif x == 4:
        import mysql.connector as mycon
        mycon =mycon.connect(host='localhost',
                             user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
        cur = mycon.cursor()
        s = input("enter no of units sold to search:")
        cur.execute(f"select * from sales where unit_sold = '{s}'")
        res = cur.fetchall()
        for i in res:
            print(i)
        else:
            print("invalid choice:")



def menu4():
    print("---------------------------------PURCHASE SECTION-----------------------------")
    import mysql.connector as mycon
    mycon =mycon.connect(host='localhost',
                         user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
    cur = mycon.cursor()
    
    print('''\t\t\t 1-insert purchase detail
                    2-delete purchase detail
                    3-update purchase detail
                    4-search purchase detail''')

    x = int(input("enter coice:"))
    
    if x == 1:
        i_d = input("enter customer id:")
        name = input("enter name:")
        address = input("enter address:")
        contact_details = input("enter phone number:")
        typ_e = input("enter mode of payment(regular or occasional):")
        med_name = input("enter med name:")
        se = f"insert into customervalues('{i_d}','{name}','{address}','{contact_details}','{typ_e}','{med_name}')"
        cur.execute(se)
        mycon.commit()

    elif x == 2:
        a = input("enter field name:")
        b = input("enter record to delete:")
        det = f"delete from customer where '{a}' = '{b}'"
        cur.execute(det)
        mycon.commit()

    elif x == 3:
        import mysql.connector as mycon
        mycon =mycon.connect(host='localhost',
                             user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
        cur = mycon.cursor()
        b = input("enter field to input:")
        c = input("enter id of record to update:")
        d = input("enter new record:")
        upd = f"update customer set '{b}' = '{d}' where id = '{c}'"
        cur.execute(upd)
        mycon.commit()

    elif x == 4:
        import mysql.connector as mycon
        mycon =mycon.connect(host='localhost',
                             user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
        cur = mycon.cursor()
        s = input("enter name of customer to search:")
        cur.execute("select * from customer where name = '"+s+"'")
        res = cur.fetchall()
        for i in res:
            print(i)
        else:
            print("invalid choice:")

def menu5():
    print("----------------------------------REPORT/BILL SECTION------------------------------")
    import mysql.connector as mycon
    mycon =mycon.connect(host='localhost',
                         user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
    cur = mycon.cursor()
    from datetime import date
    dat = date.today()
    print('''\t\t\t 1-med report
                    2-sales report
                    3-purchase report
                    4-bill
                    5-new bill''')
    x = int(input("enter coice 1-4:"))

    if x==1:
        print('*'*100)
        print('\t\tMedicine List')
        print('='*70)
        print("{0:^15}{1:^20}{2:^20}{3:^15}".format('id','Medicine-Name','Batchnumber','Type of Medicine'))
        s1=("select * from product")
        cur.execute(s1)
        for(id,name,batchnumber,manufacturedate,import_date,expire_date,manufacturer,type,medicine_unit,medicine_cost) in cur:
            print("{0:^15}{1:^20}{2:^20}{3:^15}".format(id,name,batchnumber,type))

    elif x==2:
        s1=("select * from sales")
        cur.execute(s1)
        for(id,order_date,pay_date,user_id,paymentmode,amt_paid,unit_sold,med_name) in cur:
            print("{0:^15}{1:^20}{2:^20}{3:^15}".format(id,med_name,paymentmode,unit_sold))

    elif x==3:
        s1=("select * from customer")
        cur.execute(s1)
        for (id,name,address,contact_detail,type,med_name) in cur:
            print("{0:^15}{1:^20}{2:^20}{3:^15}{4:^20}".format(id,med_name,type,name,contact_details))

    elif x==4:
        import mysql.connector as mycon
        mycon =mycon.connect(host='localhost',
                           user='ankit',
                          passwd='ankit',
                          database='medic',
                          auth_plugin='mysql_native_password')
        b = int(input("enter no. of medicines bought:"))
        for i in range(0,b):
            cur = mycon.cursor()
            print("enter values for the bill:")
            i_d = input("enter id:")
            pay_mode = input("enter payment mode(cash or net:")
            med_name = input("enter med name:")
            quantity = input("enter quantity of med bought:")
            price = input("enter the price:")
            sf = f"insert into billvalues('{i_d}','{pay_mode}','{med_name}','{quantity}','{price}')"
            cur.execute(sf)
            mycon.commit()
            print('*'*100)
            print('\t\t{}'.format("MEDICAL SHOP"))
            print('\t\t{}'.format("Dadupur"))
            print('\t\t{}'.format("Contact No.- 8295289223"))
            print('\t\t{}'.format(dat))
            print("=" * 70)
            print("{0:^15}{1:^20}{2:^20}{3:^15}{4:^20}".format('bill_id','Medicine-Name','payment_mode','price','quantity'))
            print('-'*100)
            s1 = ("select * from bill")
            cur.execute(s1)
            Total_Cost=0
            for (id,pay_mode,med_name,quantity,price) in cur:
                print("{0:^15}{1:^20}{2:^20}{3:^15}{4:^20}".format(id,med_name,pay_mode,price,quantity))
                Total_Cost+= price*quantity
                print('-'*100)
                print('Total Cost\t\t\t\t\t\t\t=\t\t{}'.format(Total_Cost))
                print('-'*100)
                print('\t\t\tThank you for shopping with us')
                print('-' * 100)
                print('\n')
                print('*' * 100)
    elif x==5:
        cur.execute("truncate table bill")
        mycon.commit()
        print("bill cleared")



def menu6():
    print("---------------------------REFUND------------------------------")
    import mysql.connector as mycon
    
    mycon =mycon.connect(host='localhost',
                         user='ankit',
                         passwd='ankit',
                         database='medic',auth_plugin='mysql_native_password')
    
    cur = mycon.cursor()
    
    x = input('enter name of med:')
    y = int(input('enter no. of med returned:'))
    a = f"select medicine_cost from product where name = '{x}'"
    
    cur.execute(a)
    b = cur.fetchall()
    for i in b:
        print("The amount to be payed back =",i[0]*y)



x = True
 
while x == True:
    print("")
    print("------------------------MEDICAL STORE----------------------------")
    print("select {1} - Medicine section ")
    print("select {2} - sales section ")
    print("select {3} - purchase section ")
    print("select {4} - report/bill section ")
    print("select {5} - refund")
    print("select {6} - exit")
    print("-"*70)
     
    option = int(input("\nenter from choices {1-5} ="))
     
    if option == 1:
        menu2()
    elif option == 2:
        menu3()
    elif option == 3:
        menu4()
    elif option == 4:
        menu5()
    elif option == 5:
        menu6()
    elif option == 6:
        print("-"*50,"Thank you","-"*50)
        x = False
    
    else:
        print("Invalid choice, choose between 1 and 5")

    
    
