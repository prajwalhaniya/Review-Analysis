from ssl import Options
from typing import Text

import justpy as jp
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc
data=pd.read_csv('reviews.csv',parse_dates=['Timestamp'])

#calculation of the average rating per Month
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
data_month_course = data.groupby(['Month','Course Name'])['Rating'].mean().unstack()


from pandas.core.dtypes.common import classes

#template of code from HighChart for better presentation of graph
chart_def="""
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
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
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' Rating'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
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
    # Creating a web page
    wp = jp.QuasarPage() 

    # heading
    h1 = jp.QDiv(a=wp, text='Analysis of Course Reviews',classes="text-h3 text-center text-weight-bold")
    
    # Displaying the chart
    hc = jp.HighCharts(a=wp,options=chart_def)

    #title of the chart
    hc.options.title.text = "Average Rating by Course by Month"
    hc.options.subtitle.text = "According the provided dataset"

    #taking the dataset from the given dataframe
    hc.options.xAxis.categories = list(data_month_course.index)

    hc_data = [{"name":v1,"data":[v2 for v2 in data_month_course[v1]]} for v1 in data_month_course.columns]

    hc.options.series = hc_data


    return wp

jp.justpy(app)


