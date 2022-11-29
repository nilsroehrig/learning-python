import justpy as jp

import pandas

data = pandas.read_csv("../materials/reviews.csv", parse_dates=["Timestamp"])
share = data.groupby(["Course Name"])["Rating"].count()

chart_options = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Share of Ratings by Course'
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
        name: 'Courses',
        colorByPoint: true,
    }]
}
"""


def app():
    page = jp.QuasarPage()
    headline = jp.H1(a=page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    paragraph = jp.P(a=page, text="These graphs represent course review analysis")

    chart = jp.HighCharts(a=page, options=chart_options)

    chart.options.series[0].data = [{"name": name, "y": y} for name, y in zip(share.index, share)]

    return page


jp.justpy(app)
