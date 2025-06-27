
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

def Conteo_años(data: dict,years: list): #Cuenta la cantidad de sismos ocurridos en una lista de años dada
    count=0
    for i in years:
        count+=data[f"{i}"]["total"]
    return count
def Top_Sismos(data): #retorna una lista con los totales de sismos por año
    lista=[]
    for i in data.keys():
        if data[i]["total"] is not None:
            lista.append(data[i]["total"])
    lista.sort()
    return lista
def Top_Quake(data): #retorna una lista con el maximo de magnitud por año
    lista=[]
    for i in data.keys():
        if data[i]["terremoto_principal"]["magnitud"] is not None:
            lista.append(data[i]["terremoto_principal"]["magnitud"])
    lista.sort()
    return lista
def Top_ZAS(data): #retorna una lista con el total de sismos de las Zonas de Actividad Sísmica  por año
    lista=[]
    for i in data.keys():
        if data[i]["zona_activa"]["cantidad"] is not None:
            lista.append(data[i]["zona_activa"]["cantidad"])
    lista.sort()
    return lista
def sismos_mensualidad(data, year): #Grafica el numero de sismos de cada mes dado un año
    lista = [] #lista que almacena listas con los meses y el numero de sismos correspondiente para cada año
    for i in data[year]["meses"].keys():
        lista.append([i, data[year]["meses"][i]["total"]])
    
    dt = pd.DataFrame(lista, columns=["Mes", "total"]) #construccion del dataframe
    fig = px.histogram(dt, x="Mes", y="total",
                title=f"Sismos mensuales - Año {year}",
                labels={"total": "Número de sismos", "Mes": "Mes del año"})

  
    # Personalización adicional del gráfico
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray')
    )
    
    return fig
    
def evolucion_mensual_por_zona(data,year): #Grafica el comportamiento de las Zonas de Actividd Sismica a lo largo de los meses en un año segun la cantidad
    datos_zonas = [] #lista que almacena listas con los meses, nombre de la ZAS, y la cantidad de sismos reportados 
    for i in data[year]["meses"].keys():
        for j in data[year]["meses"][i]["zonas"].keys():
            datos_zonas.append([i,j,data[year]["meses"][i]["zonas"][j]["cantidad"]])
        
    
    df_zonas = pd.DataFrame(datos_zonas,columns=["Meses","Zona","Cantidad"])

    # Crear el gráfico
    fig = px.line(
        df_zonas,
        x='Meses',
        y='Cantidad',
        color='Zona',
        title=f'Evolución Mensual de Actividad Sísmica por Zona - Año {year}',
        markers=True,
        labels={'cantidad': 'Número de sismos', 'mes': 'Mes', 'zona': 'Zona sísmica'}
    )
    
    # Personalización adicional
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
        hovermode='x unified'
    )
    return fig
def evolucion_mensual_días(data,year): #Grafica la evolucion a lo largo de los meses de los dias mas activos de un año
    datos_dias=[]

    for i in data[year]["meses"].keys():
        if data[year]["meses"][i]["dia_activo"]["fecha"] is not None:
            datos_dias.append([data[year]["meses"][i]["dia_activo"]["fecha"],data[year]["meses"][i]["dia_activo"]["cantidad"]])
    df=pd.DataFrame(datos_dias,columns=["Fecha","Cantidad"])
    
    fig = px.line(
        df,
        x='Fecha',
        y='Cantidad',
        title=f'Evolución Mensual de Días con mayor actividad - Año {year}',
        markers=True,
        labels={'cantidad': 'Número de sismos', 'mes': 'Mes', 'zona': 'Zona sísmica'}
    )
    
    # Personalización adicional
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
        hovermode='x unified'
    )
    return fig
def perceptibles_df(data): #Construye un dataframe con toda la informacion de los sismos perceptibles
    dataframe={
    "localidad":[],
    "fecha":[],
    "hora":[],
    "ln":[],
    "lw":[],
    "profundidad":[],
    "magnitud":[],
    "region":[],
    "provincia":[]   
    }
    for i in data.keys():
        for j in range(len(data[i]["perceptibles"]["magnitudes_perceptibles"])):
            dataframe["localidad"].append(data[i]["perceptibles"]["magnitudes_perceptibles"][j]["localidad"])
            dataframe["fecha"].append(data[i]["perceptibles"]["magnitudes_perceptibles"][j]["fecha"])
            dataframe["hora"].append(data[i]["perceptibles"]["magnitudes_perceptibles"][j]["hora"])
            dataframe["ln"].append(data[i]["perceptibles"]["magnitudes_perceptibles"][j]["lw"])
            dataframe["lw"].append(data[i]["perceptibles"]["magnitudes_perceptibles"][j]["profundidad"])
            dataframe["profundidad"].append(data[i]["perceptibles"]["magnitudes_perceptibles"][j]["profundidad"])
            dataframe["magnitud"].append(data[i]["perceptibles"]["magnitudes_perceptibles"][j]["magnitud"])
            dataframe["region"].append(data[i]["perceptibles"]["magnitudes_perceptibles"][j]["region"])
            dataframe["provincia"].append(data[i]["perceptibles"]["magnitudes_perceptibles"][j]["provincia"])
    
    df=pd.DataFrame(dataframe)
    df['fecha'] = pd.to_datetime(df['fecha'])
    df['año'] = df['fecha'].dt.year
    df['año'] = pd.to_numeric(df['año'], errors='coerce').astype('Int64')
    df['mes_nombre'] = df['fecha'].dt.month_name(locale='es')
    return df

