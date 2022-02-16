# %%

START_INTEGER = 1
# START_INTEGER = 6
# START_INTEGER = 9
# START_INTEGER = 16

# START_INTEGER = 27 # 31
# START_INTEGER = 100
# START_INTEGER = 100 # 1000 | 10000 | 100000

import sys
from time import sleep

from bokeh.io import push_notebook, show, output_notebook
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure

output_notebook()

def collatz_while(num):
    sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1

        sequence.append(num)

    return sequence

def collatz_graph(start):
    sequence = collatz_while(start)
    length = len(sequence)

    # Create a Python dict as the basis of your ColumnDataSource
    data = {'x_values': range(0, length),
            'y_values': sequence}
    source = ColumnDataSource(data=data)

    # Create a plot using the ColumnDataSource's two columns
    fig = figure(title="Collatz Conjecture")
    fig.circle(
        source=source,
        x='x_values',
        y='y_values', 
        fill_alpha=0.2,
        size=20,
    )
    fig.line(
        source=source,
        x='x_values',
        y='y_values', 
        line_width=2
    )
    tooltips = [
        ("Step", "@x_values"),
        ("Value", "@y_values"),
    ]
    fig.add_tools(HoverTool(tooltips=tooltips))

    print(f'Sequence: {sequence}')
    print(f'Length/Steps: {length}')

    show(fig)

collatz_graph(START_INTEGER)


# %%
