import streamlit as st
import numpy as np
import google.generativeai as genai
import os
import requests
import plotly.graph_objects as go

# Configure Google Generative AI
genai.configure(api_key="AIzaSyDUMlx6rT867EZ7pN_FAj_9rcXfnkwtOLc")  # Replace with your Google API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyDUMlx6rT867EZ7pN_FAj_9rcXfnkwtOLc"

# Google Generative AI settings
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

model2 = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config={
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    },
    system_instruction=(
        "You are a helpful personal assistant chatbot"
    ),
)

chat = model2.start_chat()

def chat_with_me(question):
    try:
        response = chat.send_message(question)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# NASA API Key
API_KEY = 'bnoi4MJ8HCB1l6wGFpuUeX4pdphfr6L2wkcvrUI2'  # Replace with your NASA API key
API_URL = f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-10-01&end_date=2024-10-02&api_key={API_KEY}'

# Fetch NASA asteroid data
def fetch_asteroid_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Error fetching data from NASA API.")
        return None

# Sidebar
st.sidebar.title("Dashboard")

app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Orrery", "Chat Support", "Quiz"])
st.sidebar.markdown("""
### Connect with Us
<a href="https://github.com/link-to-repo/" target="_blank">
    <img src="https://img.icons8.com/material-outlined/24/ffffff/github.png" style="vertical-align: middle;"/>
</a>
<a href="https://www.linkedin.com/in/your-linkedin-profile/" target="_blank">
    <img src="https://img.icons8.com/material-outlined/24/ffffff/linkedin.png" style="vertical-align: middle;"/>
</a>
<a href="https://www.instagram.com/your-instagram-profile/" target="_blank">
    <img src="https://img.icons8.com/material-outlined/24/ffffff/instagram-new.png" style="vertical-align: middle;"/>
</a>
""", unsafe_allow_html=True)

# Main Page
if app_mode == "Home":
    st.markdown("""
    <style>
    .popup-text h1 {
        font-family: 'Courier New', Courier, monospace;
        font-size: 3.5em;
        color: white;
    }
    .popup-text h1 span {
        display: inline-block;
        opacity: 0;
        transform: scale(0.5);
        animation: popUp 0.5s ease forwards;
    }
    .popup-text h1 span:nth-child(1) { animation-delay: 0.1s; }
    .popup-text h1 span:nth-child(2) { animation-delay: 0.2s; }
    .popup-text h1 span:nth-child(3) { animation-delay: 0.3s; }
    .popup-text h1 span:nth-child(4) { animation-delay: 0.4s; }
    .popup-text h1 span:nth-child(5) { animation-delay: 0.5s; }
    .popup-text h1 span:nth-child(6) { animation-delay: 0.6s; }
    .popup-text h1 span:nth-child(7) { animation-delay: 0.7s; }
    .popup-text h1 span:nth-child(8) { animation-delay: 0.8s; }
    .popup-text h1 span:nth-child(9) { animation-delay: 0.9s; }
    .popup-text h1 span:nth-child(10) { animation-delay: 1.0s; }
    .popup-text h1 span:nth-child(11) { animation-delay: 1.1s; }
    .popup-text h1 span:nth-child(12) { animation-delay: 1.2s; }
    .popup-text h1 span:nth-child(13) { animation-delay: 1.3s; }
    .popup-text h1 span:nth-child(14) { animation-delay: 1.4s; }

    @keyframes popUp {
        0% { transform: scale(0.5); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    </style>

    <div class="popup-text">
        <h1>
            <span>A</span><span>N</span><span>T</span><span>A</span><span>R</span><span>I</span><span>K</span><span>S</span><span>H</span><span>A</span>
            <span>Y</span><span>A</span><span>N</span><span>A</span>
        </h1>
    </div>
    """, unsafe_allow_html=True)

    # Background Image
    st.markdown("""
    <style>
    .main {
        background-image: url("https://www.bing.com/images/search?view=detailV2&ccid=Sr00HSPH&id=B501C10B9F610D17D58E9B23BF67FB2A689CD9FC&thid=OIP.Sr00HSPHwbe_ZDy3K6cywAHaEo&mediaurl=https%3A%2F%2Fwallpapercave.com%2Fwp%2Fwp2293445.jpg&exph=1600&expw=2560&q=space&simid=608028732745208281&FORM=IRPRST&ck=9D6E5A1364D99B1286FBFC0AA8EC4262&selectedIndex=9&itb=0&cw=1375&ch=676&ajaxhist=0&ajaxserp=0");
        background-size: cover;
        background-repeat: no-repeat;
        padding: 50px;
        color:white;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    Welcome to ANTARIKSHA YANA 🔍
    Explore the interactive orrery to view celestial bodies such as planets, asteroids, and more!
    """)

