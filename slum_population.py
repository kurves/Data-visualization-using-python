# import the required libraries
import csv
from generate_code import get_country_code



filename= "API_EN.POP.SLUM.UR.ZS_DS2_en_csv_v2_5729134.csv"

with open(filename) as f:
    reader= csv.reader(f) 
    header_1=next(reader)
    header_2=next(reader)
    header_3=next(reader)
    header_4=next(reader)
    header_5=next(reader)
    #print(header_5)
   
    countries= []
    for row in reader:
        if any(row):
            
            countries.append(int(row[5]))
 
            print(countries)

    """population=[]
    for row in reader:
        
        population.append(row[5])
        print(population)"""


