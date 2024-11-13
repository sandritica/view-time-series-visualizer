import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates =['date'])
df.set_index('date', inplace=True)

print(df)

# Clean data
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]


def draw_line_plot():
    # Draw line plot
     # Create the line plot
    fig = plt.figure(figsize=(14, 8))

   
    plt.plot(df.index, df['value'], color='tab:red')

  # Customize the plot
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Page Views', fontsize=14)
    plt.grid(True)
  

  # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)

  # Display the plot
   # plt.show()
   


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig
 
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df.groupby([df.index.year, df.index.month]).mean().unstack()
    df_bar.columns = months
    df_bar.index.name = "Years"
    df_bar.columns.name = 'Months'
   
    print(df_bar)
    Year = df_bar.index.tolist()
    print(Year)
    ax = df_bar.plot(kind='bar', figsize=(12, 6), width=0.8)
      
    
    plt.title('Average Daily Page Views by Month and Year', fontsize=12)
    plt.xlabel('Years', fontsize=8)
    plt.ylabel('Average Page Views', fontsize=8)
    plt.tight_layout()
    #plt.show()
    
    fig = ax.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    
    
    return fig
    
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    df_box['month'] = pd.Categorical(df_box['month'], categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                                                                 "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], ordered=True)
    sns.set_theme(style="darkgrid")
    fig, axes = plt.subplots(1,2,figsize=(15,7))
 # 1. Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    yticks = [0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]
    ymin, ymax = axes[0].get_ylim()
    #yticks = [tick for tick in yticks if tick >= ymin and tick <= ymax]
    axes[0].set_yticks(yticks)  # Set the positions of the ticks
    axes[0].set_yticklabels([str(tick) for tick in yticks])

# 2. Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])  # Same assumption for 'value'
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    yticks = [0, 20000, 40000, 60000, 80000, 100000, 120000, 140000, 160000, 180000, 200000]
    ymin, ymax = axes[1].get_ylim()  # Get the limits of the y-axis for axes[1]
    #yticks = [tick for tick in yticks if tick >= ymin and tick <= ymax]  # Filter yticks to fit within limits
    axes[1].set_yticks(yticks)  # Set the positions of the ticks for axes[1]
    axes[1].set_yticklabels([str(tick) for tick in yticks])  # Set the labels for the ticks
    #print(yticks)
    #exit()
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png') 
   # plt.show()
    return fig
