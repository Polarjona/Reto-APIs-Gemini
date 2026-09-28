# Reto del Día: Integración y Exploración de la API de Google Gemini

## 1. Proceso de Obtención de la API Key

Para obtener la clave de acceso a la API de Gemini:

1. Acceder a https://aistudio.google.com/
2. Iniciar sesión con una cuenta de Google
3. En el menú de navegación, seleccionar la opción **Get API key**
4. Hacer clic en **Create API key in new project** (o seleccionar un proyecto existente de Google Cloud)
5. Copiar la clave generada y guardarla en un lugar seguro (se recomienda almacenarla como variable de entorno)

---

## 2. Límites Gratuitos Disponibles (Free Tier)

Google AI Studio ofrece un nivel gratuito con acceso a modelos como `gemini-2.5-flash` y `gemini-1.5-flash`, ideal para desarrollo y prototipado. Sus límites estándar son:

| Parámetro | Límite Gratuito |
| :--- | :--- |
| **Requests per Minute (RPM)** | 15 solicitudes / minuto |
| **Tokens per Minute (TPM)** | 1,000,000 tokens / minuto |
| **Requests per Day (RPD)** | 1,500 solicitudes / día |
| **Uso de datos** | Los datos procesados en la capa gratuita pueden ser utilizados por Google para mejorar sus modelos (sin información de identificación personal). |

---

## 3. Requisitos e Instalación

Asegúrate de contar con Python 3.9 o superior e instalar la librería oficial `google-genai` junto con `pillow` para el manejo de imágenes:

```bash
pip install google-genai pillow
```

---

## 5. Resultados Obtenidos

## Texto
Texto: Me encanta la nueva interfaz del sistema, es súper intuitiva y rápida.
Aquí tienes el análisis del texto:

* **Sentimiento:** Positivo
* **Entidades detectadas:** 
  * **Interfaz del sistema** (Componente / Producto de software)
--------------------------------------------------
Texto: El servicio técnico tardó tres días en responder y no solucionó el problema.
Aquí tienes el análisis del texto:

* **Sentimiento:** Negativo (expresa insatisfacción por la demora y la falta de solución).
* **Entidades detectadas:**
  * **Servicio técnico** (Organización / Servicio)
  * **Tres días** (Tiempo / Duración)
--------------------------------------------------
Texto: La actualización se instalará esta noche a las 02:00 AM.
Aquí tienes el análisis del texto:

* **Sentimiento:** **Neutro** 
  *(Es un comunicado meramente informativo y objetivo que no expresa emociones implícitas ni explícitas).*

* **Entidades detectadas:**
  * **Expresión de tiempo / Hora:** `02:00 AM`
  * **Expresión de tiempo / Momento:** `esta noche`
  * **Objeto / Evento (Tecnología):** `actualización`
--------------------------------------------------
Texto: No estoy seguro de si este cambio en la configuración nos beneficie a todos.
Aquí tienes el análisis del texto:

* **Sentimiento:** **Neutro** (expresa duda e incertidumbre; aunque refleja escepticismo, no llega a ser explícitamente negativo ni positivo).
* **Entidades detectadas:** 
  * **Entidades nombradas (propias):** Ninguna (no hay nombres de personas, organizaciones, lugares o marcas).
  * **Entidades de dominio/concepto (TI):** `Configuración` (se refiere a un parámetro, componente o estado de un sistema).
--------------------------------------------------
Texto: Google lanzó una nueva herramienta de IA esta semana en California.
Aquí tienes el análisis del texto:

* **Sentimiento:** **Neutro** 
*(Es un texto puramente informativo y objetivo que reporta un hecho. En algunos contextos de noticias de tecnología podría considerarse levemente positivo por tratarse de un nuevo lanzamiento, pero su tono gramatical es neutro).*

* **Entidades detectadas:**
  * **Google:** Organización / Empresa
  * **IA (Inteligencia Artificial):** Tecnología / Concepto
  * **California:** Lugar / Ubicación geográfica
  * **Esta semana:** Expresión de tiempo / Fecha relativa
--------------------------------------------------
Texto: The customer support team in London was amazingly helpful and fast!
Aquí tienes el análisis del texto:

* **Sentimiento:** Positivo
* **Entidades detectadas:**
  * **London** (Ubicación / Ciudad)
  * **Customer support team** (Organización / Equipo de trabajo)
--------------------------------------------------
Texto: This laptop gets extremely hot after only twenty minutes of use.
Aquí tienes el análisis del texto:

* **Sentimiento:** Negativo (expresa una queja/defecto sobre el rendimiento y sobrecalentamiento del producto en poco tiempo).

