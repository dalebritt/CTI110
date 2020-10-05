input_month = input() 
input_day = int(input())
if input_month in ('January', 'February', 'March','April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December',):
    if (input_day < 32) and (input_day > 0):
        
        
        if input_month in ('March', 'April', 'May', 'June'):
            if (input_month == 'March') and (input_day > 19):
                print('Spring')
            if input_month == 'April':
                print ('Spring')
            if input_month == 'May':
                print('Spring')
            elif (input_month == 'June') and (input_day <= 20):
                print('Spring')   


        if input_month in ('June', 'July', 'August', 'Septempter'):
            if (input_month == 'June') and (input_day > 20):
                print('Summer')
            if input_month == 'July':
                print('Summer')
            if input_month == 'August':
                print('Summer')
            elif (input_month == 'September') and (input_day <= 21):
                print('Summer')
      
        if input_month in ('September', 'October', 'November', 'December'):
            if (input_month == 'September'):
                
                if input_day > 30:
                    print('Invalid')   
                elif input_day > 21:
                    print('Autumn')
                    
        
            if input_month == 'October':
                print('Autumn')
            if input_month == 'November':
                print('Autumn')
            elif (input_month == 'December') and (input_day <= 20):
                print('Autumn')
            
        if input_month in ('December', 'January', 'February', 'March'):
            if (input_month == 'December') and (input_day > 20):
                print('Winter')
            if input_month == 'January':
                print('Winter')
            if input_month == 'February':
                print('Winter')
            elif (input_month == 'March') and (input_day <= 19):
                print('Winter')  
    else:
        print('Invalid')
   
else:
      print('Invalid')

