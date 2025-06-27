import streamlit as st
import json
import analysis as mylib
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
c1,c2=st.columns([2,2])
with c1:
    st.title("Cuba avanza y eso....")
with c2:
    st.title("Presentado por:")
    st.image("Extra/GeoData.png")

with st.sidebar:
        st.image("Extra/GeoData.png",use_container_width=True)        
        # Menú para navegar
        st.sidebar.markdown("## 📖 Índice ")
        st.sidebar.markdown("- [Inicio](#Inicio)")
        st.sidebar.markdown("- [Contexto Geológico](#Contexto)")
        st.sidebar.markdown("- [Panorama histórico](#historia)")   
        st.sidebar.markdown("- [Conclusiones](#conclusiones)")

st.markdown("<a id='Inicio'></a>", unsafe_allow_html=True)
st.header("")
st.header("La mañana que cambió la perspectiva científica")

st.markdown("**10 de noviembre de 2024, 11:49 de la mañana...**")
st.markdown("""En Santiago de Cuba, los científicos del Centro Nacional de Investigaciones 
Sismológicas (CENAIS) observaban sus monitores con una mezcla de 
fascinación y preocupación. Las señales que llegaban desde la red de 
estaciones sísmicas no dejaban dudas: algo extraordinario estaba ocurriendo 
en las profundidades de la falla Septentrional-Oriente""") 
c1,c2,c3=st.columns([1,2,1])
with c2:
    st.image("Extra/Cientifico.png")  
st.markdown("""Mientras miles de cubanos almorzaban o trabajaban en sus rutinas 
dominicales, la tierra decidió recordarles que bajo sus pies se esconde una de 
las zonas tectónicamente más activas del Caribe. Un sismo de magnitud 6.7 
(el más fuerte registrado en Cuba en 2024)  sacudió la isla desde Bartolomé 
Masó, en la costa suroriental""")

st.image("Extra/Bartolome-Masó.png", use_container_width=True)

st.markdown("""Pero este evento tenía algo diferente. Una hora antes, a las 10:50 de la mañana, 
un precursor sísmico ya había hecho saltar las alarmas en el observatorio. Los 
científicos sabían que algo significativo se aproximaba, pero nadie imaginaba 
que estaban presenciando el inicio de la secuencia sísmica más intensa 
registrada en Cuba en décadas, pero para poder describir el fenómeno, debemos comprender primero el contexto geológico de Cuba""")

st.markdown("<a id='Contexto'></a>", unsafe_allow_html=True)
st.header("Contexto Geolólico")

st.markdown("""Desde el punto de vista geodinámico, el archipiélago cubano forma parte de la placa de Norteamérica, próximo al límite con la microplaca de Gonave. 
Este límite lo constituye la falla Oriente, situada al sur de la región oriental de Cuba, zona donde se registró la actividad anómala.
Aquí  se pone de manifiesto un proceso transpresivo tipo flower, manifestado por un predominio de fallas inversas. Este proceso transpresivo ha ocasionado el levantamiento del fondo marino, denominado Cinturón Deformado de Santiago de Cuba.""")

with st.expander("¿Quieres saber en que consiste este proceso?"):
    st.write("Se trata de un proceso tectónico donde una falla transpresiva (combinación de deslizamiento horizontal y compresión) genera una estructura en flor, caracterizada por múltiples fallas secundarias que se ramifican, similar a los pétalos de una flor.")
b1,b2=st.columns([2,2])
with b1:
    st.image("Extra/contexto.png")
with b2:
    st.markdown("""Esta estructura tectónica representa una de las zonas más activas del sistema 
de fallas cubano, donde la energía acumulada durante décadas se libera 
súbitamente en forma de terremotos. En las horas siguientes al sismo principal, 
los datos comenzaron a revelar una secuencia sísmica intensa que se 
extendería durante semanas
""")
st.markdown("<a id='historia'></a>", unsafe_allow_html=True)
st.header("¿Qué pasó en noviembre de 2024?")

st.markdown("")
