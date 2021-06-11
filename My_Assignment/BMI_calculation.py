import pandas as pd
import json
import os

def find_BMI(input_data_file, input_info_table, output_directory):
	#print("we are calculating BMI")
	
	df_json = pd.read_json(input_data_file)

	df_table = pd.read_csv(input_info_table)

	i = "BMI(kg/m\u00b2)"


	df_json[i] = round(df_json["WeightKg"]/((df_json["HeightCm"]/100)**2),2)

	j = df_table.columns[0]
	k = df_table.columns[1]
	m = df_table.columns[2]
	#df_json.loc[df_json[i] <= float(df_table[j][1]), k ] = df_table[k][1]

	#df.loc[df['column name'] condition, 'new column name'] = 'value if condition is met'
	
	df_json.loc[df_json[i] <=float(df_table[j][1]) , k] = df_table[k][0]
	df_json.loc[(df_json[i] > float(df_table[j][1])) & (df_json[i] <= float(df_table[j][2])) , k ] = df_table[k][1]
	df_json.loc[(df_json[i] > float(df_table[j][2])) & (df_json[i] <= float(df_table[j][3])) , k ] = df_table[k][2]
	df_json.loc[(df_json[i] > float(df_table[j][3])) & (df_json[i] <= float(df_table[j][4])) , k ] = df_table[k][3]
	df_json.loc[(df_json[i] > float(df_table[j][4])) & (df_json[i] <= float(df_table[j][5])) , k ] = df_table[k][4]
	df_json.loc[df_json[i] > float(df_table[j][4]) , k ] = df_table[k][5]


	df_json.loc[df_json[i] <=float(df_table[j][1]) , m ] = df_table[k][0]
	df_json.loc[(df_json[i] > float(df_table[j][1])) & (df_json[i] <= float(df_table[j][2])) , m ] = df_table[m][1]
	df_json.loc[(df_json[i] > float(df_table[j][2])) & (df_json[i] <= float(df_table[j][3])) , m ] = df_table[m][2]
	df_json.loc[(df_json[i] > float(df_table[j][3])) & (df_json[i] <= float(df_table[j][4])) , m ] = df_table[m][3]
	df_json.loc[(df_json[i] > float(df_table[j][4])) & (df_json[i] <= float(df_table[j][5])) , m ] = df_table[m][4]
	df_json.loc[df_json[i] > float(df_table[j][4]) , m ] = df_table[m][5]

	#print(df_json)

	#print("At start : ",os.getcwd())

	os.chdir(os.getcwd()+"/"+ output_directory)

	print("Output file is generated and stored at below location:")
	print(os.getcwd())

	df_json.to_csv('Output_file.csv')


