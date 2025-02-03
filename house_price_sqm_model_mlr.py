import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression

df = pd.read_excel(f"C:/Users/danie/OneDrive/Work/Career/Coding/Folio/ML/found_ml_projects/data.xlsx")

#print(df)
#print(df.info())
# Check for null values
df.isna().sum()

# Exploratory data visualisation
scatter_plot_sqm = px.scatter(data_frame= df, x=df['SQM'], y=df['Price'])
scatter_plot_bedrooms = px.scatter(data_frame= df, x=df['Bedrooms'], y=df['Price'])

# scatter_plot_sqm.show()
# scatter_plot_bedrooms.show()

# Create model isntance:
mlr_mdl = LinearRegression()

# Set x and y variables
X = df[['Car parks', 'SQM', 'Bedrooms', 'Bathrooms']]
Y = df['Price']

# print(X)
# print(Y)

# Fit the model
mlr_mdl.fit(X, Y)

# Print the coefficients for each feature
coefficients = mlr_mdl.coef_
features = X.columns

# Print the feature importance (coefficients), so for example if sqm = 950, then for each additional square metre you can expect $950 of value to be added to the property
for feature, coef in zip(features, coefficients):
    print(f"{feature}: {coef:.4f}")

# Make predictions with the model
car_parks = 1
sqm = 155
bedrooms = 2
bathrooms = 1

predicted_price = mlr_mdl.predict([[car_parks, sqm, bedrooms, bathrooms]])

print(f"Predicted Price: ${predicted_price[0]:,.2f}")
