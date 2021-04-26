import io

import plotly.express as px
import plotly.io as pio

from datetime import datetime
from PIL import Image


def show(fig):
    buf = io.BytesIO()
    pio.write_image(fig, buf)
    img = Image.open(buf)
    img.show()


def plot_schedule(dataframe):
    df_converted = dataframe.copy()
    df_converted['Start'] = df_converted['Start'].apply(convert_to_datetime)
    df_converted['Finish'] = df_converted['Finish'].apply(convert_to_datetime)

    hovers = []
    for i in range(len(df_converted)):
        hovers.append(f"Process: {dataframe['Task'].loc[i]}<br>Start: {dataframe['Start'].loc[i]}"
                      f"<br>Finish: {dataframe['Finish'].loc[i]}")

    df_converted['hover'] = hovers

    num_tick_labels = sorted(list(dataframe['Start']) + list(dataframe['Finish']))

    date_ticks = [convert_to_datetime(x) for x in num_tick_labels]

    fig = px.timeline(df_converted, x_start="Start", x_end="Finish", y="Task", hover_name='hover',
                      hover_data={'Task': False, 'Start': False, 'Finish': False})
    fig.layout.xaxis.update({
        'tickvals': date_ticks,
        'ticktext': num_tick_labels
    })
    fig.update_yaxes(autorange="reversed")
    show(fig)


def convert_to_datetime(x):
    return datetime.fromtimestamp(31536000 + x * 24 * 3600).strftime("%Y-%m-%d")


# df = pd.DataFrame([
#     dict(Task="Job A", Start=0, Finish=5),
#     dict(Task="Job B", Start=5, Finish=10),
#     dict(Task="Job C", Start=10, Finish=12),
#     dict(Task="Job D", Start=12, Finish=15),
#     dict(Task="Job C", Start=15, Finish=17.5),
#     dict(Task="Job C", Start=20, Finish=25.5)
# ])
# plot_schedule(df)
