import justpy as jp
import pandas
from datetime import datetime
from pytz import utc

data = pandas.read_csv('/Users/jose/Documents/Python Lessons (GitHub)/Python Mega Course - Udemy/Third Application: Data Analysis and Visualization (Part 2: Interactive Charts)/reviews.csv', parse_dates=['Timestamp'])
share = data.groupby(['Course Name'])['Rating'].count()

chart_def = """ 
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""



def app():
    wp = jp.QuasarPage() # We are creating a Quasar page object instance. Will return that instance.
    h1 = jp.QDiv(a=wp, text="Analysis of the happiest day of the week", classes="text-h3 text-center q-pa-md") # H1 Element
    p1 = jp.QDiv(a=wp, text="These graphs represent which day people are the happiest", classes="text-body1") # p Element

    hc = jp.HighCharts(a=wp, options=chart_def)
    hc_data = [{"name":course, "y":ratings} for course,ratings in zip(share.index, share)]
    hc.options.series[0].data = hc_data

    return wp

jp.justpy(app)