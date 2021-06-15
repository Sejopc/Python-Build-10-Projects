import justpy as jp
import pandas
from datetime import datetime
from pytz import utc


data = pandas.read_csv('/Users/jose/Documents/Python Lessons (GitHub)/Python Mega Course - Udemy/Third Application: Data Analysis and Visualization (Part 2: Interactive Charts)/reviews.csv', parse_dates=['Timestamp'])

# Average Rating by Month by Course.
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
month_average_crs = data.groupby(['Month', 'Course Name'])['Rating'].mean().unstack() 
# NOTE: What causes that the Course Names became the Column names for the Dataframe, is the "unstack()" method above.
#       Please see the "Average Ratings By Course by Month" Jupyter Notebook for understanding.
#print(month_average_crs)
#print(month_average_crs.index)


# We will be using Areaspline chart: https://www.highcharts.com/docs/chart-and-series-types/areaspline-chart 
chart_def = """ 
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average Rating by Course per Month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false, //changed from true, to false.
        borderWidth: 1,
        backgroundColor:
            // Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF' // Python cannot recognize this line. Just leave #FFFFFF
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.0 //changed from 0.5 to 0.0
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def app():

    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md") # H1 Element
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-body1") # p Element

    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.xAxis.categories = list(month_average_crs.index)

    hc_data = [ {"name": course, "data": [rating for rating in month_average_crs[course]]} for course in month_average_crs.columns ]

    hc.options.series = hc_data

    return wp

jp.justpy(app)