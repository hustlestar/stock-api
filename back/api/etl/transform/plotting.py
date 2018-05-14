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

    layout = dict()
    fig = dict(data=data, layout=layout)
    fig['layout'] = dict()
    fig['layout']['plot_bgcolor'] = 'rgb(250, 250, 250)'
    fig['layout']['xaxis'] = dict(rangeselector=dict(visible=True))
    fig['layout']['yaxis'] = dict(domain=[0, 0.2], showticklabels=False)
    fig['layout']['yaxis2'] = dict(domain=[0.2, 0.8])
    fig['layout']['legend'] = dict(orientation='h', y=0.9, x=0.3, yanchor='bottom')
    fig['layout']['margin'] = dict(t=40, b=40, r=40, l=40)

    fig['data'].append(dict(x=dates, y=[d.volume_ for d in stock_raw.daily_data],
                            type='bar', yaxis='y', name='Volume'))
    #plotly.offline.plot(fig, filename=save_to_dir + stock_raw.ticker + '.html', validate = False)
    return plotly.offline.plot(fig, validate = False, output_type='div', auto_open=False)
    # plotly.plotly.plot(data, filename='simple_candlestick')
