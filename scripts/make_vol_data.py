

# import pandas as pd

# data = pd.read_csv("arc_od.csv")
# data = data.drop_duplicates(subset="Facility Latitude_x",keep="first",inplace=False)

# data.to_csv("compressed_arc.csv",index=False,sep=",")

lat_data_file = open("tol1.csv")
lat_data_file.readline()

loc_json = open("vol_data.json", 'w')
loc_json.write('{\n\t"AllData": \n\t[ \n\t\t{\n\t\t"Year": 2019, \n\t\t"Data": \n\t\t\t[\n')

first = True

for line in lat_data_file:
    if not first:
        loc_json.write(",\n")
    else:
        first = False
    line_data = line.strip().split(',')
    # print (line_data)
    loc_json.write("\t\t\t\"" + line_data[1] + "\", \"" + line_data[2] +
     "\", \""  + line_data[3] + "\", \"" + line_data[5] + "\", \"" + line_data[7] + 
     "\", \"" + line_data[8] + "\", \"" + line_data[6] + "\"")

loc_json.write('\n\t\t\t]\n\t\t}\n\t]\n}')
loc_json.close()

lat_data_file.close()
