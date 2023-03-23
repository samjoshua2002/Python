from pyexpat.errors import XML_ERROR_SYNTAX
import pandas as pd
import bar_chart_race as bcr
df=pd.read_excel("Salesdata.xlsx")
df.set_index("Date",inplace=True)
# Documentation: https://pypi.org/project/bar-chart-race/
bcr.bar_chart_race(
    df=df,
    filename='Salesdata.mp4',
    orientation='h',
    sort='desc',
    n_bars=6,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=10,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%B %d, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total Sales: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    period_length=500,
    figsize=(12, 6),
    dpi=300,
    cmap='dark12',
    title='Sales by stores in USD',
    bar_label_size=7,
    tick_label_size=7,
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False) 