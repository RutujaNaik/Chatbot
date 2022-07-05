import datetime
import pandas as pd
import os
Flag=0
# df1=pd.read_csv("Appointment_of_DR.csv")



# Division=(df1['Answer'][8])
# Day=df1['Answer'][9]
# Time=df1['Answer'][10]


def CSV_Generation(appoint_name, con_details, dept_data, date_det, time_det):
    data = [[appoint_name, con_details, dept_data, date_det, time_det]]
    df = pd.DataFrame(data, columns = ['Name', 'Contact details','Division','Day','Time'])
    
    if not os.path.exists("Appointment.csv"):
        old_df = pd.DataFrame(columns = ['Name', 'Contact details','Division','Day','Time'])
    else:
        old_df = pd.read_csv("Appointment.csv")
    
    old_df = pd.concat([old_df, df], ignore_index=True)

 
    old_df.to_csv("Appointment.csv",index=False)
    
def CSV_Fetching(dept_data,date_det):
    if not os.path.exists("Appointment.csv"):
        old_df = pd.DataFrame(columns = ['Name', 'Contact details','Division','Day','Time'])
    else:
        old_df = pd.read_csv("Appointment.csv")
       
    # old_df = pd.concat([old_df, df], ignore_index=True)
    
    data_date = datetime.datetime.fromisoformat(date_det)
    data_date = data_date.strftime("%d-%m-%Y")
    
    rslt_df = old_df[(old_df['Division'] == dept_data) & (old_df['Day'] == data_date )]

    print('-'*50)
    rslt_df['Time'] = rslt_df['Time'].str.strip()
    time_slot_list =  rslt_df['Time'].to_list()
    

    
    l2 = ['10.00 - 11.00', '11.00 - 12.00', '12.00 - 13.00', '13.00 - 14.00', '14.00 - 15.00', '15.00 - 16.00', '16.00 - 17.00', '17.00 - 18.00']
    l3 = [element for element in l2 if element not in time_slot_list]       
    return l3, data_date

# CSV_Generation('xcvb', '45678', 'Cardiologist', '2022-05-17', '12.00 - 13.00')
#CSV_Fetching('xcvb', '45678', 'Cardiologist', '2022-05-17', '12.00 - 13.00')

   


