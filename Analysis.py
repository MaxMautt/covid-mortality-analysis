import pandas as pd

df = pd.read_excel('data/Provisional_COVID-19_Deaths_by_Sex_and_Age_20260317.xlsx')
#Dejar solo los datos por año, por sexo y por grupo de edad
df=df[df['Group']=='By Year']
df=df[df['Sex']!='All Sexes']
df=df[df['Age Group']!='All Ages']

#Utilizar grupos de edad que no se solapen 
df=df[df['Age Group'].isin(['Under 1 year', '1-4 years', '5-14 years', '15-24 years',
    '25-34 years', '35-44 years', '45-54 years', '55-64 years',
    '65-74 years', '75-84 years', '85 years and over'])]
#Convertir años a entero
df['Year'] = df['Year'].astype(int)

#Seleccionamos las columnas necesarias para el análisis

df = df[['Year', 'State', 'Sex', 'Age Group', 'COVID-19 Deaths', 'Total Deaths', 'Pneumonia Deaths', 'Influenza Deaths']]

#Contamos la cantidad de nulos
# print(df.isnull().sum())
#Se usa la extensión Data Wrangler para visualizar los datos y comprobar los errores faltantes y duplicados

#Se rellenan los datos faltantes con 0
df=df.fillna(0)

#ANALISIS 1. MUERTES DE COVID POR EDAD Y SEXO
#Utilizar solo los datos nacionales
us=df[df['State']=='United States']

#Filtrar las muertes por covid en funcion del sexo y de la edad
m1=us.groupby(['Sex','Age Group'])['COVID-19 Deaths'].sum()

df.to_csv('data/covid_limpio.csv', index=False)