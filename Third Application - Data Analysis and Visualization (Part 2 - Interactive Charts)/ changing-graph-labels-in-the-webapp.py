import justpy as jp


chart_def = """ 
{
    chart: {
        type: 'spline',
        inverted: false // Revert X,Y axis, so series.data variable below has their values inverted.
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
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
            text: 'Average Rating'
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

# A Quasar page is like the Main (index.html) page for Justpy Web Framework.

def app():
    wp = jp.QuasarPage() # We are creating a Quasar page object instance. Will return that instance.
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md") # H1 Element
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-body1") # p Element
    # We will add HighChart (another JustPy componenent) Graph. For choosing which graph we need, go to:
    # https://www.highcharts.com/docs/index > Charts and Series Types - HighCharts is a JavaScript Library 
    # to produce Graphs. 
    # Same as Quasar, which is another JavaScript Library, whoever it is unrelated to HighCharts.
    # Python is getting these 2 JavaScript Frameworks together. 

    # In our case, we will use Spline Chart: https://www.highcharts.com/docs/chart-and-series-types/spline-chart 
    # For this, we need the JavaScript code, so we open the chart in jsFiddle (upper-right corner of the graph),
    # and copy JS code after "   Highcharts.chart('container',   "   All the WAY to the last curly bracket (}) - and
    # we will paste it in our variable chart_def from above ^^^.

    hc = jp.HighCharts(a=wp, options=chart_def) # We will create our HighChart here.

    # Above 2 prints will only print (on VS Code Terminal, or whethever you run the script from) after we access the page.
    ###print(hc.options.) # same as the JS (actually JSON) code above on the chart_def variable. Python converts it into a Dictionary
    ###print(type(hc.options))

    # NOTE: We can ACCESS and MODIFY all the Dictionary attributes from above (i.e Title, Subtitle, etc) using
    # hc.options.<attribute>

    ###print(hc.options.title.text)
    hc.options.title.text = "Average Rating by Day"
    ###hc.options.series[0].data = [[3,4], [6,7], [8,9]] # [X,Y] axis values. However this is cumbersome and not the 
                                                      # proper way to add data. We add data this way:
   # x = [3, 6, 8]
   # y = [4, 7, 9]
    ###hc.options.series[0].data = list(zip(x, y)) # Will produce: [(3,4), (6,7), (8,9)]

    # NOW what really matter. Injecting data from a Dataframe to produce useful Graphs.

    import pandas
    from datetime import datetime
    from pytz import utc
    import matplotlib.pyplot as plt

    data = pandas.read_csv('/Users/jose/Documents/Python Lessons (GitHub)/Python Mega Course - Udemy/Third Application: Data Analysis and Visualization (Part 2: Interactive Charts)/reviews.csv', parse_dates=['Timestamp'])

    # Average Rating by Day
    data['Day'] = data['Timestamp'].dt.date
    day_average = data.groupby(['Day']).mean()

    ###hc.options.series[0].data = list(zip(day_average.index, day_average['Rating']))
    # NOTE: However, this also won't fill out the graph because HighCharts considers the dates (day_average.index) as
    # categories types of data, not numbers. To solve this, we need to provide this data in this way:

    hc.options.xAxis.categories = list(day_average.index) # We are creating "categories" key inside "xAxis" dictionary.
    hc.options.series[0].data = list(day_average['Rating'])

    return wp

jp.justpy(app)