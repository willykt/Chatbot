import streamlit as st

st.set_page_config(
    page_title="ChatData",
    page_icon="🪄",
    layout='wide'

)



st.title("Interactua con tus documentos 👩‍💻📝")


st.title("ChatExcel")

st.markdown("""
                Permite a los usuarios interactuar con un archivo Excel utilizando modelos de lenguaje (LLMs) a través de la integración con **LangChain** 🦜️🔗 y la API de **Gemini** 🔷 de Google. La funcionalidad principal de ChatExcel incluye:

                1. **Carga de archivos Excel**: Los usuarios pueden subir archivos Excel (.xlsx, .xls) para que la aplicación lea las hojas de cálculo.
                2. **Interacción con el archivo**: Utiliza LangChain y modelos LLM para generar respuestas basadas en los datos de las hojas de Excel, permitiendo consultas y análisis.
                3. **Selección de agente**: Los usuarios pueden elegir entre diferentes agentes (ZERO_SHOT_REACT_DESCRIPTION y OPENAI_FUNCTIONS) para interactuar con el archivo.
                4. **Gestión de la sesión**: El código almacena el historial de mensajes y el estado del agente para mantener una conversación fluida.
                5. **Formatos de respuesta**: Mejora el formato de salida de los agentes, limpiando el texto y resaltando los pasos del razonamiento.
                6. **Interfaz intuitiva**: La aplicación cuenta con pestañas para chat y visualización de los "pensamientos" del modelo, haciendo la interacción más comprensible.

                En resumen, este código ofrece una plataforma de interacción avanzada con hojas de Excel mediante inteligencia artificial, ideal para realizar análisis o consultas sobre los datos de forma eficiente.
            """)


st.title("ChatPDF")

st.markdown("""

                ChatPDF que permite a los usuarios cargar un archivo PDF, extraer su contenido y hacer consultas basadas en el texto extraído utilizando un modelo de lenguaje generativo de Google **Gemini** 🔷, todo esto integrado con **LangChain** 🦜️🔗. Detalles de funcionamiento:

                
                1. **Carga de PDF**: El usuario puede subir un archivo PDF mediante la interfaz de usuario, y el texto se extrae usando la librería `PyPDF2`.
                2. **Extracción del Texto**: Se extrae el texto de cada página del archivo PDF y se procesa para su posterior uso.
                3. **Gemini API Key**: El usuario debe ingresar una clave API de Gemini en la barra lateral, la cual se usa para acceder a los servicios de Google Generative AI.
                4. **Segmentación Semántica del Texto**: El texto extraído del PDF se segmenta en partes más pequeñas (chunks) usando un `SemanticChunker`, que utiliza embeddings generados por Google Gemini para detectar puntos de ruptura basados en diferencias semánticas.
                5. **Embeddings y Vector Store**: Los fragmentos de texto segmentados se convierten en embeddings y se almacenan en memoria utilizando `DocArrayInMemorySearch`, permitiendo la búsqueda y recuperación de documentos relevantes.
                6. **Consulta del Usuario**: El usuario puede realizar consultas mediante una entrada de texto. La consulta se evalúa en el contexto de los documentos extraídos del PDF, y el modelo `ChatGoogleGenerativeAI` genera una respuesta basada en ese contexto.
                7. **Interfaz de Respuesta**: Las respuestas generadas se muestran en la interfaz de chat.

                ChatPDF facilita la interacción entre un usuario y el contenido de un PDF, permitiendo hacer preguntas y recibir respuestas contextualizadas utilizando IA generativa.

                            """)