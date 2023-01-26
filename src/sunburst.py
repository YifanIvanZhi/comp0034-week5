import plotly.graph_objects as go
import pandas as pd


def sunburst():
    """Creates a sunburst chart using Plotly Go"""
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/718417069ead87650b90472464c7565dc8c2cb1c/coffee-flavors.csv"
    )

    # Create a figure
    fig = go.Figure()

    # Add a trace to the figure
    fig.add_trace(
        go.Sunburst(
            ids=df.ids,
            labels=df.labels,
            parents=df.parents,
            domain=dict(column=1),
            maxdepth=2,
            insidetextorientation="radial",
        )
    )


if __name__ == "__main__":
    sunburst()
