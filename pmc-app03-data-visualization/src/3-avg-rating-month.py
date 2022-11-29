import justpy as jp
import pandas

data = pandas.read_csv("../materials/reviews.csv", parse_dates=["Timestamp"])
data["Week"] = data["Timestamp"].dt.strftime('%Y-%m')
month_avg = data.groupby(["Week"]).mean()

chart_definition = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Ratings by Month'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
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
    chart.options.xAxis.categories = list(month_avg.index)
    chart.options.series = [{
        "name": "Average Rating",
        "data": list(month_avg["Rating"])
    }]

    return page


jp.justpy(app)
