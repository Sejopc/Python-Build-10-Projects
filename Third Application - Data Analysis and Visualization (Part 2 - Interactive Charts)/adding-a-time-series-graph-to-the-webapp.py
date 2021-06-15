import justpy as jp
import pandas
from datetime import datetime
from pytz import utc


data = pandas.read_csv('/Users/jose/Documents/Python Lessons (GitHub)/Python Mega Course - Udemy/Third Application: Data Analysis and Visualization (Part 2: Interactive Charts)/reviews.csv', parse_dates=['Timestamp'])
# Average Rating by Week
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()

chart_def = """ 
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Week'
    },
    subtitle: {
        text: 'According to the Python Courses'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} - {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Ratings',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""


def app():
    wp = jp.QuasarPage() # We are creating a Quasar page object instance. Will return that instance.
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md") # H1 Element
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-body1") # p Element

    hc = jp.HighCharts(a=wp, options=chart_def) # We will create our HighChart here. 

    hc.options.xAxis.categories = list(week_average.index)
    hc.options.series[0].data = list(week_average['Rating'])

    return wp

jp.justpy(app)