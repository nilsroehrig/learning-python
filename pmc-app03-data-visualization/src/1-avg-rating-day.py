import justpy as jp
import pandas

data = pandas.read_csv("../materials/reviews.csv", parse_dates=["Timestamp"])
data["Day"] = data["Timestamp"].dt.date
day_avg = data.groupby(["Day"]).mean()

chart_definition = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Ratings by Day'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Date'
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
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}: {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    }
}
"""


def app():
    page = jp.QuasarPage()
    headline = jp.H1(a=page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    paragraph = jp.QDiv(a=page, text="These graphs represent course review analysis")
    chart = jp.HighCharts(a=page, options=chart_definition)
    chart.options.xAxis.categories = list(day_avg.index)
    chart.options.series = [{
        "name": "Average Rating",
        "data": list(day_avg["Rating"])
    }]

    return page


jp.justpy(app)
