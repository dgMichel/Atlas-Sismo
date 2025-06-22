import streamlit as st


# Esto siempre va primero en el código
st.set_page_config(
    page_title="GeodataCuba",
    page_icon="🌋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Todo el CSS que hace bonita la página
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

# Lo principal de la app
def main_app():
    # Barra lateral con menú
    with st.sidebar:
        st.markdown('<div class="sidebar-title"><span>🌋</span> GeodataCuba</div>', unsafe_allow_html=True)
        
        # Menú para navegar
        st.markdown('<div style="margin-bottom:1.5rem"><div style="font-size:1.1rem; margin-bottom:0.8rem">📊 Análisis</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-item active"><span>📈</span> Dashboard</div>', unsafe_allow_html=True)
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
        st.markdown("🟢 Servicios en línea")
        st.markdown("**Versión:** 1.0.0")
    
    # Parte principal de la app
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    
    # Título grande
    st.markdown('<div style="margin-bottom:2.5rem">', unsafe_allow_html=True)
    st.markdown('<h1 style="font-size:2.5rem">Dashboard de Análisis Sísmico</h1>', unsafe_allow_html=True)
    st.markdown('<p>Visualización de datos sísmicos de Cuba</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Estadísticas importantes
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    st.markdown("""
        <div class="stat-card">
            <div>Eventos totales</div>
            <div class="stat-value">1,542</div>
            <div>↑ 12 este mes</div>
        </div>
        <div class="stat-card">
            <div>Magnitud máxima</div>
            <div class="stat-value">6.7</div>
            <div>Registro histórico</div>
        </div>
        <div class="stat-card">
            <div>Promedio</div>
            <div class="stat-value">3.2</div>
            <div>↓ 0.3 vs año anterior</div>
        </div>
        <div class="stat-card">
            <div>Último evento</div>
            <div class="stat-value">4.2</div>
            <div>Hace 3 días</div>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Tarjetas de información
    st.markdown('<div class="card-grid">', unsafe_allow_html=True)
    
    # Tarjeta de fuentes de datos
    st.markdown("""
        <div class="card">
            <div class="card-header">
                <h3><span>📡</span> Fuentes de Datos</h3>
            </div>
            <div class="card-body">
                <p>Dónde sacamos la info:</p>
                <ul>
                    <li>CENAIS</li>
                    <li>USGS</li>
                    <li>Red Sísmica del Caribe</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Tarjeta de configuración
    st.markdown("""
        <div class="card">
            <div class="card-header">
                <h3><span>⚙️</span> Configuración</h3>
            </div>
            <div class="card-body">
                <p>Lo que tenemos activo:</p>
                <ul>
                    <li>Últimos 12 meses</li>
                    <li>Magnitud mínima: 3.0</li>
                    <li>Toda Cuba</li>
                </ul>
            </div>
        </div>
""", unsafe_allow_html=True)
    
    # Tarjeta de próximas cosas
    st.markdown("""
        <div class="card">
            <div class="card-header">
                <h3><span>🚀</span> Próximamente</h3>
            </div>
            <div class="card-body">
                <p>Cosas que queremos agregar:</p>
                <ul>
                    <li>Machine learning</li>
                    <li>Alertas tempranas</li>
                    <li>Reportes en PDF</li>
                </ul>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Tabla de ejemplo
    st.markdown('<h2>Eventos Recientes</h2>', unsafe_allow_html=True)
    st.markdown("""
    <table class="data-table">
        <thead>
            <tr>
                <th>Fecha</th>
                <th>Ubicación</th>
                <th>Magnitud</th>
                <th>Región</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>2023-06-15</td>
                <td>22.12°N, 80.45°W</td>
                <td>4.2</td>
                <td>Central</td>
            </tr>
            <tr>
                <td>2023-06-12</td>
                <td>21.85°N, 79.92°W</td>
                <td>3.8</td>
                <td>Occidental</td>
            </tr>
            <tr>
                <td>2023-06-10</td>
                <td>20.35°N, 76.55°W</td>
                <td>5.1</td>
                <td>Oriental</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)
    
    # Pie de página
    st.markdown('<div class="app-footer">', unsafe_allow_html=True)
    st.markdown('🌋 GeodataCuba v1.0 · Hecho para Cuba')
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Cerrar contenedor principal
    st.markdown('</div>', unsafe_allow_html=True)

# Punto de entrada
if __name__ == "__main__":
    main_app()
