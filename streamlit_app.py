# Original Code
# Imports
import streamlit as st
import pandas as pd
import plotly.express as px
import base64
import numpy as np
import pickle

# Configuration of the appearance of the ‘Union Insights’ app, optimising the visual experience for wedding planners through the use of pastel colours and customised styles reminiscent of the wedding theme. 
# Configuration of the appearance of the ‘Union Inscights’ app
st.set_page_config(
page_title="Union Insights",
page_icon="💍",
    layout="wide",
    initial_sidebar_state="expanded"
)
    # Use of a clear aesthetic configuration appropriate for the non-technical target audience, making the app creative and user-friendly.
    # Define Colors and Styles
# Define Colors and Styles
PRIMARY_COLOR = "#e4afaf"  # Pink for buttons and charts
BACKGROUND_COLOR = "#f6ceca"  # Pink for the main background
TEXT_COLOR = "#000000"  # Grey for text
ACCENT_COLOR = "#e4afaf"  # Pink for clean contrasts

    # Custom CSS for Global Styles

    # Animation: this is useful to enhance the interactivity of the app, providing an engaging experience for wedding planners.
    # Check if the animation should be shown 
if "show_animation" not in st.session_state:
    st.session_state.show_animation = True
    
# Function to load the main content
def show_main_content():

    # Configuration of a sidebar with filters and options to improve interactivity and customisation of the app, suitable for different analysis scenarios.
    # Logo in the sidebar and main bar to enhance the visual identity of the app.
    LOGO_LARGE = "logo lungo 2.png"  # Logo in the sidebar
    LOGO_ICON = "logo lungo 2.png"      # Logo in the main bar
    st.logo(
        image=LOGO_LARGE,  
        icon_image=LOGO_ICON,  
    )

show_main_content()
# Updated Code with Fixes
def load_model(file_path):
    """
    Load a trained model from the specified file and validate it.
    """
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    if not hasattr(model, "predict"):
        raise AttributeError("The loaded object is not a valid model. Ensure the file contains a trained model.")
    return model

try:
    model = load_model('trained_stack_model.pkl')
except Exception as e:
    st.sidebar.error(f"Error loading model: {e}")

cantons = ['Zürich', 'Bern / Berne', 'Luzern', 'Uri', 'Schwyz', 'Obwalden', 'Nidwalden', 
    'Glarus', 'Zug', 'Fribourg / Freiburg', 'Solothurn', 'Basel-Stadt', 'Basel-Landschaft',
    'Schaffhausen', 'Appenzell Ausserrhoden', 'Appenzell Innerrhoden', 'St. Gallen', 
    'Graubünden / Grigioni / Grischun', 'Aargau', 'Thurgau', 'Ticino', 'Vaud', 
    'Valais / Wallis', 'Neuchâtel', 'Genève', 'Jura']
age_groups = ['20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89']

