import os
import sys
import plotly

import plotly.express as px
import pandas as pd

from datetime import datetime
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication


class PlotlyViewer(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, fig, execute=True):
        # Create a QApplication instance or use the existing one if it exists
        self.app = QApplication.instance() if QApplication.instance() else QApplication(sys.argv)

        super().__init__()

        self.file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "temp.html"))
        plotly.offline.plot(fig, filename=self.file_path, auto_open=False)
        self.load(QUrl.fromLocalFile(self.file_path))
        self.setWindowTitle("Plotly Viewer")
        self.show()

        if execute:
            self.app.exec_()

    def closeEvent(self, event):
        os.remove(self.file_path)


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
    print(fig['data'])
    PlotlyViewer(fig)


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
