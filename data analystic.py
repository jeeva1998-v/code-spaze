import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset (example: Titanic dataset)
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# === 1. Basic Data Analysis ===
print("Dataset Info:")
print(df.info())  # Display the structure of the dataset
print("\nSummary Statistics:")
print(df.describe())  # Summary statistics

# === 2. Insights & Visualizations ===
# Example Insight: Passenger Class Distribution
class_distribution = df['Pclass'].value_counts()
print("\nPassenger Class Distribution:\n", class_distribution)

# === 3. Static Visualization Using Matplotlib ===
plt.figure(figsize=(8, 5))
class_distribution.plot(kind='bar', color='skyblue')
plt.title('Passenger Class Distribution on the Titanic')
plt.xlabel('Class')
plt.ylabel('Number of Passengers')
plt.show()

# Static Histogram: Age Distribution of Passengers
plt.figure(figsize=(8, 5))
df['Age'].dropna().plot(kind='hist', bins=20, color='lightgreen')
plt.title('Age Distribution of Passengers on the Titanic')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# === 4. Interactive Visualizations Using Plotly ===
# Interactive Pie Chart for Passenger Class Distribution
fig = px.pie(df, names='Pclass', title='Passenger Class Distribution')
fig.show()

# Interactive Scatter Plot (Age vs. Fare)
fig = px.scatter(df, x='Age', y='Fare', color='Pclass', title='Age vs Fare (colored by Class)',
                 labels={"Pclass": "Passenger Class"}, hover_data=['Name'])
fig.show()

# Interactive Bar Chart for Passenger Survival Count by Class
survival_by_class = df.groupby('Pclass')['Survived'].sum().reset_index()
fig = px.bar(survival_by_class, x='Pclass', y='Survived', title='Survival Count by Passenger Class',
             labels={'Pclass': 'Passenger Class', 'Survived': 'Number of Survivors'})
fig.show()