features = ['Canton_AgeGroup_Aargau_20-29', 'Canton_AgeGroup_Aargau_30-39', 'Canton_AgeGroup_Aargau_40-49', 'Canton_AgeGroup_Aargau_50-59', 'Canton_AgeGroup_Aargau_60-69', 'Canton_AgeGroup_Aargau_70-79', 'Canton_AgeGroup_Aargau_80-89', 'Canton_AgeGroup_Appenzell Ausserrhoden_10-19', 'Canton_AgeGroup_Appenzell Ausserrhoden_20-29', 'Canton_AgeGroup_Appenzell Ausserrhoden_30-39', 'Canton_AgeGroup_Appenzell Ausserrhoden_40-49', 'Canton_AgeGroup_Appenzell Ausserrhoden_50-59', 'Canton_AgeGroup_Appenzell Ausserrhoden_60-69', 'Canton_AgeGroup_Appenzell Ausserrhoden_70-79', 'Canton_AgeGroup_Appenzell Ausserrhoden_80-89', 'Canton_AgeGroup_Appenzell Innerrhoden_10-19', 'Canton_AgeGroup_Appenzell Innerrhoden_20-29', 'Canton_AgeGroup_Appenzell Innerrhoden_30-39', 'Canton_AgeGroup_Appenzell Innerrhoden_40-49', 'Canton_AgeGroup_Appenzell Innerrhoden_50-59', 'Canton_AgeGroup_Appenzell Innerrhoden_60-69', 'Canton_AgeGroup_Appenzell Innerrhoden_70-79', 'Canton_AgeGroup_Appenzell Innerrhoden_80-89', 'Canton_AgeGroup_Basel-Landschaft_10-19', 'Canton_AgeGroup_Basel-Landschaft_20-29', 'Canton_AgeGroup_Basel-Landschaft_30-39', 'Canton_AgeGroup_Basel-Landschaft_40-49', 'Canton_AgeGroup_Basel-Landschaft_50-59', 'Canton_AgeGroup_Basel-Landschaft_60-69', 'Canton_AgeGroup_Basel-Landschaft_70-79', 'Canton_AgeGroup_Basel-Landschaft_80-89', 'Canton_AgeGroup_Basel-Stadt_10-19', 'Canton_AgeGroup_Basel-Stadt_20-29', 'Canton_AgeGroup_Basel-Stadt_30-39', 'Canton_AgeGroup_Basel-Stadt_40-49', 'Canton_AgeGroup_Basel-Stadt_50-59', 'Canton_AgeGroup_Basel-Stadt_60-69', 'Canton_AgeGroup_Basel-Stadt_70-79', 'Canton_AgeGroup_Basel-Stadt_80-89', 'Canton_AgeGroup_Bern / Berne_10-19', 'Canton_AgeGroup_Bern / Berne_20-29', 'Canton_AgeGroup_Bern / Berne_30-39', 'Canton_AgeGroup_Bern / Berne_40-49', 'Canton_AgeGroup_Bern / Berne_50-59', 'Canton_AgeGroup_Bern / Berne_60-69', 'Canton_AgeGroup_Bern / Berne_70-79', 'Canton_AgeGroup_Bern / Berne_80-89', 'Canton_AgeGroup_Fribourg / Freiburg_10-19', 'Canton_AgeGroup_Fribourg / Freiburg_20-29', 'Canton_AgeGroup_Fribourg / Freiburg_30-39', 'Canton_AgeGroup_Fribourg / Freiburg_40-49', 'Canton_AgeGroup_Fribourg / Freiburg_50-59', 'Canton_AgeGroup_Fribourg / Freiburg_60-69', 'Canton_AgeGroup_Fribourg / Freiburg_70-79', 'Canton_AgeGroup_Fribourg / Freiburg_80-89', 'Canton_AgeGroup_Genève_10-19', 'Canton_AgeGroup_Genève_20-29', 'Canton_AgeGroup_Genève_30-39', 'Canton_AgeGroup_Genève_40-49', 'Canton_AgeGroup_Genève_50-59', 'Canton_AgeGroup_Genève_60-69', 'Canton_AgeGroup_Genève_70-79', 'Canton_AgeGroup_Genève_80-89', 'Canton_AgeGroup_Glarus_10-19', 'Canton_AgeGroup_Glarus_20-29', 'Canton_AgeGroup_Glarus_30-39', 'Canton_AgeGroup_Glarus_40-49', 'Canton_AgeGroup_Glarus_50-59', 'Canton_AgeGroup_Glarus_60-69', 'Canton_AgeGroup_Glarus_70-79', 'Canton_AgeGroup_Glarus_80-89', 'Canton_AgeGroup_Graubünden / Grigioni / Grischun_10-19', 'Canton_AgeGroup_Graubünden / Grigioni / Grischun_20-29', 'Canton_AgeGroup_Graubünden / Grigioni / Grischun_30-39', 'Canton_AgeGroup_Graubünden / Grigioni / Grischun_40-49', 'Canton_AgeGroup_Graubünden / Grigioni / Grischun_50-59', 'Canton_AgeGroup_Graubünden / Grigioni / Grischun_60-69', 'Canton_AgeGroup_Graubünden / Grigioni / Grischun_70-79', 'Canton_AgeGroup_Graubünden / Grigioni / Grischun_80-89', 'Canton_AgeGroup_Jura_10-19', 'Canton_AgeGroup_Jura_20-29', 'Canton_AgeGroup_Jura_30-39', 'Canton_AgeGroup_Jura_40-49', 'Canton_AgeGroup_Jura_50-59', 'Canton_AgeGroup_Jura_60-69', 'Canton_AgeGroup_Jura_70-79', 'Canton_AgeGroup_Jura_80-89', 'Canton_AgeGroup_Luzern_10-19', 'Canton_AgeGroup_Luzern_20-29', 'Canton_AgeGroup_Luzern_30-39', 'Canton_AgeGroup_Luzern_40-49', 'Canton_AgeGroup_Luzern_50-59', 'Canton_AgeGroup_Luzern_60-69', 'Canton_AgeGroup_Luzern_70-79', 'Canton_AgeGroup_Luzern_80-89', 'Canton_AgeGroup_Neuchâtel_10-19', 'Canton_AgeGroup_Neuchâtel_20-29', 'Canton_AgeGroup_Neuchâtel_30-39', 'Canton_AgeGroup_Neuchâtel_40-49', 'Canton_AgeGroup_Neuchâtel_50-59', 'Canton_AgeGroup_Neuchâtel_60-69', 'Canton_AgeGroup_Neuchâtel_70-79', 'Canton_AgeGroup_Neuchâtel_80-89', 'Canton_AgeGroup_Nidwalden_10-19', 'Canton_AgeGroup_Nidwalden_20-29', 'Canton_AgeGroup_Nidwalden_30-39', 'Canton_AgeGroup_Nidwalden_40-49', 'Canton_AgeGroup_Nidwalden_50-59', 'Canton_AgeGroup_Nidwalden_60-69', 'Canton_AgeGroup_Nidwalden_70-79', 'Canton_AgeGroup_Nidwalden_80-89', 'Canton_AgeGroup_Obwalden_10-19', 'Canton_AgeGroup_Obwalden_20-29', 'Canton_AgeGroup_Obwalden_30-39', 'Canton_AgeGroup_Obwalden_40-49', 'Canton_AgeGroup_Obwalden_50-59', 'Canton_AgeGroup_Obwalden_60-69', 'Canton_AgeGroup_Obwalden_70-79', 'Canton_AgeGroup_Obwalden_80-89', 'Canton_AgeGroup_Schaffhausen_10-19', 'Canton_AgeGroup_Schaffhausen_20-29', 'Canton_AgeGroup_Schaffhausen_30-39', 'Canton_AgeGroup_Schaffhausen_40-49', 'Canton_AgeGroup_Schaffhausen_50-59', 'Canton_AgeGroup_Schaffhausen_60-69', 'Canton_AgeGroup_Schaffhausen_70-79', 'Canton_AgeGroup_Schaffhausen_80-89', 'Canton_AgeGroup_Schwyz_10-19', 'Canton_AgeGroup_Schwyz_20-29', 'Canton_AgeGroup_Schwyz_30-39', 'Canton_AgeGroup_Schwyz_40-49', 'Canton_AgeGroup_Schwyz_50-59', 'Canton_AgeGroup_Schwyz_60-69', 'Canton_AgeGroup_Schwyz_70-79', 'Canton_AgeGroup_Schwyz_80-89', 'Canton_AgeGroup_Solothurn_10-19', 'Canton_AgeGroup_Solothurn_20-29', 'Canton_AgeGroup_Solothurn_30-39', 'Canton_AgeGroup_Solothurn_40-49', 'Canton_AgeGroup_Solothurn_50-59', 'Canton_AgeGroup_Solothurn_60-69', 'Canton_AgeGroup_Solothurn_70-79', 'Canton_AgeGroup_Solothurn_80-89', 'Canton_AgeGroup_St. Gallen_10-19', 'Canton_AgeGroup_St. Gallen_20-29', 'Canton_AgeGroup_St. Gallen_30-39', 'Canton_AgeGroup_St. Gallen_40-49', 'Canton_AgeGroup_St. Gallen_50-59', 'Canton_AgeGroup_St. Gallen_60-69', 'Canton_AgeGroup_St. Gallen_70-79', 'Canton_AgeGroup_St. Gallen_80-89', 'Canton_AgeGroup_Thurgau_10-19', 'Canton_AgeGroup_Thurgau_20-29', 'Canton_AgeGroup_Thurgau_30-39', 'Canton_AgeGroup_Thurgau_40-49', 'Canton_AgeGroup_Thurgau_50-59', 'Canton_AgeGroup_Thurgau_60-69', 'Canton_AgeGroup_Thurgau_70-79', 'Canton_AgeGroup_Thurgau_80-89', 'Canton_AgeGroup_Ticino_10-19', 'Canton_AgeGroup_Ticino_20-29', 'Canton_AgeGroup_Ticino_30-39', 'Canton_AgeGroup_Ticino_40-49', 'Canton_AgeGroup_Ticino_50-59', 'Canton_AgeGroup_Ticino_60-69', 'Canton_AgeGroup_Ticino_70-79', 'Canton_AgeGroup_Ticino_80-89', 'Canton_AgeGroup_Uri_10-19', 'Canton_AgeGroup_Uri_20-29', 'Canton_AgeGroup_Uri_30-39', 'Canton_AgeGroup_Uri_40-49', 'Canton_AgeGroup_Uri_50-59', 'Canton_AgeGroup_Uri_60-69', 'Canton_AgeGroup_Uri_70-79', 'Canton_AgeGroup_Uri_80-89', 'Canton_AgeGroup_Valais / Wallis_10-19', 'Canton_AgeGroup_Valais / Wallis_20-29', 'Canton_AgeGroup_Valais / Wallis_30-39', 'Canton_AgeGroup_Valais / Wallis_40-49', 'Canton_AgeGroup_Valais / Wallis_50-59', 'Canton_AgeGroup_Valais / Wallis_60-69', 'Canton_AgeGroup_Valais / Wallis_70-79', 'Canton_AgeGroup_Valais / Wallis_80-89', 'Canton_AgeGroup_Vaud_10-19', 'Canton_AgeGroup_Vaud_20-29', 'Canton_AgeGroup_Vaud_30-39', 'Canton_AgeGroup_Vaud_40-49', 'Canton_AgeGroup_Vaud_50-59', 'Canton_AgeGroup_Vaud_60-69', 'Canton_AgeGroup_Vaud_70-79', 'Canton_AgeGroup_Vaud_80-89', 'Canton_AgeGroup_Zug_10-19', 'Canton_AgeGroup_Zug_20-29', 'Canton_AgeGroup_Zug_30-39', 'Canton_AgeGroup_Zug_40-49', 'Canton_AgeGroup_Zug_50-59', 'Canton_AgeGroup_Zug_60-69', 'Canton_AgeGroup_Zug_70-79', 'Canton_AgeGroup_Zug_80-89', 'Canton_AgeGroup_Zürich_10-19', 'Canton_AgeGroup_Zürich_20-29', 'Canton_AgeGroup_Zürich_30-39', 'Canton_AgeGroup_Zürich_40-49', 'Canton_AgeGroup_Zürich_50-59', 'Canton_AgeGroup_Zürich_60-69', 'Canton_AgeGroup_Zürich_70-79', 'Canton_AgeGroup_Zürich_80-89']