elif app_mode == "About":
    st.header("About")
    st.markdown("""
    #### About the Project
    Welcome to Antariksha Yana — your gateway to exploring the wonders of the solar system!
    This interactive orrery app is designed to visually represent celestial bodies such as planets, Near-Earth Asteroids (NEAs), Near-Earth Comets (NECs), and Potentially Hazardous Asteroids (PHAs).
    Our mission is to educate the public about the intricate and dynamic nature of our solar neighborhood.
    """)

# Function to calculate orbital positions for NEOs
def calculate_orbital_positions(neo, theta):
    try:
        if 'orbital_data' not in neo:
            return None

        a = float(neo['orbital_data'].get('semi_major_axis', 0))
        e = float(neo['orbital_data'].get('eccentricity', 0))
        i = np.radians(float(neo['orbital_data'].get('inclination', 0)))
        omega = np.radians(float(neo['orbital_data'].get('argument_of_periapsis', 0)))
        Omega = np.radians(float(neo['orbital_data'].get('ascending_node_longitude', 0)))

        if a == 0:
            return None

        x_prime = a * (np.cos(theta) - e)
        y_prime = a * np.sqrt(1 - e ** 2) * np.sin(theta)

        x = (x_prime * (np.cos(Omega) * np.cos(omega) - np.sin(Omega) * np.sin(omega) * np.cos(i))
             - y_prime * (np.cos(Omega) * np.sin(omega) + np.sin(Omega) * np.cos(omega) * np.cos(i)))
        y = (x_prime * (np.sin(Omega) * np.cos(omega) + np.cos(Omega) * np.sin(omega) * np.cos(i))
             + y_prime * (np.sin(Omega) * np.sin(omega) - np.cos(Omega) * np.cos(omega) * np.cos(i)))
        z = (x_prime * np.sin(i) * np.sin(omega) + y_prime * np.sin(i) * np.cos(omega))

        return x, y, z

    except (KeyError, ValueError) as e:
        return None

# Function to calculate positions for planets
def calculate_planet_positions(planet_data, theta):
    a = planet_data["a"]
    x = a * np.cos(theta)
    y = a * np.sin(theta)
    z = 0
    return x, y, z

# NASA API endpoint for Near-Earth Objects
def fetch_neo_data():
    neo_url = "https://api.nasa.gov/neo/rest/v1/neo/browse"
    params = {'api_key': 'bnoi4MJ8HCB1l6wGFpuUeX4pdphfr6L2wkcvrUI2'}  # Replace with your NASA API key
    response = requests.get(neo_url, params=params)
    if response.status_code == 200:
        return response.json()["near_earth_objects"]
    else:
        st.error("Error fetching NEO data.")
        return []

# Create the Plotly figure for the orrery
def create_figure(neo_data):
    orbit_data = []
    point_data = []

    # Create data for each NEO
    for neo in neo_data:
        for theta in np.linspace(0, 2 * np.pi, 100):
            pos = calculate_orbital_positions(neo, theta)
            if pos:
                x, y, z = pos
                orbit_data.append(go.Scatter3d(
                    x=[x], y=[y], z=[z], mode='lines', name=neo['name'], line=dict(width=2)
                ))

    # Create data for planets (sample data)
    planets = {
        "Mercury": {"a": 0.39},
        "Venus": {"a": 0.72},
        "Earth": {"a": 1.0},
        "Mars": {"a": 1.52},
        "Jupiter": {"a": 5.2},
        "Saturn": {"a": 9.58},
        "Uranus": {"a": 19.22},
        "Neptune": {"a": 30.05},
    }

    for planet, data in planets.items():
        for theta in np.linspace(0, 2 * np.pi, 100):
            pos = calculate_planet_positions(data, theta)
            x, y, z = pos
            point_data.append(go.Scatter3d(
                x=[x], y=[y], z=[z], mode='markers', name=planet, marker=dict(size=5)
            ))

    # Define the layout for the 3D plot
    layout = go.Layout(
        scene=dict(
            xaxis=dict(title='X Axis', showgrid=False, zeroline=False),
            yaxis=dict(title='Y Axis', showgrid=False, zeroline=False),
            zaxis=dict(title='Z Axis', showgrid=False, zeroline=False),
            aspectmode='cube'
        ),
        title="Interactive Orrery of Celestial Bodies",
        margin=dict(l=0, r=0, b=0, t=40),
        showlegend=True
    )

    fig = go.Figure(data=orbit_data + point_data, layout=layout)
    return fig

