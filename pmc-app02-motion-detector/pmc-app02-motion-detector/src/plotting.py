from bokeh.models import HoverTool, ColumnDataSource
from bokeh.plotting import figure, show, output_file

from motion_detector import timespan_dataframe

timespan_dataframe["start_string"] = timespan_dataframe["start"].dt.strftime("%Y-%m-%d %H:%M:%S")
timespan_dataframe["end_string"] = timespan_dataframe["end"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(timespan_dataframe)

plot = figure(x_axis_type="datetime", height=100, width=500, title="Motion Graph", sizing_mode="scale_width")
plot.yaxis.minor_tick_line_color = None
plot.yaxis.ticker.desired_num_ticks = 1

hover = HoverTool(tooltips=[("Start", "@start_string"), ("End", "@end_string")])
plot.add_tools(hover)

quad = plot.quad(left="start", right="end", bottom=0, top=1, color="green", source=cds)

output_file("../output/graph.html")
show(plot)