# Initialize the DataFrame with all values set to 0
cantongroup = pd.DataFrame(columns=features)
cantongroup.loc[0] = 0  # Set all the rows (initially 0)

    
net_migration = st.sidebar.number_input('Net Migration per Age Group', value=0.0, step=1.0)
population = st.sidebar.number_input('Population per Age Group', value=10000.0, step=1000.0)
death = st.sidebar.number_input('Death per Age Group', value=0.0, step=1.0)
births = st.sidebar.number_input('Births per Age Group', value=0.0, step=1.0)
divorces = st.sidebar.number_input('Divorces per Age Group', value=0.0, step=1.0)
unemployment = st.sidebar.number_input('Unemployment Rate (%)', value=0.0, step=0.1)
gdp_pc = st.sidebar.number_input('GDP per Capita', value=0.0, step=1000.0)

# Dummy variables


# Merging DataFrames on the 'ID' colu    
canton = st.sidebar.selectbox('Select Canton', options=cantons)
age_group = st.sidebar.selectbox('Select Age Group', options=age_groups)
feature_name =  'Canton_AgeGroup_'+canton+'_'+age_group
def user_input_features():
    feature_name = 'Canton_AgeGroup_'+canton+'_'+age_group
    
    if feature_name in cantongroup.columns:
        cantongroup[feature_name] = 1  # Set the selected feature to 1
        print(f"Feature '{feature_name}' updated to 1.")
    else:
        print(f"Feature '{feature_name}' does not exist.")
    
    
    data = {
        'Net Migration': [net_migration],
        'Population': [population],
        'Death': [death],
        'Births': [births],
        'Divorces': [divorces],
        'unemployment': [unemployment],
        'GDP_pc': [gdp_pc]
    }
    df2 = pd.DataFrame(data)
    return pd.concat([df2, cantongroup], axis=1)

