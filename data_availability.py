# -*- coding: utf-8 -*-
"""
Created on Wed May 18 17:16:33 2022

@author: rutuj
"""
        data = [[appoint_name, con_details, dept_data, date_det, time_det]]
        df = pd.DataFrame(data, columns = ['Name', 'Contact details','Division','Day','Time'])
        if not os.path.exists("Appointment.csv"):
            old_df = pd.DataFrame(columns = ['Name', 'Contact details','Division','Day','Time'])
        else:
            old_df = pd.read_csv("Appointment.csv")
           
        # old_df = pd.concat([old_df, df], ignore_index=True)
        
        data_date = datetime.datetime.fromisoformat(date_det[0])
        data_date = data_date.strftime("%d-%m-%Y")
        
        rslt_df = old_df[(old_df['Division'] == dept_data[0].strip()) & (old_df['Day'] == data_date )]

        print('-'*50)
        rslt_df['Time'] = rslt_df['Time'].str.strip()
        time_slot_list =  rslt_df['Time'].to_list()
        print(time_slot_list)
        print('-'*50)

        
        l2 = ['10.00 - 11.00', '11.00 - 12.00', '12.00 - 13.00', '13.00 - 14.00', '14.00 - 15.00', '15.00 - 16.00', '16.00 - 17.00', '17.00 - 18.00']
        l3 = [element for element in l2 if element not in time_slot_list] 
        
        if l3 == []:
            print("Select another date")
        else:
            string = 'Please select Time slot $'
        
            for i in l3:
                string = string + i + ', '
        
            print(string.rstrip(', '))
            shoeb_flag_1 = True
        print('-'*50)
