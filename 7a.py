from bokeh.plotting import figure, show
from bokeh.models import Label

# 1. Setup Data & Figure
p = figure(title="Line Graph", x_axis_label='X', y_axis_label='Y')

# 2. Draw Line
p.line([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], legend_label="y=2x", line_width=2)

# 3. Add Simplified Annotation
p.add_layout(Label(x=3, y=6, text="Point", text_color="red"))

# 4. Settings & Show
p.legend.click_policy = "hide"
show(p)
