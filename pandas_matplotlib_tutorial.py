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
    revenue_by_genre.plot(kind='bar') # plot our organised data
    plt.title('Total Revenue by Genre') # Give our graph a title
    plt.xlabel('Genre') # Label the X axis
    plt.ylabel('Revenue (Million $)') # Label the Y axis
    plt.show() # display our graph

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

# Analyze Best-Selling Games
# Identify the top 10 best-selling games (by units sold).
# Display the Game Title, Platform, and Units Sold (Millions) for each of the top 10 games.
def task6():
    top_10_games = df.nlargest(10, 'Units Sold (Millions)')[['Game Title', 'Platform', 'Units Sold (Millions)']]
    print(top_10_games)

# Scatter Plot of Revenue vs Units Sold
# Create a scatter plot to show the relationship between Units Sold (Millions) and Revenue (Million $).
# Add labels for the axes and a title.
def task7():
    # alpha defines the opacity of the points on the graph.
    # 1 = solid (opaque), 0 = fully transparent (invisible)
    df.plot(kind='scatter', x='Units Sold (Millions)', y='Revenue (Million $)', alpha=0.5) 
    plt.title('Revenue vs Units Sold')
    plt.xlabel('Units Sold (Millions)')
    plt.ylabel('Revenue (Million $)')
    plt.show()

# Distribution of Game Releases per Year
# Plot a histogram to show how many games were released each year.
def task8():
    # bins is how many "intervals" we want to group into. 
    # Since we have a range of 14 years in our data, we want 14 separate bins to group our data by.
    df['Year'].plot(kind='hist', bins=14, edgecolor='black') 
    plt.title('Distribution of Game Releases per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Games Released')
    plt.show()


# Plot a pie chart showing the distribution of games released by Genre.
def task9():
    # Grouping by 'Genre' and counting the number of titles in each genre
    genre_counts = df['Genre'].value_counts() # value_counts() counts a total for each group.

    # Creating a pie chart
    plt.figure(figsize=(8, 8)) # figsize is the dimension of the chart.
    # Keep the arguments for figsize the same if you want a perfect circle pie chart.
    plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90)
    # labels=genre_counts.index: Labels the slices with the genre names.
    # autopct='%1.1f%%': Displays the percentage for each slice.
    # startangle=90: Rotates the pie chart to start from a different angle (90 degrees in this case).
    plt.title('Distribution of Game Titles by Genre')
    plt.axis('equal')  # Equal aspect ratio ensures that the pie chart is a circle
    plt.show()


# Uncomment the task(s) below that you want to run
#task1()
#task2()
#task3()
#task4()
#task5()
#task6()
#task7()
#task8()
#task9()