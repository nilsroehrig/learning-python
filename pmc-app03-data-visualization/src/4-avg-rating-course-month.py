import justpy as jp
import pandas

data = pandas.read_csv("../materials/reviews.csv", parse_dates=["Timestamp"])

data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
month_avg_course = data.groupby(["Month", "Course Name"])["Rating"].mean().unstack()

chart_def = """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average Rating per Course by Month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 120,
        y: 70,
        floating: true,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        }
    },
    tooltip: {
        shared: true,
        headerFormat: '{point.x}: {point.y}'
    },
    credits: {
        enabled: true
    }
}"""


def app():
    page = jp.QuasarPage()
    headline = jp.H1(a=page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    paragraph = jp.QDiv(a=page, text="These graphs represent course review analysis")

    chart = jp.HighCharts(a=page, options=chart_def)
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
