import datetime
import pandas as pd


def CSV_Generation(First_name,Middle_Name,Last_Name,Division,Day,Time):
    data = [[First_name,Middle_Name,Last_Name,Division,Day,Time]]

    df = pd.DataFrame(data, columns = ['Name', 'Middle Name','Last_Name','Division','Day','Time'])
 
    df.to_csv("Appointment.csv",index=False,mode='a',header=False)
    
def CSV_Fetching(Division,Day,Time):
    Division=str(Division)
    Day=str(Day)
    df=pd.read_csv("Appointment.csv")
   
    Flag=0
    #print(df['Name'])
    for i in range(len(df)):
        if Division in str(df['Division'][i]):
            if Day in str(df['Day'][i]):
            
            
                if Time in str(df['Time'][i]):
                    Flag=1
                    break
                else:
                    print("Not")
        
    return Flag
 
def timing():
    


    Current_Date = datetime. date. today()
    Day_after_tomorrow=datetime. date. today() + datetime. timedelta(days=2)
    Tomorrow = datetime. date. today() + datetime. timedelta(days=1)
    

    time1 = {
        "1": "10 Am - 11 Am",
        "2": "11 Am - 12 Pm",
        "3": "1 Pm - 2 Pm",
        "4": "2 Pm - 3 Pm",
        "5": "3 Pm - 4 Pm",
        "6": "4 Pm - 5 Pm",
        "7": "5 Pm - 6 Pm",
        "8": "6 Pm - 7 Pm"
    }
   
    print("choose your time for today:")
    print(time1)
    t = input("select your time:")
    x = time1[t]
    return x

 
def Cardiology():
    Division='Cardiology'
    print("Please,Select Day From Below On Which You Want to Book Appointment")
    print("Today")
    print("Tomorrow")
    print("Day After Tomorrow")
    #print("4,back")
    Day = int(input("Enter the Appointment Date"))
    Time=timing()
    print("TIminf ss",Time)
    iret=CSV_Fetching(Division, Day, Time)
    if iret:
        print("Sorry You Can't Book Apointment")
    elif iret==0:
        print("You Can Book")
        First_name=input("Enter Your Name")
        Middle_Name=input("Enter Your Middle Name")
        Last_Name=input("Enter Last Name")
        
        
        
    #print("Your Booking is Successfull for Day "+x)
        CSV_Generation(First_name,Middle_Name,Last_Name,Division,Day,Time)
        print("Your Booking is Successfull for Day ")
    return 0

def Neurology():
    print("Please,Select Day From Below On Which You Want to Book Appointment")
    print("Today")
    print("Tomorrow")
    print("Day After Tomorrow")
    #print("4,back")
    a = int(input("choose your option: "))
   # Day(a,'Neurology')
    return 0
def Gynecologist():
    print("Please,Select Day From Below On Which You Want to Book Appointment")
    print("Today")
    print("Tomorrow")
    print("Day After Tomorrow")
    #print("4,back")
    a = int(input("choose your option: "))
   # Day(a,'Gynecologist')
    return 0

def Appointment():
    print("Welcome To Appointment Booking")
    print("Which Department You Want to Book Department")
    print("Cardiology")
    print("Neurology")
    print("Gynecologist")
    place = int(input("choose your option: "))
    if place == 1:
      Cardiology()
    elif place == 2:
      Neurology()
    elif place == 3:
      Gynecologist()
    else:
      print("wrong choice")
 
 
Appointment()