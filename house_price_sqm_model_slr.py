import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_excel(f"C:/Users/danie/OneDrive/Work/Career/Coding/Folio/ML/found_ml_projects/data.xlsx")

#print(df)

Y_train = df[['Price']]
X_train = df[['SQM']]

# Initialize and fit the model
model = LinearRegression()
model.fit(X_train, Y_train)
compute_cost = model.fit(X_train, Y_train)

# Coefficients
slope = model.coef_[0][0]
intercept = model.intercept_[0]

print(f"Slope (w) value: {slope}") #w value
print(f"Intercept (b) value: {intercept}") #b intercept value

#X_input = [[210]]

# Predictions
#prediction = model.predict(X_input)
#print(f"For {X_input} square metres the model estimates the property is worth {prediction}")


###################################Visualisation

#Create scatter plot for initial values
scatter_plot = px.scatter(data_frame= df, x='SQM', y='Price')
#scatter_plot.show()

#Create column in df for predicted values:
df['Predicted_Price'] = model.predict(X_train)

# Add the line of best fit
line_trace = go.Scatter(
    x=df['SQM'],
    y=df['Predicted_Price'],
    mode='lines',
    name='Line of Best Fit',
    line=dict(color='red'),
    xaxis='x',
    yaxis='y'
)

# Combine the scatter plot with the line of best fit
fig = go.Figure(data=list(scatter_plot.data) + [line_trace])

# Creating layout with overall title
layout = go.Layout(
    title='Single linear regression house price ($m) vs square metres',
    xaxis=dict(title='Square metres'),
    yaxis=dict(title='House price ($m)')
)

# Update the figure with layout
fig.update_layout(layout)

# Add annotations for w and b
annotation_text = f'Slope (w): {slope:.2f}<br>Intercept (b): {intercept:.2f}'

# Add annotation with w and b to the plot
fig.add_annotation(
    x=0.05,  # Position the annotation at the left
    y=0.95,  # Position it near the top
    xref="paper",  # Use paper coordinates (normalized space from 0 to 1)
    yref="paper",  # Use paper coordinates
    text=annotation_text,  # The text to display
    showarrow=False,  # No arrow needed
    font=dict(size=14, color="black"),  # Font settings
    align="left"  # Align text to the left
)

# Show the plot
fig.show()

