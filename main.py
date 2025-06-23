import streamlit as st
import analysis as mylib
import json
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np


#Carga el archivo JSON
with open("anuales.json","r",encoding='utf-8')as file:
    data=json.load(file)

#configura los detalles de la página
st.set_page_config(
    page_title="GeodataCuba",
    page_icon="🌋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Todo el CSS que hace bonita la página :D
st.markdown("""
<style>
    /* Fuentes bonitas para que se vea profesional */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Source+Sans+3:wght@300;400;600&display=swap');
    
    /* Los colores principales que elegimos */
    :root {
        --primary: #6B352C;
        --primary-dark: #5a2b24;
        --primary-light: #8B4513;
        --light-bg: #f8f5f2;
        --card-bg: #ffffff;
    }
    
    /* Estilo general de texto */
    * {
        font-family: 'Source Sans 3', sans-serif;
    }
    
    /* Títulos con otra fuente */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif;
        color: var(--primary);
    }
    
    body {
        background-color: var(--light-bg);
    }
    
    /* Barra lateral con color */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--primary) 0%, var(--primary-dark) 100%);
        color: white;
        padding: 1.5rem 1rem;
    }
    
    .sidebar-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 2rem;
    }
    
    .sidebar-item {
        padding: 0.8rem 1rem;
        border-radius: 6px;
        margin-bottom: 0.5rem;
        cursor: pointer;
    }
    
    .sidebar-item:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    .sidebar-item.active {
        background-color: rgba(255, 255, 255, 0.15);
        font-weight: 600;
    }
    
    /* Contenedor principal */
    .main-container {
        padding: 2rem 3rem;
    }
    
    /* Tarjetas que se ven modernas */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2.5rem;
    }
    
    .card {
        background-color: var(--card-bg);
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(107, 53, 44, 0.1);
        overflow: hidden;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(107, 53, 44, 0.15);
    }
    
    .card-header {
        background: linear-gradient(90deg, var(--primary) 0%, var(--primary-light) 100%);
        color: white;
        padding: 1.2rem;
    }
    
    .card-body {
        padding: 1.5rem;
    }
    
    /* Estadísticas grandes */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2.5rem;
    }
    
    .stat-card {
        background-color: var(--card-bg);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }
    
    .stat-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--primary);
    }
    
    /* Tabla con estilo */
    .data-table {
        width: 100%;
        border-collapse: collapse;
        background-color: var(--card-bg);
        border-radius: 10px;
        overflow: hidden;
    }
    
    .data-table th {
        background-color: var(--primary);
        color: white;
        padding: 1rem;
    }
    
    .data-table td {
        padding: 0.9rem 1rem;
        border-bottom: 1px solid #eeeeee;
    }
    
    .data-table tr:hover td {
        background-color: #f9f5f2;
    }
    
    /* Pie de página */
    .app-footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        color: #777777;
        border-top: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)
#Título
st.title("GeoDataCuba: Cuando los Datos Cuentan la Historia de la Tierra")

col1,col2,col3=st.columns([1,2,1])
with col2:
    st.image("Extra/1.png",use_container_width=True)

def main_app():
    # Barra lateral con menú
    with st.sidebar:
        st.image("Extra/GeoData.png",use_container_width=True)        
        # Menú para navegar
        st.sidebar.markdown("## 📖 Índice ")
        st.sidebar.markdown("- [Inicio](#Inicio)")
        st.sidebar.markdown("- [Datos](#datos)")
        st.sidebar.markdown("- [Gráficos](#graficos)")   
        st.sidebar.markdown("- [Conclusiones](#conclusiones)")

        st.markdown('<div class="sidebar-item"><span>🗺️</span> Mapas</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-item"><span>📉</span> Gráficos</div>', unsafe_allow_html=True)
        
        st.markdown('<div style="margin-bottom:1.5rem"><div style="font-size:1.1rem; margin-bottom:0.8rem">📚 Datos</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-item"><span>💾</span> Importar</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-item"><span>🔍</span> Explorar</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-item"><span>📋</span> Tablas</div>', unsafe_allow_html=True)
        
        st.markdown('<div style="margin-bottom:1.5rem"><div style="font-size:1.1rem; margin-bottom:0.8rem">⚙️ Sistema</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-item"><span>🔒</span> Seguridad</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-item"><span>🛠️</span> Configuración</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-item"><span>❓</span> Ayuda</div>', unsafe_allow_html=True)
        
        # Estado del sistema
        st.markdown("---")
        st.markdown("**Estado del sistema:**")
        st.markdown("🟢 Base de datos activa")
        st.markdown("🟢 Información Actualizada")
        st.markdown("**Versión:** 1.0.0")
        
    
        
    
    # Secciones con IDs
    #Región Inicio
    st.markdown("<a id='Inicio'></a>", unsafe_allow_html=True)
    st.header("Inicio🏃",)
    st.markdown('''
    <p style="font-size:17px; font-weight:bold; color:black;">
        <i>
            ¿Sabían que Cuba se mueve constantemente?. Y no hablamos metafóricamente, literalmente.
            Cada día nuestra isla registra micro-terremotos que dibujan un mapa invisible de fuerzas geológicas increíbles<br>
            En los últimos 5 años:
        </i>
    </p>
''', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="stat-card">
            <div>Eventos totales</div>
            <div class="stat-value">{mylib.Conteo_años(data,[2024,2023,2022,2021,2020])}</div>
            <div>↑ {mylib.Conteo_años(data,[2024,2023,2022,2021,2020])-mylib.Conteo_años(data,[2019,2018,2017,2016,2015])} del último período</div>
        </div>""", unsafe_allow_html=True)
    
    st.markdown('''
    <p style="font-size:17px; font-weight:bold; color:black;">
        <i>
            Cada día son registrados patrones fascinantes escondidos en números🤓, algunos bastante inusuales...🤔.
            Un sinfín de historias geológicas esperando a ser descubiertas.<br>
            Nosotros construimos la llave para descifrar  esas historias. Se llama:
        </i>
    </p>
''', unsafe_allow_html=True)
    #Introducción
    col1,col2,col3=st.columns([1,2,1])
    with col2:
        st.image("Extra/GeoData.png")
        st.markdown('<p style="font-family: sans-serif;font-size: 20px;font-weight: bold;"><i style="color:rgb(0,87,214);">GeoDataCuba:</i> <l style= "color:rgb(0,33,66);">Cuando la tierra tiembla, los datos hablan...</l></p>', unsafe_allow_html=True)

    # Tarjetas de información
    st.markdown('<div class="card-grid">', unsafe_allow_html=True)
    
    # Tarjeta de fuentes de datos 
    st.markdown("""
        <div class="card">
            <div class="card-header">
                <h3><span>📡</span> Fuentes de Datos</h3>
            </div>
            <div class="card-body">
                <p>Trabajamos con información pública extraída de:</p>
                <ul>
                    <li>Centro Nacional de Investigaciones Sismológicas (CENAIS)</li>
                    <li>Oficina Nacional de Estadística e Información (ONEI)</li>
                    <li>Earthquakelist.org</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    #Región Datos
    st.markdown("<a id='datos'></a>", unsafe_allow_html=True)
    st.header("Dashboard General-Resumen Anual 📊")
    
    #Explicación de los Datos que disponemos en el dataset
    with st.expander("Datos Disponibles"):
        st.markdown('''
    <p style="font-size:17px; font-weight:bold; color:black;">
        <i>
            Disponemos de información de los años del período (2003-2024) extraída de las fuentes antes mencionadas
            en donde reflejamos los datos registrados con respecto a la cantidad de sismos perceptibles con sus características
            y las zonas de actividad sísmica para cada año asi como algunos datos descriptivos extras. Además disponemos de información
            específica sobre el comportamiento de cada mes en el rango de años de (2016-2024)
        </i>
    </p>
''', unsafe_allow_html=True)
    
    #Inicio de los análisis
    st.write("Ingresa la introduccion a esta seccion")

    tab1,tab2=st.tabs(["Anual","Mensual"])
    opciones=list(data.keys()) #lista con los años presentes en el json
    with tab1:
        selected=st.selectbox("Elija el año para ver su resumen:",opciones)
        b1,b2=st.columns([1,1])
        with b1:
            st.markdown(f"""
            <div class="stat-card">
                <div>Total de Sismos</div>
                <div class="stat-value">{data[selected]["total"]}</div>
                <div>#{len(mylib.Top_Sismos(data))-mylib.Top_Sismos(data).index(data[selected]["total"]) if data[selected]["total"] in mylib.Top_Sismos(data) else "No hay información registrada"} en los años disponibles</div>
            </div>""", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="stat-card">
                <div>zona más activa:<br>{data[selected]["zona_activa"]["nombre"]}
                </div>
                <div class="stat-value">{data[selected]["zona_activa"]["cantidad"]}</div>
                <div>#{len(mylib.Top_ZAS(data))-mylib.Top_ZAS(data).index(data[selected]["zona_activa"]["cantidad"])} en la lista de zonas disponibles</div>
            </div>""", unsafe_allow_html=True)
        with b2:
            st.markdown(f"""
            <div class="stat-card">
                <div>Máxima magnitud alcanzada:<br>lugar:{data[selected]["terremoto_principal"]["lugar"]}<br>fecha:{data[selected]["terremoto_principal"]["fecha"]}</div>
                <div class="stat-value">{data[selected]["terremoto_principal"]["magnitud"]}</div>
                <div>#{len(mylib.Top_Quake(data))-mylib.Top_Quake(data).index(data[selected]["terremoto_principal"]["magnitud"])} de la Base de Datos</div>
            </div>""", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="stat-card">
                <div>Día más activo:<br>fecha:{data[selected]["dia_activo"]["fecha"]}</div>
                <div class="stat-value">{data[selected]["dia_activo"]["cantidad"]}</div>
                <div></div>
            </div>""", unsafe_allow_html=True)

        if selected in opciones[:10]: #Toma el rango de valores de "2024" hasta "2015" al ser los que presentas datos sobre la información mensual
            
        
            fig = mylib.sismos_mensualidad(data, selected)
            st.plotly_chart(fig,use_container_width=True)
        
            fig2 = mylib.evolucion_mensual_por_zona(data,selected)
            st.plotly_chart(fig2,use_container_width=True)

            fig3= mylib.evolucion_mensual_días(data,selected)
            st.plotly_chart(fig3,use_container_width=True)
        
    with tab2:
            opciones_m=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
            selectedm=st.selectbox("Elija el mes para ver su resumen:",opciones_m)
            c1,c2,c3=st.columns([1,1,1])
            datos_m=mylib.month_analize(data,selected,selectedm)
            with c1:
                st.markdown(f"""
                <div class="stat-card">
                    <div>Día mas activo<br> {datos_m[0]} </div>
                    <div class="stat-value">{datos_m[1]}</div>
                </div>""", unsafe_allow_html=True)
                
            with c2:
                st.markdown(f"""
                <div class="stat-card">
                    <div>Zona más activa:<br>lugar:{datos_m[2]}</div>
                    <div class="stat-value">{datos_m[3]}</div>
                </div>""", unsafe_allow_html=True)
            with c3:
                st.markdown(f"""
                <div class="stat-card">
                    <div>Zona energética:</div>
                    <div class="stat-value">{datos_m[4]}</div>
                </div>""", unsafe_allow_html=True)
            st.plotly_chart(datos_m[-1],use_container_width=True)
    #Región Gráficos
    st.markdown("<a id='graficos'></a>", unsafe_allow_html=True)
    st.header("Tabla con filtros")
    
    perceptibles=mylib.perceptibles_df(data)
    perceptibles=perceptibles.dropna(subset='año') #elimina las filas con valor NA en el dataframe
    toggle1 = st.toggle("Global Año")
    toggle2 = st.toggle("Global Mes")
    años = perceptibles['año'].unique().tolist() #devuelve lista con los años del dataframe sin repetir
    meses = perceptibles['mes_nombre'].unique().tolist() #devuelve lista con los meses del dataframe sin repetir
    if not toggle1: #En esta sección habilitamos las secciones Global Año y Global Mes, cada una es el equivalente a seleccionar todos los años, meses respectivamente 
        año_seleccionado = st.multiselect("Año(s)",años, placeholder="Selecciona el año deseado")
        
    else:
        año_seleccionado=años
    if not toggle2:
        mes_seleccionado = st.multiselect("Mes(es)",meses,placeholder="Selecciona el mes deseado")
    else:
        mes_seleccionado=meses
    min_rango, max_rango = perceptibles['magnitud'].min(), perceptibles['magnitud'].max() #define un rango desde el minimo de las magnitudes hasta el maximo
    m_range = st.slider(
        'Rango de magnitudes',
        min_rango, max_rango, (min_rango, max_rango)
    )

    min_prof, max_prof = perceptibles['profundidad'].min(), perceptibles['profundidad'].max() #define un rango desde el minimo de profundidad hasta el maximo
    prof_range = st.slider(
        'Rango de profundidades',
        min_prof, max_prof, (min_prof, max_prof)
    )

    df_filtrado = perceptibles[ #filtra el Dataframe bajo las opciones antes elegidas
        (perceptibles["año"].isin(año_seleccionado)) &
        (perceptibles["magnitud"]).between(*m_range) &
        (perceptibles["mes_nombre"].isin(mes_seleccionado)) &
        (perceptibles["profundidad"].between(*prof_range))
        ]
    
    st.write("### Tabla Perceptibles")
    st.dataframe(df_filtrado)

    st.write("añadir analisis")

    fig_zonas=mylib.Top_zonas(data)
    st.plotly_chart(fig_zonas,use_container_width=True)


    fig_magnitud=mylib.magnitud_anual(data)
    st.plotly_chart(fig_magnitud,use_container_width=True)
    st.markdown("<a id='conclusiones'></a>", unsafe_allow_html=True)
    st.header("Conclusiones")
    st.write("Contenido de conclusiones...")

    


    #Esto puedes quitarlo
    with st.expander("¿Quiénes somos?"):
        st.write("Respuesta a quienes somos")
        st.write("GeoDataCuba nos permite no solo visualizar, sino comprender el comportamiento de Cuba en este tema de una manera sencilla y llamativa para la audiencia.")
        col1, col2, col3 = st.columns(3)
        with col2:
            st.markdown('<p style="font-family: sans-serif;font-size: 20px;font-weight: bold;"><i style="color:rgb(0,87,214);">GeoDataCuba:</i> <l style= "color:rgb(0,33,66);">Cuando la tierra tiembla, los datos hablan...</l></p>', unsafe_allow_html=True)
        

    with st.expander("¿Cuál es nuestro objetivo principal?"):
        st.write("Respuesta al objetivo")
        st.write("Partimos de información pública brindada por el ")
    #Hasta aquí
        


        # Pie de página
    st.markdown('<div class="app-footer">', unsafe_allow_html=True)
    st.markdown('🌋 GeodataCuba v1.0 · Made in Cuba (:D)')
    st.markdown('</div>', unsafe_allow_html=True)
    
        # Cerrar contenedor principal
    st.markdown('</div>', unsafe_allow_html=True)

# Punto de entrada
if __name__ == "__main__":
    main_app()