user_input = user_input_features()

# Custom CSS for Global Styles

 # Main app title
st.title("Union Insights")

if st.button('Predict Marriages'):
    try:
        prediction = model.predict(user_input)
        round = int(np.ceil(prediction[0]))
        st.subheading(f'The predicted number of marriages in two years from now for {canton} in the age group {age_group} is:')
        st.markdown(f'<h1>{round}</h1>', unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Prediction error: {e}")

# Sidebar configuration
st.sidebar.header("Filters and Options")

# Load the uploaded dataset
data = pd.read_csv('X_data.csv')

cantons = data['Canton'].unique().tolist()
age_groups = data['Age Group'].unique().tolist()

# Select All options for cantons and age groups
cantons_with_select_all = ["Select All"] + cantons
age_groups_with_select_all = ["Select All"] + age_groups

# Canton selection with "Select All"
selected_cantons = st.sidebar.multiselect(
    "Select Cantons:", options=cantons_with_select_all, default=[]
)
if "Select All" in selected_cantons:
    selected_cantons = cantons
else:
    selected_cantons = [canton for canton in selected_cantons if canton != "Select All"]

# Age group selection with "Select All"
selected_age_groups = st.sidebar.multiselect(
    "Select Age Groups:", options=age_groups_with_select_all, default=[]
)
if "Select All" in selected_age_groups:
    selected_age_groups = age_groups
else:
    selected_age_groups = [age_group for age_group in selected_age_groups if age_group != "Select All"]

# Year selection slider
selected_year = st.sidebar.slider("Select the Year:", min_value=int(data['Year'].min()), max_value=int(data['Year'].max()), step=1)

# Chart type selection
graph_type = st.sidebar.selectbox("Chart Type:", ["Bar", "Pie", "Line"])

# View options for location, wedding trends, and distribution
view_option_location = st.sidebar.radio(
    "Select View Mode for Location Recommendations:",
    options=["By Age Group", "By Canton", "Both"],
    key="view_option_location"
)
top_n = st.sidebar.slider("Number of Regions to Display:", min_value=1, max_value=10, value=5)


view_option_wedding_distribution = st.sidebar.radio(
    "Select View Mode for Wedding Distribution:",
    options=["By Age Group", "By Canton", "Both"],
    key="view_option_wedding_distribution"
)

# Filter data based on selected options
filtered_data = data[
    (data['Canton'].isin(selected_cantons)) & 
    (data['Age Group'].isin(selected_age_groups)) &
    (data['Year'] == selected_year)
]

# Section 1: Location Recommendations based on selected view option
if view_option_location == "By Age Group":
    st.subheader("📍 Location Recommendations by Age Group")
    popular_locations = (
        filtered_data.groupby(["Age Group"])["marriages"]
        .sum()
        .reset_index()
        .sort_values(by="marriages", ascending=False)
        .head(top_n)
    )
    st.table(popular_locations)

elif view_option_location == "By Canton":
    st.subheader("📍 Location Recommendations by Canton")
    popular_locations = (
        filtered_data.groupby("Canton")["marriages"]
        .sum()
        .reset_index()
        .sort_values(by="marriages", ascending=False)
        .head(top_n)
    )
    st.table(popular_locations)

else:
    st.subheader("📍 Location Recommendations by Age Group and Canton")
    popular_locations = (
        filtered_data.groupby(["Age Group", "Canton"])["marriages"]
        .sum()
        .reset_index()
        .sort_values(by="marriages", ascending=False)
        .head(top_n)
    )
    st.table(popular_locations)

   # Section 2: Wedding Distribution
# Demographic Views based on selected view option
if view_option_wedding_distribution == "By Age Group":
    st.subheader("👥 Wedding Distribution by Age Group")
elif view_option_wedding_distribution == "By Canton":
    st.subheader("👥 Wedding Distribution by Canton")
elif view_option_wedding_distribution == "Both":
    st.subheader("👥 Wedding Distribution by Age Group and Canton")

# Chart type logic (Bar, Pie, or Line) for all view options
if graph_type == "Bar":
    if view_option_wedding_distribution == "By Age Group":
        fig_bar = px.bar(
            filtered_data, 
            x="Age Group",  # Adjusted to match the case of the column
            y="marriages",  # Adjusted to match the case of the column
            color="Age Group",
            title="Weddings by Age Group",
            color_discrete_sequence=px.colors.sequential.Pinkyl
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    elif view_option_wedding_distribution == "By Canton":
        fig_bar = px.bar(
            filtered_data, 
            x="Canton",  # Adjusted to match the case of the column
            y="marriages",  # Adjusted to match the case of the column
            color="Canton",
            title="Weddings by Canton",
            color_discrete_sequence=px.colors.sequential.Pinkyl
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    elif view_option_wedding_distribution == "Both":
        # Combine "Age Group" and "Canton" into a new column
        filtered_data["Age_Canton_Combined"] = filtered_data["Age Group"] + " - " + filtered_data["Canton"]
        
        fig_bar = px.bar(
            filtered_data, 
            x="Age_Canton_Combined",  # New combined column for x-axis
            y="marriages",  # Adjusted to match the case of the column
            color="Canton",
            title="Weddings by Age Group and Canton",
            color_discrete_sequence=px.colors.sequential.Pinkyl
        )
        st.plotly_chart(fig_bar, use_container_width=True)

elif graph_type == "Pie":
    if view_option_wedding_distribution == "By Age Group":
        fig_pie = px.pie(
            filtered_data, 
            names="Age Group",  # Adjusted to match the case of the column
            values="marriages",  # Adjusted to match the case of the column
            title="Wedding Distribution by Age Group",
            color_discrete_sequence=px.colors.sequential.Pinkyl
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    elif view_option_wedding_distribution == "By Canton":
        fig_pie = px.pie(
            filtered_data, 
            names="Canton",  # Adjusted to match the case of the column
            values="marriages",  # Adjusted to match the case of the column
            title="Wedding Distribution by Canton",
            color_discrete_sequence=px.colors.sequential.Pinkyl
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    elif view_option_wedding_distribution == "Both":
        # Combine "Age Group" and "Canton" into a new column
        filtered_data["Age_Canton_Combined"] = filtered_data["Age Group"] + " - " + filtered_data["Canton"]
        
        fig_pie = px.pie(
            filtered_data, 
            names="Age_Canton_Combined",  # New combined column for Pie Chart
            values="marriages",  # Adjusted to match the case of the column
            title="Wedding Distribution by Age Group and Canton",
            color_discrete_sequence=px.colors.sequential.Pinkyl
        )
        st.plotly_chart(fig_pie, use_container_width=True)

elif graph_type == "Line":
    if view_option_wedding_distribution == "By Age Group":
        fig_line_age = px.line(
            filtered_data, 
            x="Age Group",  # Adjusted to match the case of the column
            y="marriages",  # Adjusted to match the case of the column
            color="Canton",
            title="Weddings by Age Group",
            color_discrete_sequence=px.colors.sequential.Pinkyl
        )
        st.plotly_chart(fig_line_age, use_container_width=True)

    elif view_option_wedding_distribution == "By Canton":
        fig_line_canton = px.line(
            filtered_data, 
            x="Canton",  # Adjusted to match the case of the column
            y="marriages",  # Adjusted to match the case of the column
            color="Age Group",
            title="Weddings by Canton",
            color_discrete_sequence=px.colors.sequential.Pinkyl
        )
        st.plotly_chart(fig_line_canton, use_container_width=True)

    elif view_option_wedding_distribution == "Both":
        # Combine "Age Group" and "Canton" into a new column
        filtered_data["Age_Canton_Combined"] = filtered_data["Age Group"] + " - " + filtered_data["Canton"]
        
        fig_line_both = px.line(
            filtered_data, 
            x="Age_Canton_Combined",  # New combined column for Line Chart
            y="marriages",  # Adjusted to match the case of the column
            color="Canton",  # Color differentiation by canton
            title="Weddings by Age Group and Canton",
            color_discrete_sequence=px.colors.sequential.Pinkyl
        )
        st.plotly_chart(fig_line_both, use_container_width=True)


# Convert filtered data to CSV format for downloading
csv = filtered_data.to_csv(index=False)  # Converts the DataFrame into a downloadable CSV format

# Add a download button for the generated CSV
st.download_button(
     label="Download CSV",  # Button label for the user
     data=csv,  # CSV data to be downloaded
     file_name="marriage.csv",  # Suggested file name for the download
     mime="text/csv"  
 )

# Add a footer section for branding or additional app details
st.markdown("---") 
st.markdown(
     f"<p style='color:{TEXT_COLOR};'>App developed for Swiss Marriage Data Analysis 🇨🇭</p>", 
     unsafe_allow_html=True  
 )
st.markdown(
    """
    <style>
    .st-emotion-cache-5drf04 {
        width: 130px;  /* Set a fixed width for the logo */
        height: auto;  /* Keep the aspect ratio intact */
        margin: 10px;   /* Add some space around the logo */
    }
    </style>
    """, unsafe_allow_html=True
)



st.markdown(f"""
    <style>
        body {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
        }}
        .css-1d391kg p, .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3 {{
            color: {TEXT_COLOR};
        }}
        .stButton button {{
            background-color: {PRIMARY_COLOR};
            color: {BACKGROUND_COLOR};
            border: none;
            border-radius: 4px;
        }}
        .stButton button:hover {{
            background-color: {TEXT_COLOR};
        }}
        .stSlider {{
            color: {PRIMARY_COLOR};
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;  /* Green */
        color: ;               /* White text */
        font-size: 16px;            /* Text size */
        border: none;               /* No border */
        border-radius: 12px;        /* Rounded corners */
        padding: 10px 20px;         /* Padding */
        cursor: pointer;           /* Pointer cursor on hover */
        transition: background-color 0.3s ease; /* Smooth transition */
    }white
    .stButton>button:hover {
        background-color: #45a049;  /* Darker green on hover */
    }
    .st-emotion-cache-1jicfl2 {
        padding-top: 5rem
    }
    .st-emotion-cache-12fmjuu{
        background-color: rgb(255 245 232)
    }
    .st-emotion-cache-19u4bdk{
        top: 0;
        left: 0
    }
    .st-emotion-cache-ausnhs{
        margin-top: 15px
    }
    .st-emotion-cache-15ecox0{
        top: 1rem
    }
    .st-emotion-cache-hzo1qh{
        top: 0.8rem
    }
    h2 {
        padding: 0;
        margin-bottom: 25px
    }
    </style>
""", unsafe_allow_html=True)
st.markdown(f"""
    <style>
        body {{
            background-color: {BACKGROUND_COLOR};
            color: {TEXT_COLOR};
        }}
        .css-1d391kg p, .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3 {{
            color: {TEXT_COLOR};
        }}
        .stButton button {{
            background-color: #ff00ca;
            color: white;
            border: none;
            border-radius: 4px;
        }}
        .stButton button:hover {{
            background-color: {TEXT_COLOR};
        }}
        .stSlider {{
            color: {PRIMARY_COLOR};
        }}
    </style>
""", unsafe_allow_html=True)
