import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample historical data (Replace with your own data)
# Format: [time (days), x_position, y_position, z_position]
data = {
    'time': [0, 1, 2, 3, 4, 5],
    'x_position': [1, 1.1, 1.2, 1.3, 1.5, 1.6],
    'y_position': [0, 0.1, 0.2, 0.3, 0.4, 0.5],
    'z_position': [0, 0.05, 0.1, 0.15, 0.2, 0.25]
}

df = pd.DataFrame(data)

# Machine Learning Model
model = LinearRegression()
X = df[['time']]
y = df[['x_position', 'y_position', 'z_position']]

model.fit(X, y)

# User input for prediction
st.title('Orbit Prediction for Celestial Bodies')
days_ahead = st.number_input('Days Ahead to Predict:', min_value=1, value=1)

# Make prediction
future_time = np.array([[max(df['time']) + days_ahead]])
predicted_position = model.predict(future_time)

st.subheader(f'Predicted Position in {days_ahead} days:')
st.write(f'X Position: {predicted_position[0][0]:.2f}')
st.write(f'Y Position: {predicted_position[0][1]:.2f}')
st.write(f'Z Position: {predicted_position[0][2]:.2f}')

# Plotting
fig, ax = plt.subplots()
ax.plot(df['time'], df['x_position'], label='X Position', marker='o')
ax.plot(df['time'], df['y_position'], label='Y Position', marker='o')
ax.plot(df['time'], df['z_position'], label='Z Position', marker='o')

# Prepare data for the predicted position
predicted_x = predicted_position[0][0]
predicted_y = predicted_position[0][1]
predicted_z = predicted_position[0][2]
predicted_time = max(df['time']) + days_ahead

# Scatter the predicted position
ax.scatter([predicted_time], [predicted_x], color='red', label='Predicted X Position', s=100)
ax.scatter([predicted_time], [predicted_y], color='green', label='Predicted Y Position', s=100)
ax.scatter([predicted_time], [predicted_z], color='blue', label='Predicted Z Position', s=100)

ax.set_xlabel('Time (days)')
ax.set_ylabel('Position')
ax.set_title('Orbit Prediction')
ax.legend()
st.pyplot(fig)
