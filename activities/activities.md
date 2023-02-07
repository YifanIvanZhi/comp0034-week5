# Optional activities

These are entirely optional but may be useful if you have a design that makes use of them.

1. Plotly Go
2. [For Multipage Dash apps please refer to the Dash documentation directly](https://dash.plotly.com/urls)

## Plotly Go

### Overview of `plotly.graph_objects`

You may need to change features of a visualisation that are not exposed in Express, in which case you would need to use Plotly.py graph objects instead. The following is a brief overview of using graph objects.

There are 3 main concepts in Plotly’s philosophy:

1. Data
2. Layout
3. Figure

### Data

The Data object defines what we want to display in the chart (that is, the data). We define a collection of data and the specifications to display them as a trace. A Data object can have many traces. Think of a line chart with two lines representing two different categories: each line is a trace.

### Layout

The Layout object defines features that are not related to data (like title, axis titles, and so on). We can also use the Layout to add annotations and shapes to the chart.

### Figure

The Figure object creates the final object to be plotted. It's an object that contains both data and layout.

### Example chart

In the following code you can see how the layout is updated

```python
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv')

fig = go.Figure()

fig.add_trace(go.Sunburst(
    ids=df.ids,
    labels=df.labels,
    parents=df.parents,
    domain=dict(column=1),
    maxdepth=2,
    insidetextorientation='radial'
))

fig.update_layout(
    margin=dict(t=10, l=10, r=10, b=10)
)

fig.show()
```

The code in [/src/sunburst.py](/src/sunburst.py) creates the above plot using code
from [Plotly.](https://plotly.com/python/sunburst-charts/#controlling-text-orientation-inside-sunburst-sectors)

There are [Go activities in week 2](https://github.com/nicholsons/comp0034-week2/blob/main/activities/lollapalooza.md#adding-plotly-go-charts-to-the-lollapalooza-dashboard) that can be added to the Lollapalooza dashboard.

### Further information

- [Plotly Graph Objects documentation](https://plotly.com/python/graph-objects/).

- [Examples](https://plotly.com/python/) for creating many different chart types in Plotly Express and Plotly Go.

- [Article with examples of lots of charts and different styling techniques](https://towardsdatascience.com/visualization-with-plotly-express-comprehensive-guide-eb5ee4b50b57) and the [code in GitHub](https://github.com/vaclavdekanovsky/data-analysis-in-examples/blob/master/Vizualizations/Plotly/Comperhansive%20Guide/Plotly%20Express%20-%20Comprehensive%20Guide.ipynb)
