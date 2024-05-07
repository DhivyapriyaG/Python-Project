class pa_det:
     def __init__(self,name,age,passid,password,status,bt,price,place,classes):
          self.name=name
          self.age=age
          self.passid=passid
          self.password=password
          self.status='not yet booked'
          self.bt=0
          self.price=price
          self.place=place
          self.classes=classes
     def show(self):
          print(self.name,'\t',self.age,'\t' ,self.passid,'\t' ,self.password,'\t' ,self.status,'\t' ,self.bt,'\t',self.place,'\t' ,self.classes)

class Book_det:
     def __init__(self):
          self.btickets=25
          self.etickets=75
          self.passid=1000
          self.l=[]

y=Book_det()

class b_list:     
     def __init__(self):
          self.L=[]
          self.sno=0

bl=b_list()

class Tic_det:
     def __init__(self):
          self.bticket_price=1000
          self.eticket_price=500
v=Tic_det()
        

def passenger():
    while True:
          print("\n-----------------------------------------------------------------------")
          print("\nMain Menu :")
          print("\n\t1.Sigup\n\t2.Signin\n\t3.Exit")
          n=int(input("\nEnter your choice:"))
          if n==1:
               print("\n-----------------------------------------------------------------------")
               print("\n\t\t      Welcome to SignUp Page")
               name=input("\nEnter your name     : ")
               age=int(input("Enter your age      : "))
               print("Your id is          :",y.passid)
               password=input('Enter your Password : ')
               status=0
               price=0
               bt=0
               place=0
               classes=0
               x=pa_det(name,age,y.passid,password,status,bt,price,place,classes)
               y.l.append(x)
               y.passid+=1
               print("\n\t\t    Signed Up Successfully..!")
          elif n==2:
               print("\n-----------------------------------------------------------------------")
               print("\n\t\t      Welcome to SignIn Page")
               i=int(input('\nEnter your ID       :'))
               m=input('Enter your password :')
               try:
                    if y.l[i-1000].passid==i and y.l[i-1000].password==m:
                         print("\n\t\t     Signed In Successfully..!")
                         print("\n-----------------------------------------------------------------------")
                         while True:
                              print("\nSelect Service :")
                              print("\n\t1.availability\n\t2.book tickets\n\t3.check status\n\t4.cancel tickets\n\t5.Print Bill\n\t6.LogOut")
                              nm=int(input("\nEnter your choice:"))
                              print("\n-----------------------------------------------------------------------")
                              if nm==2:
                                   print("\n\t\t     Welcome to BOOKING Page")
                                   place=input('\nWhich place to be booked                           : ')
                                   mn=int(input("Enter number of Tickets                            : "))
                                   while True:
                                        try:
                                             cl=input('Which class BUSINESS (Press 1) /ECONOMIC (Press 2) : ')
                                             if cl=='1':
                                                  classes='Business'
                                                  break
                                             elif cl=='2':
                                                  classes='Economic'
                                                  break
                                             else:
                                                  print("\n\t\t       Please Check Your Option..!\n")
                                        except ValueError:
                                             print('\n\t\t      Please Check your Option..!')
                                   if classes=='Business' and mn<=y.btickets:
                                        y.l[i-1000].bt=mn
                                        y.l[i-1000].status='pending'
                                        y.l[i-1000].place=place
                                        y.l[i-1000].classes=classes
                                        y.btickets-=mn
                                        y.l[i-1000].price=v.bticket_price * mn
                                        bl.L.append([y.l[i-1000].name,y.l[i-1000].passid,y.l[i-1000].place,y.l[i-1000].classes,y.l[i-1000].bt,y.l[i-1000].status,y.l[i-1000].price,bl.sno])
                                        bl.sno+=1
                                        print("\n\tTickets Booked Successfully..! Check Status!")
                                        print("\n-----------------------------------------------------------------------")
                                   elif classes=='Economic' and mn<=y.etickets:
                                        y.l[i-1000].bt=mn
                                        y.l[i-1000].status='pending'
                                        y.l[i-1000].place=place
                                        y.l[i-1000].classes=classes
                                        y.etickets-=mn
                                        y.l[i-1000].price=v.eticket_price * mn
                                        bl.L.append([y.l[i-1000].name,y.l[i-1000].passid,y.l[i-1000].place,y.l[i-1000].classes,y.l[i-1000].bt,y.l[i-1000].status,y.l[i-1000].price,bl.sno])
                                        bl.sno+=1
                                        print("\n\tTickets Booked Successfully..! Check Status!")
                                        print("\n-----------------------------------------------------------------------")
                                   else:
                                        print("\n\t\t     OOps!..Seats not available.")
                                        print("\n-----------------------------------------------------------------------")

                              elif nm==3:
                                   print("\nHistry :")
                                   print("\n Name         ID     Place           Class      Tic.Booked   Status            Price    S.Number")
                                   print(" -----------------------------------------------------------------------------------------------")
                                   if len(bl.L)>0:
                                        for j in range(len(bl.L)):
                                             if y.l[i-1000].name==bl.L[j][0]:
                                                  print(" %-10s   %-4d   %-13s   %-8s   %-10d   %-14s    %-6d   %-8d"%(bl.L[j][0],bl.L[j][1],bl.L[j][2],bl.L[j][3],bl.L[j][4],bl.L[j][5],bl.L[j][6],bl.L[j][7]))
                                   else:
                                        print("\n\t\t\t          No Records Found..!")
                                   print("\n -----------------------------------------------------------------------------------------------")
                                   print("\n-----------------------------------------------------------------------")

                              elif nm==4:
                                   print("\nCancelling Tickets :")
                                   print("\n Name         ID     Place           Class      Tic.Booked   Status            Price    S.Number")
                                   print(" -----------------------------------------------------------------------------------------------\n")
                                   if len(bl.L)>0:
                                        for j in range(len(bl.L)):
                                             if bl.L[j][5]=='approved' or bl.L[j][5]=='pending' and y.l[i-1000].name==bl.L[j][0]:
                                                  print(" %-10s   %-4d   %-13s   %-8s   %-10d   %-14s    %-6d   %-8d"%(bl.L[j][0],bl.L[j][1],bl.L[j][2],bl.L[j][3],bl.L[j][4],bl.L[j][5],bl.L[j][6],bl.L[j][7]))
                                   else:
                                        print("\n\t\t                  No Records Found..!")
                                   print("\n -----------------------------------------------------------------------------------------------")
                                   print("\n-----------------------------------------------------------------------")
                                   t=True
                                   if len(bl.L)>0:
                                        while (t==True):
                                             try:
                                                  sNo=int(input("\nEnter S.Number to be Cancelled : "))
                                                  if sNo>=0 and bl.L[sNo][5]=='approved' or bl.L[sNo][5]=='pending' and bl.L[sNo][0]==y.l[i-1000].name and bl.L[sNo][3]=='Business':
                                                       bl.L[sNo][5]='cancelled'
                                                       y.btickets+=bl.L[sNo][4]
                                                       print("\n\t\t    Tickets Cancelled Sucessfully..!")
                                                       print("\n-----------------------------------------------------------------------")
                                                       break
                                                  elif bl.L[sNo][5]=='approved' or bl.L[sNo][5]=='pending' and bl.L[sNo][0]==y.l[i-1000].name and bl.L[sNo][3]=='Economic':
                                                       bl.L[sNo][5]='cancelled'
                                                       y.etickets+=bl.L[sNo][4]
                                                       print("\n\t\t    Tickets Cancelled Successfully..!")
                                                       print("\n-----------------------------------------------------------------------")
                                                       break
                                                  else:
                                                       print("\n\t\t     Please check Your S.Number..!")
                                             except:
                                                  print("\n\t\t     Please check Your S.Number..!")
                                                  while True:
                                                       Opt=input("\nDo you want to CONTINUE (Press 1) or DROP (Press 2) the Process : ")
                                                       if Opt=='1':
                                                            print("\n-----------------------------------------------------------------------")
                                                            break
                                                       elif Opt=='2':
                                                            t=False
                                                            print("\n-----------------------------------------------------------------------")
                                                            break
                                                       else:
                                                            print("\n\t\t     Please check Your Option..!")
                                                            
                                                            
                              elif nm==6:
                                   print("\n\t\t   Logged Out Successfully...!")
                                   break
                              elif nm==5:
                                   tot=0
                                   print("\nBill Receipt :")
                                   print("\n\t Name         ID     Place           Class      Tic.Booked   Price")
                                   print("\t ------------------------------------------------------------------\n")
                                   if len(bl.L)>0:
                                        for j in range(len(bl.L)):
                                             if bl.L[j][0]==y.l[i-1000].name and bl.L[j][4]=='approved':
                                                  print(" %-10s   %-4d   %-13s   %-8s   %-10d   %-4d"%(bl.L[j][0],bl.L[j][1],bl.L[j][2],bl.L[j][3],bl.L[j][4],bl.L[j][6]))
                                                  tot+=bl.L[j][6]
                                   else:
                                        print("\n\t\t                 No Such Records Found..!")
                                   print("\n\t ------------------------------------------------------------------")
                                   print("\t                                                   Total $ =",tot)
                                   print("\t ------------------------------------------------------------------")
                              elif nm==1:
                                   print("\nAvailable tickets :")
                                   print("\n\t\t     Business Class :",y.btickets)
                                   print("\n\t\t     Economic Class :",y.etickets)
                                   print("\n-----------------------------------------------------------------------")
                    elif y.l[i-1000].passid!=i or y.l[i-1000].password!=m:
                         print('\n\t\tIncorrect Id or Password..!') 
               except IndexError:
                    print("\n\tID doesn't Exist...reCheck Entered ID..!\n\t\tOR SignUp Now...!")
              
          elif n==3:
               print("\n\t\t     VISIT AGAIN..THANK YOU...!")
               print("__________________________________***__________________________________")
               print("-----------------------------------------------------------------------")
               break
          else:
               print("\t\tEnter Valid Option..!")
