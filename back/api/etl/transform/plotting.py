import plotly
from plotly import graph_objs


def plot_chart(stock_raw, save_to_dir):
    plotly.tools.set_credentials_file('hustlestar', 'mVugSTzaesWxwrbOwJfY')
    dates = [d.date for d in stock_raw.daily_data]
    trace = graph_objs.Candlestick(
        x=dates,
        open=[d.open_ for d in stock_raw.daily_data],
        high=[d.high_ for d in stock_raw.daily_data],
        low=[d.low_ for d in stock_raw.daily_data],
        close=[d.close_ for d in stock_raw.daily_data],
        yaxis='y2')
    data = [trace]

    data.append(dict(x=dates,
                     y=[d.volume_ for d in stock_raw.daily_data],
                     type='bar',
                     yaxis='y',
                     name='Volume'))
    layout = graph_objs.Layout(
        plot_bgcolor='rgb(250, 250, 250)',
        xaxis=dict(rangeslider=dict(visible=False)),
        yaxis=dict(domain=[0, 0.2], showticklabels=True),
        yaxis2=dict(domain=[0.2, 1]),
        legend=dict(orientation='h', y=0.9, x=0.3, yanchor='bottom'),
        margin=dict(t=40, b=40, r=40, l=40)
    )

    figure = graph_objs.Figure(data=data, layout=layout)

    return plotly.offline.plot(figure, validate=False, output_type='div', auto_open=False, show_link=False)
