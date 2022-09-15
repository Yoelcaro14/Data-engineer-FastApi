# Proyecto Individual 1 - Data engineer
  *By:* **Yoel A. Carocancha Armas**

## Creación de una API

En el presente proyecto se crea y ejecuta un API. Para ello, se trabaja con un conjunto de Datasets de distintos formatos los cuales 
son normalizados y analizados para garantizar su calidad. Asi mismo, se hace uso del framework **FastAPI** para el desarrollo del proyecto. 

Una vez normalizado el dataset se crea una serie de consultas a la **API**, las cuales son:

* Año con más carreras
* Piloto con mayor cantidad de primeros puestos
* Nombre del circuito más corrido
* Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British

## Guia de consultas en la **API**

**http://localhost:8000/Portada** :  "welcome"
  **1** "/guia" : 'Contenido'
  "/docs": "Documentación generada por FastAPI",
  "/Datasets/name": "Nombre de los Dataset a consultar",
  "/Datasets/{carga_datos}": "Datasets de trabajo",
  "/consigna1": "Año con más carreras",
  "/consigna2": "Piloto con mayor cantidad de primeros puestos",
  "/consigna3": "Nombre del circuito más corrido",
  "/consigna4": "Piloto con mayor cantidad de puntos totales con un constructor estadounidense o británico",