# Render the appropriate page based on user selection
if app_mode == "Orrery":
    st.header("Orrery Visualization")
    neo_data = fetch_neo_data()  # Fetch NEO data
    if neo_data:
        fig = create_figure(neo_data)  # Create figure with NEOs
        st.plotly_chart(fig)  # Display the Plotly chart

elif app_mode == "Chat Support":
    st.header("Chat Support")
    user_input = st.text_input("Ask me anything about celestial bodies:")
    if user_input:
        response = chat_with_me(user_input)
        st.write(response)

elif app_mode == "Quiz":
    st.header("Quiz on Celestial Bodies")
    st.markdown("Test your knowledge about celestial bodies in our solar system!")


    # Define the questions and answers
    questions = [
        {"question": "What type of galaxy is the Milky Way classified as?", 
         "options": ["A) Elliptical", "B) Irregular", "C) Spiral", "D) Lenticular"], 
         "answer": "C) Spiral"},
        
        {"question": "What is the primary purpose of the Hubble Space Telescope?", 
         "options": ["A) Studying the Earth's atmosphere", "B) Observing deep space and celestial objects", 
                     "C) Mapping the surface of Mars", "D) Monitoring satellite communications"], 
         "answer": "B) Observing deep space and celestial objects"},
        
        {"question": "Which of the following moons is the largest in our solar system?", 
         "options": ["A) Europa", "B) Ganymede", "C) Titan", "D) Callisto"], 
         "answer": "B) Ganymede"},
        
        {"question": "What is the term for the boundary around a black hole beyond which nothing can escape?", 
         "options": ["A) Event horizon", "B) Singularity", "C) Photon sphere", "D) Accretion disk"], 
         "answer": "A) Event horizon"},
        
        {"question": "What is the main source of the Sun's energy?", 
         "options": ["A) Chemical reactions", "B) Nuclear fusion", "C) Gravitational collapse", 
                     "D) Electrical discharge"], 
         "answer": "B) Nuclear fusion"},
        
        {"question": "Which space mission was the first to land on the surface of the Moon?", 
         "options": ["A) Apollo 11", "B) Apollo 12", "C) Luna 9", "D) Voyager 1"], 
         "answer": "A) Apollo 11"},
        
        {"question": "Which element is most abundant in the universe?", 
         "options": ["A) Carbon", "B) Helium", "C) Oxygen", "D) Hydrogen"], 
         "answer": "D) Hydrogen"},
        
        {"question": "What is the phenomenon that causes light from distant stars to appear redder as they move away from us?", 
         "options": ["A) Blue shift", "B) Red shift", "C) Gravitational lensing", "D) Cosmic microwave background"], 
         "answer": "B) Red shift"},
        
        {"question": "Which planet has the longest day relative to its year?", 
         "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"], 
         "answer": "A) Venus"},
        
        {"question": "What is the name of the force that keeps planets in orbit around the Sun?", 
         "options": ["A) Electromagnetic force", "B) Gravitational force", "C) Nuclear force", "D) Frictional force"], 
         "answer": "B) Gravitational force"},
        
        {"question": "What is the largest planet in our solar system?", 
         "options": ["A) Earth", "B) Jupiter", "C) Mars"], 
         "answer": "B) Jupiter"},
        
        {"question": "What planet is known as the Red Planet?", 
         "options": ["A) Mars", "B) Venus", "C) Saturn"], 
         "answer": "A) Mars"},
    ]

    # Session state to manage the current question index and score
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0

    current_question = questions[st.session_state.question_index]

    # Display current question and options
    st.write(current_question["question"])
    selected_option = st.radio("Choose an option:", current_question["options"])

    if st.button("Submit Answer"):
        # Check if the selected option is correct
        if selected_option == current_question["answer"]:
            st.success("Correct!")
            st.session_state.score += 1  # Increase score for correct answer
        else:
            st.error("Incorrect! The correct answer was: " + current_question["answer"])

        # Move to the next question
        if st.session_state.question_index < len(questions) - 1:
            st.session_state.question_index += 1
            st.rerun()  # Rerun to show the next question
        else:
            st.success("Quiz completed!")
            st.write(f"You scored: {st.session_state.score} out of {len(questions)}")
            del st.session_state.question_index  # Reset the quiz state
            del st.session_state.score  # Reset the score state
