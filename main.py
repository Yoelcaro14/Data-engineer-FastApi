
from venv import create
from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
import json

app = FastAPI()

# **Carga de Datasets**

## Results
results= pd.read_json('C:/Users/yoe_1/Documents/Datasets/results.json',lines=True)
results1 = results.to_json()
resultsJson=json.loads(results1) 
## Drivers
drivers= pd.read_json('C:/Users/yoe_1/Documents/Datasets/drivers.json',lines=True) 
drivers= pd.concat([drivers.drop(['name'],axis=1), drivers['name'].apply(pd.Series)],axis=1) 
drivers1 = drivers.to_json()
driversJson=json.loads(drivers1) 
## Races
races= pd.read_csv('C:/Users/yoe_1/Documents/Datasets/races.csv')
races1 = races.to_json()
racesJson=json.loads(races1) 
## Constructors
constructors= pd.read_json('C:/Users/yoe_1/Documents/Datasets/constructors.json',lines=True)
constructors1 = constructors.to_json()
constructorsJson=json.loads(constructors1) 
## Circuits
circuits= pd.read_csv('C:/Users/yoe_1/Documents/Datasets/circuits.csv')
circuits1 = circuits.to_json()
circuitsJson=json.loads(circuits1) 

## Welcome
@app.get('/Portada')
def Welcome():
    return{'Bienvenido al Poryecto individual de ': 'Yoel Carocancha' }

# Documentacion
@app.get('/guia')
def Guia():
    return {    "/Portada": "welcome",
                "/guia" : 'Contenido',
                "/docs": "Documentación generada por FastAPI",
                "/Datasets/name": "Nombre de los Dataset a consultar",
                "/Datasets/{carga_datos}": "Datasets de trabajo",
                "/consigna1": "Año con más carreras",
                "/consigna2": "Piloto con mayor cantidad de primeros puestos",
                "/consigna3": "Nombre del circuito más corrido",
                "/consigna4": "Piloto con mayor cantidad de puntos totales con un constructor estadounidense o británico",
                }

## name datasets
@app.get('/Datasets/name')
def Datasets_name():
    return{'datasets':['results','drivers','races','constructors','circuits']}

## Estructura
@app.get('/Datasets/{carga_datos}')
def consultas_BD(carga_datos):
    if carga_datos == 'results':
        carga_datos = resultsJson
    if carga_datos == 'drivers':
        carga_datos = driversJson
    if carga_datos == 'races':
        carga_datos = racesJson
    if carga_datos == 'constructors':
        carga_datos = constructorsJson
    if carga_datos == 'circuits':
        carga_datos = circuitsJson
    
    return carga_datos


#Año con más carreras
@app.get('/consigna1')
def año_con_mas_carreras():
    ra=races.drop(['raceId','circuitId'],axis=1).groupby(['year']).sum().to_dict()['round']
    re=ra[max(ra)]
    for e in ra:
        if ra[e]== re:
            print (e)

    return {'Año con más carreras': e }


## Piloto con mayor cantidad de primeros puestos
@app.get('/consigna2')
def piloto_con_mayor_cantidad_de_primeros_puesto():
    results_position=results[results['positionOrder']==1].groupby(['driverId']).count()
    n=results_position[results_position['positionOrder']==results_position['positionOrder'].max()].index[0]

    return {'Piloto con mayor cantidad de primeros puestos': driversJson['forename'][f'{n-1}']+' '+ driversJson['surname'][f'{n-1}']}

# Nombre del circuito más corrido
@app.get('/consigna3')
def circuito_mas_recorrido():
    races_circuitId= races['circuitId'].value_counts()
    n_circuitId=races_circuitId[races_circuitId==races_circuitId.max()].index[0]
    mas_recorrido = circuits[circuits['circuitId']==n_circuitId].iloc[0,2]
    return {'Nombre del circuito más corrido': f'{mas_recorrido}'}

# Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
@app.get('/consigna4')
def Piloto_con_mayores_puntos():
    nacional=constructors[constructors['nationality']==('British'or'American')].drop(columns=['url','constructorRef'])
    filtrado= results[results['constructorId'].isin(nacional['constructorId'])]
    puntos=filtrado.groupby(filtrado['driverId']).sum()# id 6 y valor 9292.77
    puntos=puntos[puntos['points']==puntos['points'].max()].index[0]

    return {' Piloto de fabricante estadounidense o británico con más puntos': 
                driversJson['forename'][f'{puntos-1}']+' '+ driversJson['surname'][f'{puntos-1}']}