def month_analize(data,year,month): #retorna una tupla con (dia mas activo, cantidad de sismos de ese dia, zona mas activa, cantidad de sismos de dicha zona, zona mas energetica, y un grafico de pastel) dado un mes y año especifico
    dia=data[year]["meses"][month]["dia_activo"]["fecha"]
    cantidad=data[year]["meses"][month]["dia_activo"]["cantidad"]
    zona_activa=data[year]["meses"][month]["zona_activa"]["nombre"]
    cantidad_activa=data[year]["meses"][month]["zona_activa"]["cantidad"]
    zona=data[year]["meses"][month]["zona_energetica"]
    lista=[]
    for i in data[year]["meses"][month]["zonas"].keys():
        lista.append([i,data[year]["meses"][month]["zonas"][i]["cantidad"]])
    df=pd.DataFrame(lista,columns=["Zonas","Cantidad"])
    fig = px.pie( #grafico de pastel con la distribución de la cantidad de sismos por zonas en ese mes
        df,
        values="Cantidad",
        names="Zonas",
        title=f'Distribución de zonas en {month} del {year}',
    )

    return (dia,cantidad,zona_activa,cantidad_activa,zona,fig)

def Top_zonas(data): #Grafica las zonas con mayor actividad sismica en total
    datos_zonas = []
    for año, info in data.items():
        if 'zonas' in info:
            for zona, detalle in info['zonas'].items():
                detalle['zona'] = zona
                detalle['año'] = año
                datos_zonas.append(detalle)
                
    df_zonas = pd.DataFrame(datos_zonas)

    top_zonas = df_zonas.groupby('zona')['cantidad'].sum().nlargest(10).reset_index()
    fig_top_zonas = px.bar(
        top_zonas,
        x='zona',
        y='cantidad',
        title='Top 10 zonas con Mas Actividad Sismica',
        color='cantidad',
        color_continuous_scale='Viridis'
    )
    return fig_top_zonas

def magnitud_anual(data): #grafica boxplots sobre las magnitudes de los sismos por cada año
    eventos = []
    for año, info in data.items():
        for evento in info['perceptibles']['magnitudes_perceptibles']:
            evento['año'] = año
            eventos.append(evento)
        
    df = pd.DataFrame(eventos)
    df['fecha'] = pd.to_datetime(df['fecha'])
    fig_magnitud_anual = px.box(
    df,
    x='año',
    y='magnitud',
    title='Distribucion de Magnitudes por Año',
    color='año',
    points='all'
    )
    return fig_magnitud_anual
with open("anuales.json","r",encoding='utf-8') as file:
    data=json.load(file)

print(perceptibles_df(data))



def sismos_mensualidad_2024(data):
    lista = []
    year = "2024"
    for i in data[year]["meses"].keys():
        lista.append([i, data[year]["meses"][i]["total"]])
    
    dt = pd.DataFrame(lista, columns=["Mes", "total"])
    fig = px.bar(dt, x="Mes", y="total",
                title="Sismos mensuales - Año 2024",
                labels={"total": "Número de sismos", "Mes": "Mes del año"})
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray')
    )
    return fig

def evolucion_mensual_por_zona_2024(data):
    datos_zonas = []
    year = "2024"
    for i in data[year]["meses"].keys():
        for j in data[year]["meses"][i]["zonas"].keys():
            datos_zonas.append([i,j,data[year]["meses"][i]["zonas"][j]["cantidad"]])
    
    df_zonas = pd.DataFrame(datos_zonas,columns=["Meses","Zona","Cantidad"])

    fig = px.line(
        df_zonas,
        x='Meses',
        y='Cantidad',
        color='Zona',
        title='Evolución Mensual de Actividad Sísmica por Zona - Año 2024',
        markers=True,
        labels={'Cantidad': 'Número de sismos', 'Meses': 'Mes', 'Zona': 'Zona sísmica'}
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
        hovermode='x unified'
    )
    return fig

def evolucion_mensual_días_2024(data):
    datos_dias=[]
    year = "2024"
    
    for i in data[year]["meses"].keys():
        if data[year]["meses"][i]["dia_activo"]["fecha"] is not None:
            datos_dias.append([data[year]["meses"][i]["dia_activo"]["fecha"],
                             data[year]["meses"][i]["dia_activo"]["cantidad"]])
    
    df=pd.DataFrame(datos_dias,columns=["Fecha","Cantidad"])
    
    fig = px.line(
        df,
        x='Fecha',
        y='Cantidad',
        title='Evolución Mensual de Días con mayor actividad - Año 2024',
        markers=True,
        labels={'Cantidad': 'Número de sismos', 'Fecha': 'Fecha'}
    )
    
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='lightgray'),
        hovermode='x unified'
    )
    return fig