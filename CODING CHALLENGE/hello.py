import pandas as pd
from datetime import datetime
time_in = []
time_out = [] 
for i in range(8,23):
    time_in.append(str(i) +":00")
    time_out.append(str(i) +":30")

# for x in time_out:
#     print(x)
    


df_myName = pd.DataFrame({
    'Time in': time_in,
    'Time out': time_out
    

})
writer = pd.ExcelWriter("nameee.xlsx",datetime="hh:mm",sheet_name="Ako",index=False)
df_myName.to_excel(writer)
writer.close()