* **Entidades detectadas:**
  * **Producto / Objeto:** *Laptop* (Portátil / Computadora)
  * **Condición / Estado:** *Extremely hot* (Extremadamente caliente / Sobrecalentamiento)
  * **Tiempo / Duración:** *Twenty minutes* (Veinte minutos)
--------------------------------------------------
Texto: The meeting with Microsoft was rescheduled for next Thursday.
Aquí tienes el análisis del texto:

* **Sentimiento:** **Neutro** 
  *(Es una afirmación puramente informativa y logística sobre un cambio de agenda, sin carga emocional explícitamente positiva o negativa).*

* **Entidades detectadas:**
  * **Microsoft:** Organización / Empresa (`ORG`)
  * **next Thursday** (próximo jueves): Fecha / Expresión temporal (`DATE`)
  * **meeting** (reunión): Evento (`EVENT`)
--------------------------------------------------
Texto: I'm feeling indifferent about the new design updates made by Apple.
Aquí tienes el análisis del texto:

* **Sentimiento:** Neutro *(la palabra "indifferent" indica una falta de emoción positiva o negativa)*.
* **Entidades detectadas:**
  * **Apple:** Organización / Empresa (Entidad nombrada principal).
  * **New design updates (Nuevas actualizaciones de diseño):** Concepto / Característica de producto.
--------------------------------------------------
Texto: The delivery arrived two days late and the box was completely crushed.
Aquí tienes el análisis del texto:

* **Sentimiento:** Negativo 
* **Entidades detectadas:**
  * **Delivery** (Entrega / Servicio de envío) — *Atributo afectado: Retraso ("two days late")*
  * **Box** (Caja / Paquete) — *Atributo afectado: Estado físico ("completely crushed")*
  * **Two days** (Dos días) — *Entidad temporal / Duración del retraso*
--------------------------------------------------

## Imagen

Esta imagen es una de las fotografías más famosas e icónicas de la historia contemporánea: se trata del fondo de pantalla predeterminado del sistema operativo **Windows XP**, titulado originalmente ***Bliss*** (conocido en español como *"Felicidad"* o *"Santiago"*).

A continuación, se detallan sus elementos, colores y contexto:

---

### 1. Elementos Principales

*   **La Colina Verde:** Ocupa la mitad inferior del encuadre. Es una suave loma o colina completamente cubierta por una hierba verde, densa y limpia. La topografía presenta una curva continua que desciende ligeramente hacia la derecha.
*   **Detalles del Paisaje:** 
    *   En el primer plano (la parte inferior inmediata) se observan pequeñas manchas o puntos amarillos correspondientes a flores silvestres (probablemente dientes de león).
    *   Hacia el extremo derecho de la línea del horizonte, se aprecian tímidamente unas colinas o montañas lejanas en tonos azulados.
*   **El Cielo:** Ocupa la mitad superior de la imagen. Es un amplio cielo despejado salpicado de nubes blancas.
*   **Las Nubes:** Hay una mezcla de nubes tipo *cúmulo* (blancas, esponjosas y bien definidas en el centro y derecha) y nubes tipo *cirro* (más finas, estiradas y difusas en la parte superior izquierda).

---

### 2. Colores e Iluminación

*   **Paleta de Colores:** La composición se basa en un contraste bicromático muy marcado entre dos colores primarios/secundarios dominantes:
    *   **Verde intenso/brillante:** En el campo, con variaciones que van desde el verde lima (donde pega directamente la luz) hasta verdes más oscuros en las zonas de penumbra.
    *   **Azul cobalto/azur:** En el cielo, con un tono muy vivo y saturado.
    *   **Blanco puro:** En las nubes, aportando luminosidad.
*   **Iluminación:** La escena está iluminada por una luz solar directa y clara (típica de un día despejado de primavera), que resalta la textura de la Hierba y genera sombras suaves que marcan las ondulaciones del terreno.

---

### 3. Contexto e Historia

*   **Fotógrafo y Ubicación:** Fue tomada por el fotógrafo estadounidense **Charles O'Rear** en enero de **1996** en el condado de Sonoma, California (EE. UU.), una famosa región vitivinícola. En ese momento, los viñedos locales habían sido retirados temporalmentedebido a una plaga, dejando la colina cubierta únicamente de hierba silvestre.
*   **Impacto Cultural:** Microsoft compró los derechos fotográficos en el año 2000. Debido al éxito masivo de Windows XP, se calcula que ha sido vista por miles de millones de personas en todo el mundo, convirtiéndose en un símbolo de la estética digital de los años 2000 y evocando una sensación de paz, serenidad y nostalgia.