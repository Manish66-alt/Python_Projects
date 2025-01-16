import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="knmanish",database="cims")
mycursor=mydb.cursor()
updata=None

def add():
   while True:
       idno=0
       pname=input("Enter the PROPERTY NAME :")
       ptype=input("Enter the PROPERTY TYPE :")
       postype=input("Enter POSSESSION TYPE(PRIVATE/PUBLIC):").lower()
       mycursor.execute("select count(*) from region"+str(ch))
       mrec=mycursor.fetchone()
       idno+=mrec[0]
       idno+=1
       
       if (postype == 'private') or (postype =='public'):
                     pass
       else:
             print("ENTER A VALID DATA!")
             break
       idno='R'+str(ch)+str(idno)
       prop=input("ENTER PROPRIETOR:")
       mycursor.execute("insert into region"+str(ch)+" values('{}','{}','{}','{}','{}')" .format(idno,pname,ptype,postype,prop))
       mydb.commit()
       conch=input("Would you like to continue adding records?(y/n):")
       if conch.lower() == 'n':
           mycursor.close()
           print("DATA ADDED SUCCESSFULLY!")
           break
       
def remove():
   while True:
       idno=input("Enter the ID.NO of the property to be removed:")
       mycursor.execute("DELETE from region"+str(ch)+" where ID_no = '{}'".format(idno))
       conch=input("Would you like to continue removing records?(y/n)")
       mydb.commit()
       if conch.lower() == 'n':
           mycursor.close()
           print("DATA REMOVED SUCCESSFULLY!")
           break
def update():
       while True:
          idno=input("Enter the ID.NO of the property to be Updated:")
          upch=int(input('''
          1.Property name
          2.property type
          3.possesssion type
          4.proprietor
          Enter which of the following data should be updated(1/2/3/4):''' ))
          if upch==1:
              updata="Property_Name"
              newdat=input("Enter the new data to be updated=")
          elif ch==2:
              updata="Property_Type"
              newdat=input("Enter the new data to be updated=")
          elif ch==3:
              updata="Possession_Type"
              newdat=input("Enter the new data to be updated=")
          elif ch==4:
              updata="Proprietor"
              newdat=input("Enter the new data to be updated=")
              
          mycursor.execute("UPDATE region"+str(ch)+" set "+updata+"= '{}' where ID_no='{}'".format(newdat,idno))
          mydb.commit()
          conch=input("Would you like to continue updating records?(y/n):")
          if conch.lower() == 'n':
              mycursor.close()
              print("DATA UPDATED SUCCESSFULLY!")
              break
          
def search():
    ID_nostr="ID_no"
    pnamestr="Property_Name"
    propstr="Proprietor"
    ptypestr="Property_Type"
    postypestr="Possession_Type"
  
    
    
    sch1=int(input('''
    1.Search using ID_no
    2.Search using Property name
    3.search using proprietor
    4.search using Property type
    5.Search using Possession type

    Enter your choice(1/2/3/4/5):'''))
    
    sch2=int(input('''
       1.Search using ID_no
       2.Search using Property name
       3.search using proprietor
       4.search using Property type
       5.Search using Possession type
       6.PASS the second criteria

       Enter another choice That you would like to use for searching(1/2/3/4):'''))
    if sch1==sch2:
        print("Both chosen criteria are the same....Try again")
        
    if sch2 ==6:
      if sch1 ==1:
           idno=input("Enter ID_no to search:")
           mycursor.execute("select * from region"+str(ch)+" where ID_no ='{}'".format(idno))
           rec=mycursor.fetchall()
           for i in rec:
               print(i)
      elif sch1==2:
           pname=input("Enter the name of the property to search:")
           mycursor.execute("select * from region"+str(ch)+" where  Property_Name ='{}'".format(pname))
           rec=mycursor.fetchall()
           for i in rec:
               print(i)
      elif sch1==3:
           prop=input("Enter proprietor to search:")
           mycursor.execute("select * from region"+str(ch)+" where Proprietor ='{}'".format(prop))
           rec=mycursor.fetchall()
           for i in rec:
               print(i)
      elif sch1==4:
           ptype=input("Enter the type of property to search:")
           mycursor.execute("select * from region"+str(ch)+" where Property_Type  ='{}'".format(ptype))
           rec=mycursor.fetchall()
           for i in rec:
               print(i)
      elif sch1==5:
           postype=input("Enter the type of possession to search:")
           mycursor.execute("select * from region"+str(ch)+" where Possession_Type='{}'".format(postype))
           rec=mycursor.fetchall()
           for i in rec:
               print(i)
      else:
             print("Enter a valid input!")
             search()
             
    if sch2 !=6: 
        crit=input(''' You have entered two search criteria. Would you like to search for results that match:

                      Both criteria (AND) —  return results that match all of your conditions.
                      Either criteria (OR) — return results that match any of your conditions.
         
                    Your choice(AND/OR):''')
    if sch1 == 1:
         c1=ID_nostr
         idno=input("Enter ID_no to search:")
         d1=idno
    elif sch1==2:
         c1=pnamestr
         pname=input("Enter the name of the property to search:")
         d1=pname
    elif sch1 ==3:
          c1=propstr
          prop=input("Enter proprietor to search:")
          d1=prop
    elif sch1 ==4:
          c1=ptypestr
          ptype=input("Enter the type of property to search:")
          d1=ptype
    elif sch1 ==5:
          c1=postypestr
          postype=input("Enter the type of possession to search:")
          d1=postype
          
    if sch2==1:
        c2=ID_nostr
        idno=input("Enter ID_no to search:")
        d2=idno
    elif sch2==2:
        c2=pnamestr
        pname=input("Enter the name of the property to search:")
        d2=pname
    elif sch2==3:
        c2=propstr
        prop=input("Enter proprietor to search:")
        d2=prop
    elif sch2==4:
        c2=ptypestr
        ptype=input("Enter the type of property to search:")
        d2=ptype
    elif sch2==5:
        c2=postypestr
        postype=input("Enter the type of possession to search:")
        d2=postype
          
    if crit.lower() == "and":
            mycursor.execute("select * from region"+str(ch)+" where '{}'='{}' and '{}'='{}'".format(c1,d1,c2,d2))
            rec=mycursor.fetchall()
            if rec == None:
                 print("No records found!")     
            for i in rec:
               print(i)
    elif crit.lower() == "or":
            mycursor.execute("select * from region"+str(ch)+" where '{}'='{}' or '{}'='{}'".format(c1,d1,c2,d2))
            rec=mycursor.fetchall()
            if rec == None:
                 print("No records found!")
            for i in rec:
               print(i)
    else:
          print("Enter a valid input!")
          
   
print("--"*90)
print("\n______________________________COMMUNITY INFRASTRUCTURE MANAGEMENT SYSTEM______________________________")
print("\n                                              DATABASE")
print('\n')
ch=int(input('''
1.REGION-1
2.REGION-2
3.REGION-3
                    
ENTER THE REGION:'''))
rnch="REGION"+str(ch)
print(rnch)
print('\n')
ch2=int(input('''
1.ADD ENTITY
2.REMOVE ENTITY
3.UPDATE ENTITY
4.SEARCH ENTITY


ENTER THE OPERATION TYPE(1/2/3/4/5):'''))
if ch2==1:
       add()
elif ch2==2:
       remove()
elif ch2 == 3:
       update()
elif ch2 == 4:
      search()
    
print('\n')
