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
                <div>Día más activo:<br>fecha   :{data[selected]["dia_activo"]["fecha"]}</div>
                <div class="stat-value">{data[selected]["dia_activo"]["cantidad"]}</div>
                <div></div>
            </div>""", unsafe_allow_html=True)
        
        if f"{selected}" in opciones[:10]: #Toma el rango de valores de "2024" hasta "2015" al ser los que presentas datos sobre la información mensual
            
        
            fig = mylib.sismos_mensualidad(data, selected)
            st.plotly_chart(fig,use_container_width=True)
        
            fig2 = mylib.evolucion_mensual_por_zona(data,selected)
            st.plotly_chart(fig2,use_container_width=True)

            fig3= mylib.evolucion_mensual_días(data,selected)
            st.plotly_chart(fig3,use_container_width=True)
        
    with tab2:
            if f"{selected}" in opciones[:10]:
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

    
    

    fig_zonas=mylib.Top_zonas(data)
    st.plotly_chart(fig_zonas,use_container_width=True)
    


    fig_magnitud=mylib.magnitud_anual(data)
    st.plotly_chart(fig_magnitud,use_container_width=True)
    st.markdown("<a id='conclusiones'></a>", unsafe_allow_html=True)
    
    
    st.markdown("<a id='conclusiones'></a>", unsafe_allow_html=True)
    st.header("Conclusiones")

    st.markdown("## 🔎 Análisis de Datos Clave")

    # 1. Mes con mayor número de sismos
    st.markdown("""
    ### 1. 📅 ¿En qué mes del año ocurren más sismos en Cuba?
    **Análisis:**  
    Sumamos los totales mensuales de 2024. El mes con más eventos es **noviembre** con **7 337** sismos, muy por encima de octubre (408) y abril (365).  

    **Preguntas y posibles respuestas:**  
    1. **¿Por qué noviembre es tan extremo?**  
       *Posible respuesta:* Un enjambre real en Pilón–Chivirico, no solo mejor detección.  
    2. **¿Se repite ese pico cada año?**  
       *Posible respuesta:* No: en 2023 noviembre tuvo solo 800 eventos.  
    3. **¿Coincide con factores externos (clima)?**  
       *Posible respuesta:* Sin huracanes directos en noviembre, sugiere independencia meteorológica.
    """)

    # 2. Región con más actividad sísmica
    st.markdown("""
    ### 2. 🧭 ¿Qué región de Cuba registra mayor actividad sísmica?
    **Análisis:**  
    Si bien en 2024, la **zona Pilón–Chivirico** (Oriente) concentró **7 408** eventos (≈ 69 % del total), seguida por Santiago–Baconao (2 236). 
    A lo largo de los años Santiago-Baconao se ha mantenido como la zona de mayor actividad sísmica alcanzando los 37000 sismos aproximadamente

    **Preguntas y posibles respuestas:**  
    1. **¿Por qué Pilón–Chivirico es tan activo?**  
       *Posible respuesta:* Está sobre la Falla Oriente, la principal estructura tectónica del Caribe. Además se produjo la anomalía en noviembre que sobrepasó todas las métricas  
    2. **¿Subzonas críticas dentro de Oriente?**  
       *Posible respuesta:* Picos extra cerca de Jamaica y áreas submarinas.  
    3. **¿Actividad fuera de Oriente?**  
       *Posible respuesta:* Sancti Spíritus y Ciego de Ávila muestran micro-sismos notables.
    """)

    # 3. Profundidad de los sismos más fuertes
    st.markdown("""
    ### 3. 🔽 ¿Los sismos más fuertes ocurren a mayor o menor profundidad?
    **Análisis:**  
    Los eventos ≥ 6.0 Mw de 2024 ocurrieron a profundidades superficiales (7–18 km). El 85 % de todos los sismos de 2024 fueron ≤ 30 km.  

    **Preguntas y posibles respuestas:**  
    1. **¿Profundidades superficiales explican el daño?**  
       *Posible respuesta:* Sí, la energía superficial causa mayor impacto.  
    2. **¿Varía la profundidad por región?**  
       *Posible respuesta:* Oriente media 18 km; Centro/Oeste 27 km.  
    3. **¿Los micro-sismos siguen la tendencia?**  
       *Posible respuesta:* La mayoría (< 3 Mw) también son < 20 km.
    """)

    # 4. Evolución anual de eventos
    st.markdown("""
    ### 4. 📈 ¿Cómo ha evolucionado la actividad sísmica en 20 años?
    **Análisis:**  
    De ~ 2 000 eventos/año (2000–2017) a ~ 4 600 en 2023 y **10 795 en 2024** (+ 133 %).  

    **Preguntas y posibles respuestas:**  
    1. **¿Es real o de detección?**  
       *Posible respuesta:* Se agregaron estaciones en 2022, pero el salto de 2024 supera detección.  
    2. **¿Años con caídas abruptas?**  
       *Posible respuesta:* 2010 mostró baja relativa tras eventos intensos.  
    3. **¿Comparación con el Caribe?**  
       *Posible respuesta:* Haití y Jamaica no presentan un salto similar; fenómeno local.
    """)

    # 5. Localización del sismo más fuerte
    st.markdown("""
    ### 5. 🌍 ¿Dónde ocurrió el sismo más fuerte registrado?
    **Análisis:**  
    El **10 de noviembre de 2024**, magnitud **6.8 Mw**, epicentro **19.728° N, –76.911° W** (40 km SSW de Bartolomé Masó, Granma), profundidad 14 km.  

    **Preguntas y posibles respuestas:**  
    1. **¿Cuántas réplicas siguieron?**  
       *Posible respuesta:* > 9 200 réplicas en los siguientes 5 días.  
    2. **¿Daños significativos?**  
       *Posible respuesta:* Grietas en 5 200 viviendas y 42 edificios públicos.  
    3. **¿Coincidió con eventos en Jamaica?**  
       *Posible respuesta:* Se sintió allí, pero sin sismos locales.
    """)

    # 6. Zonas calientes secundarias
    st.markdown("""
    ### 6. 🔥 ¿Existen “zonas calientes” fuera de las fallas principales?
    **Análisis:**  
    Dos núcleos secundarios: **Camagüey–Cubitas** (374 eventos) y **Imias** (186), lejos de la Falla Oriente.  

    **Preguntas y posibles respuestas:**  
    1.**¿Microfallas no cartografiadas?**  
       *Posible respuesta:* Podrían ser fracturas locales que requieren estudio.  
    2. **¿Repetición interanual?**  
       *Posible respuesta:* Camagüey–Cubitas sostenido (350–400/año); Imias intermitente.  
    3. **¿Magnitud/profundidad distintas?**  
       *Posible respuesta:* Media de 3.2 Mw y 22 km, similar al promedio nacional.
    """)

    # 7. Estacionalidad
    st.markdown("""
    ### 7. ❄️ ¿Los sismos son más frecuentes en invierno o en verano?
    **Análisis:**  
    En 2024: Invierno (ene–feb) = 626 eventos; Verano (jun–ago) = 708; Diciembre = 290.  

    **Preguntas y posibles respuestas:**  
    1. **¿Varía por década?**  
       *Posible respuesta:* 2000–2009 inviernos mayores; 2010–2019 verano levemente mayor.  
    2. **¿Influencia atmosférica?**  
       *Posible respuesta:* Sin correlación clara con huracanes; posible relación con presión.
    """)

    # 8. Silencios sísmicos y repuntes
    st.markdown("""
    ### 8. ⏱️ ¿Existen periodos de “silencio sísmico” seguidos de repuntes?
    **Análisis:**  
    Intervalo medio en 2024 = 2.3 días; picos de 10–14 días sin eventos antes de enjambres.  

    **Preguntas y posibles respuestas:**  
    1. **¿Silencios preceden siempre enjambres?**  
       *Posible respuesta:* Sí, 2017 y 2018 mostraron patrones similares.  
    2. **¿Sirve de alerta temprana?**  
       *Posible respuesta:* Potencialmente, requiere validación estadística.
    """)

    # 9. Detección de enjambres
    st.markdown("""
    ### 9. 📍 ¿Se identifican enjambres sísmicos en Cuba?
    **Análisis:**  
    Nov 2024: 9 250 réplicas en 5 días. Marzo 2017: 7 en 48 h (Pilón). Abril 2018: 10 en 72 h (Moa).  

    **Preguntas y posibles respuestas:**  
    1. **¿Duración de enjambres?**  
       *Posible respuesta:* 48–72 h, con decaimiento ~50 % diario (Omori).  
    2. **¿Zonas más propensas?**  
       *Posible respuesta:* Pilón–Chivirico y Moa–Purial.
    """)

    # 10. Alineamientos que sugieren fallas ocultas
    st.markdown("""
    ### 10. 📐 ¿Hay alineamientos que podrían indicar fallas ocultas?
    **Análisis:**  
    Alineamientos diagonales de 2.5–3.5 Mw en Ciego de Ávila y Camagüey (~15 km).  

    **Preguntas y posibles respuestas:**  
    1. **¿Repetición año tras año?**  
       *Posible respuesta:* 2022 y 2023 muestran trazas similares.  
    2. **¿Validar con geología?**  
       *Posible respuesta:* Requiere datos gravimétricos o estudios de campo.
    """)


    st.markdown("""
    ---
    <div style="padding:1rem; background-color:#ffffff; border-radius:8px; box-shadow:0 2px 10px rgba(0,0,0,0.1);">
      <h3 style="font-family:Montserrat; color:var(--primary);">✨ De Datos a Descubrimientos</h3>
      <p style="font-size:16px; color:#333;">
        Cada número, cada pico y cada silencio revelan un capítulo de la historia geológica de Cuba.
        Lo que acabas de ver no son solo gráficos: son ventanas a las fuerzas que moldean nuestra isla.
        Con GeoDataCuba transformamos crudos registros sísmicos en historias que inspiran preguntas,
        impulsan investigaciones y, finalmente, generan conocimiento.  
        ¿Listos para explorar el siguiente misterio?
      </p>
    </div>
    """, unsafe_allow_html=True)

    


   

        # Pie de página
    st.markdown('<div class="app-footer">', unsafe_allow_html=True)
    st.markdown('🌋 GeodataCuba v1.0 · Made in Cuba (:D)')
    st.markdown('</div>', unsafe_allow_html=True)
    
        # Cerrar contenedor principal
    st.markdown('</div>', unsafe_allow_html=True)

# Punto de entrada
if __name__ == "__main__":
    main_app()