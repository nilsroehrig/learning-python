import justpy as jp
import pandas

data = pandas.read_csv("../materials/reviews.csv", parse_dates=["Timestamp"])

data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
month_avg_course = data.groupby(["Month", "Course Name"])["Rating"].count().unstack()

chart_options = """
{

    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    title: {
        floating: true,
        align: 'left',
        text: 'Count of Ratings per Course by Month'
    },

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            },
            accessibility: {
                exposeAsGroupOnly: true
            }
        }
    },

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}
"""


def app():
    page = jp.QuasarPage()
    headline = jp.H1(a=page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    paragraph = jp.QDiv(a=page, text="These graphs represent course review analysis")

    chart = jp.HighCharts(a=page, options=chart_options)
    chart.options.xAxis.categories = list(month_avg_course.index)

    series = []

    for col in list(month_avg_course.columns):
        series.append({
            "name": col,
            "data": list(month_avg_course[col])
        })

    chart.options.series = series

    return page


jp.justpy(app)
