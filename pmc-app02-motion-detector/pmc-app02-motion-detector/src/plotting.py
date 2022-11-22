from bokeh.plotting import figure, show, output_file

from motion_detector import timespan_dataframe

plot = figure(x_axis_type="datetime", height=100, width=500, title="Motion Graph", sizing_mode="scale_width")
plot.yaxis.minor_tick_line_color = None
plot.yaxis.ticker.desired_num_ticks = 1
quad = plot.quad(left=timespan_dataframe["start"], right=timespan_dataframe["end"], bottom=0, top=1, color="green")

output_file("graph.html")
show(plot)
