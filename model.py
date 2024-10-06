import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import plotly.graph_objs as go

# Function to load data
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data():
    # Load your dataset here
    # Replace with the actual path to your dataset
    data = pd.read_csv('C:\\Users\\pdube\\OneDrive\\Desktop\\NASA\\main.js\\test2\\neo_data.csv')
    return data

# Function to preprocess data
def preprocess_data(data):
    # Handle missing values
    # For example, you can fill missing values with the mean for numerical columns
    numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns
    for col in numerical_cols:
        data[col].fillna(data[col].mean(), inplace=True)
    
    # For categorical columns, fill missing values with the mode
    categorical_cols = data.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        data[col].fillna(data[col].mode()[0], inplace=True)

    # Encode categorical variables using Label Encoding
    label_encoder = LabelEncoder()
    for col in categorical_cols:
        data[col] = label_encoder.fit_transform(data[col])

    return data


# Function to train model
def train_model(data):
    # Debugging: Print the columns in the DataFrame
    print(data.columns)
    
    # Define the target column name correctly
    target_column_name = 'is_hazardous'  # Change this to your actual target column name

    # Check if the target column exists
    if target_column_name not in data.columns:
        raise KeyError(f"{target_column_name} not found in the DataFrame")

    X = data.drop(target_column_name, axis=1)  # Features
    y = data[target_column_name]  # Target variable

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Model training (example using RandomForestClassifier)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Predictions and accuracy
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    return model, accuracy, X_test, predictions

# Function to visualize orbital paths in 3D using Plotly
def plot_orbital_paths_3d(X_test, predictions):
    fig = go.Figure()

    # Assuming 'x', 'y', 'z' are columns for the positions in the dataset
    for i in range(len(predictions)):
        fig.add_trace(go.Scatter3d(
            x=X_test['x'].iloc[i],
            y=X_test['y'].iloc[i],
            z=X_test['z'].iloc[i],  # Use the z-coordinate if available
            mode='markers+text',
            marker=dict(size=5),
            text=f'Prediction {i}: {predictions[i]}',
            textposition='top center'
        ))

    fig.update_layout(
        title='3D Orbital Paths of Celestial Bodies',
        scene=dict(
            xaxis_title='X Position',
            yaxis_title='Y Position',
            zaxis_title='Z Position'
        ),
        margin=dict(l=0, r=0, b=0, t=40),
    )

    st.plotly_chart(fig)

# Function to update orrery based on user controls
def update_orbital_paths(data, selected_objects, speed, timeline):
    # Filtering the data based on selected celestial objects
    filtered_data = data[data['object_name'].isin(selected_objects)]
    
    # Simulate updating positions based on timeline and speed
    # This is a placeholder for actual orbital propagation logic
    # For example, you might update the position based on Keplerian parameters here
    # Adjust positions based on speed and timeline
    time_factor = timeline / 100  # Normalize timeline for simulation
    filtered_data['x'] += filtered_data['x'] * time_factor * speed
    filtered_data['y'] += filtered_data['y'] * time_factor * speed
    filtered_data['z'] += filtered_data['z'] * time_factor * speed

    return filtered_data

# Streamlit UI
st.title("Interactive Orrery with ML Models and 3D Visualization")

# Load and preprocess data
data = load_data()
processed_data = preprocess_data(data)

# Train model on button click
if st.button('Train Model'):
    model, accuracy, X_test, predictions = train_model(processed_data)
    st.write(f'Model trained with accuracy: {accuracy:.2f}')
    
    # Display predictions
    st.subheader("Model Predictions")
    st.write(predictions)

    # Plot orbital paths in 3D
    st.subheader("3D Orbital Path Visualization")
    plot_orbital_paths_3d(X_test, predictions)

# User controls for interaction
st.sidebar.header("Orrery Controls")

# Select celestial bodies to display
selected_objects = st.sidebar.multiselect("Select Celestial Objects", options=data['object_name'].unique())

# Simulation speed control
simulation_speed = st.sidebar.slider("Simulation Speed", min_value=1, max_value=10, value=5)

# Timeline control
timeline = st.sidebar.slider("Timeline", min_value=0, max_value=100, value=0)

# Update Orrery based on selected controls
if st.sidebar.button("Update Orrery"):
    if selected_objects:
        updated_positions = update_orbital_paths(processed_data, selected_objects, simulation_speed, timeline)
        st.subheader("Updated Orbital Path Visualization")
        plot_orbital_paths_3d(updated_positions, [0]*len(updated_positions))  # Placeholder for predictions

# Additional information about the app
st.sidebar.info("This interactive orrery uses machine learning to predict the positions of celestial bodies. "
                "Use the controls to customize your view and simulation settings.")
