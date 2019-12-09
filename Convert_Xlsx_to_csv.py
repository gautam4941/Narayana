import pandas as pd

def convert_xlsx_to_csv( path1, path2 ):
    book1xlsx = pd.read_excel( path1 )
    col = book1xlsx.columns
    
    data = []
    for i in range( len( book1xlsx.index ) ):
        temp = []

        for j in col:
            temp.append( book1xlsx[j][i] )

        data.append( temp )

    pd.DataFrame( data ).to_csv( path2 )

    
path1 = r"Excel Data/Book1.xlsx"
path2 = r"Excel Data/Converted_csv.csv"
convert_xlsx_to_csv( path1, path2 )