def cashier():
     print("\n\t\t      Welcome To LOGIN Page")
     cash_Id=input('\nEnter Your Id       : ')
     cash_Pass=input('Enter Your Password : ')
     if cash_Id=='abcd' and cash_Pass=='1111':
          print("\n\t\t         LOGIN Successfull")
          print("\n-----------------------------------------------------------------------")
          while True:
               print("\nMain Menu :")
               print("\n\t1.show details\n\t2.approve tickets\n\t3.cancell tickets\n\t4.logout")
               n=int(input("\nEnter your choice:"))
               if n==1:
                    print("\n-----------------------------------------------------------------------")
                    print("\nBooked Ticket List :")
                    print("\n Name         ID     Place           Class      Tic.Booked   Status            Price    S.Number")
                    print(" -----------------------------------------------------------------------------------------------\n")
                    if len(bl.L)>0:
                         for j in range(len(bl.L)):
                              if bl.L[j][5]=='pending':
                                   print(" %-10s   %-4d   %-13s   %-8s   %-10d   %-14s    %-6d   %-8d"%(bl.L[j][0],bl.L[j][1],bl.L[j][2],bl.L[j][3],bl.L[j][4],bl.L[j][5],bl.L[j][6],bl.L[j][7]))
                              elif bl.L[j][5]=='cancelled':
                                   print(" %-10s   %-4d   %-13s   %-8s   %-10d   %-14s    %-6d   %-8d"%(bl.L[j][0],bl.L[j][1],bl.L[j][2],bl.L[j][3],bl.L[j][4],bl.L[j][5],bl.L[j][6],bl.L[j][7]))
                              elif bl.L[j][5]=='approved':
                                   print(" %-10s   %-4d   %-13s   %-8s   %-10d   %-14s    %-6d   %-8d"%(bl.L[j][0],bl.L[j][1],bl.L[j][2],bl.L[j][3],bl.L[j][4],bl.L[j][5],bl.L[j][6],bl.L[j][7]))
                    else:
                         print("\n\t\t      No Records Found..!")
                    print("\n ------------------------------------------------------------------------------------------------")

               elif n==2:
                    print("\n-----------------------------------------------------------------------")
                    print("\nApproving tickets : ")
                    print("\n Name         ID      Place          Class      Tic.Booked   Status              Price    S.Number")
                    print(" -------------------------------------------------------------------------------------------------")
                    if len(bl.L)>0:
                         for j in range(len(bl.L)):
                              if bl.L[j][5]=='pending':
                                   print("\n %-10s   %-4d    %-13s   %-10s   %-10d   %-15s    %-6d   %-8d"%(bl.L[j][0],bl.L[j][1],bl.L[j][2],bl.L[j][3],bl.L[j][4],bl.L[j][5],bl.L[j][6],bl.L[j][7]))
                    else:
                         print("\n\t\t      No Records Found..!")
                    print("\n -------------------------------------------------------------------------------------------------")

                    if len(bl.L)>0:
                         while True:
                              try:
                                   app=int(input("\nEnter S.Number to be APPROVED : "))
                                   ID=int(input("\nEnter ID to be APPROVED       : "))
                                   if app>=0 and bl.L[app][5]=='pending' and bl.L[app][1]==ID:
                                        if bl.L[app][3]=='Business' and bl.L[app][4]<=y.btickets:
                                             bl.L[app][5]='approved'
                                             print("\n\t\t        Tickets Approved ..!")
                                             break
                                        elif bl.L[app][3]=='Economic' and bl.L[app][4]<=y.etickets:
                                             bl.L[app][5]='approved'
                                             print("\n\t\t        Tickets Approved ..!")
                                             break
                                        else:
                                             print("\n\t\t  Tickets not Available.. Can't Approve..!")
                                             break
                                   else:
                                        print('\n\t\t     Please check Entered Details..!')
                              except:
                                   print('\n\t\t     Please check Entered Details..!')
                                   
               elif n==3:
                    print("\n-----------------------------------------------------------------------")
                    print("\n\t\tCancelling tickets : ")
                    print("\n Name         ID     Place           Class      Tic.Booked   Status            Price    S.Number")
                    print(" -----------------------------------------------------------------------------------------------")
                    if len(bl.L)>0:
                         for j in range(len(bl.L)):
                              if bl.L[j][5]=='pending':
                                   print("\n %-10s   %-4d    %-13s   %-10s   %-10d   %-15s    %-6d   %-8d"%(bl.L[j][0],bl.L[j][1],bl.L[j][2],bl.L[j][3],bl.L[j][4],bl.L[j][5],bl.L[j][6],bl.L[j][7]))
                    else:
                         print("\n\t\t                 No Records Found..!")
                    print("\n -----------------------------------------------------------------------------------------------")

                    while True:
                         try:
                              app=int(input("\nEnter S.Number to be CANCELLED : "))
                              ID=int(input("\nEnter ID to be CANCELLED       : "))
                              if app>=0 and bl.L[app][5]=='pending' and bl.L[app][1]==ID:
                                   if bl.L[app][3]=='Business':
                                        bl.L[app][5]='cancelled'
                                        y.btickets+=bl.L[app][4]
                                        print("\n\t\t        Tickets CANCELLED ..!")
                                        break
                                   elif bl.L[app][3]=='Economic':
                                        bl.L[app][5]='cancelled'
                                        y.etickets+=bl.L[app][4]
                                        print("\n\t\t        Tickets CANCELLED ..!")
                                        break
                              else:
                                   print('\n\t\t     Please check Entered details..!')
                         except:
                              print('\n\t\t     Please check Entered Details..!')
               elif n==4:
                    print("__________________________________***__________________________________")
                    print("-----------------------------------------------------------------------")
                    break

               else:
                   print("\t\tCheck Your Option.....!")
     else:
        print("\n\t\t      Something went Wrong..!")
        print("\t\t             Try Again..!")        

while True:
     print("\n\n\t\t****....Welcome to AIRBHARAT....****")
     print("-----------------------------------------------------------------------")
     print("\nLOGIN as :")
     print("\n\t1.PASSANGER\n\t2.CASHIER\n\t3.Exit")
     try:
          n=int(input("\nEnter your choice:"))
          if n==1:
               passenger()
          elif n==2:
               print("\n-----------------------------------------------------------------------")
               cashier()
          elif n==3:
               print("\n\t   ........ THANKS FOR USING OUR SERVICE .......\n\t\t        ......VISIT AGAIN......")
               print("\n\t                           ***")
               break
          else:
               print("\n\t\tPlease check your entered Option\n\t\t      Enter valid Option..!")
     except ValueError:
         print("\n\t\tPlease check your entered Option\n\t\t      Enter valid Option..!")

