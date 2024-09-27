import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Video_Game_Sales_Data.csv')  # replace with actual filename

# Load the data in and check it has loaded correctly.
def task1():
    print(df.head(10)) #Check the first 10 rows to make sure data loads correctly
    print(df.describe())

    #Optional - but useful!
    print(df.isnull().sum()) # Check if there are any NULL (empty) values

# Filter data by platform: Select all games released on the "PS5" platform. 
# Display the top 5 PS5 games with the highest revenue.
def task2():
    ps5_games = df[df['Platform'] == 'PS5'] # Filter only PS5 data.
    print(ps5_games.nlargest(5, 'Revenue (Million $)')) # Print 5 largest values for Revenue

# Group and sort data
# Group by platform and display total units sold for each.
def task3():
    total_units_per_platform = df.groupby('Platform')['Units Sold (Millions)'].sum().sort_values(ascending=False)
    print(total_units_per_platform)

# Create a bar chart
# Group by Genre and caluclate total revenue for each
# Display in a bar chart to visualise which has generated the most revenue
def task4():
    revenue_by_genre = df.groupby('Genre')['Revenue (Million $)'].sum()
    revenue_by_genre.plot(kind='bar')
    plt.title('Total Revenue by Genre')
    plt.xlabel('Genre')
    plt.ylabel('Revenue (Million $)')
    plt.show()

# Create a line plot
# Group the data by year and caluclate total units sold each year
# Create a line plot to show how video games sales have changed over time
def task5():
    units_sold_per_year = df.groupby('Year')['Units Sold (Millions)'].sum()
    units_sold_per_year.plot(kind='line', marker='o')
    plt.title('Total Units Sold Over Time')
    plt.xlabel('Year')
    plt.ylabel('Units Sold (Millions)')
    plt.grid(True)
    plt.show()

#task1()
#task2()
#task3()
#task4()
task5()