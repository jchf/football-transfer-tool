import bokeh
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable, TableColumn
from bokeh.layouts import grid


def print_table(player_stats_df):
    source = ColumnDataSource(player_stats_df)
    columns = [TableColumn(field=column, title=column) for column in list(player_stats_df.columns)]
    data_table = DataTable(source=source,  columns=columns, index_position=None, height=150, width=850,
                           sizing_mode="stretch_width")

    return data_table


def print_tab(df, titre):
    grid_ = grid(
        children=[print_table(df)],
        sizing_mode="stretch_width",
    )

    return bokeh.models.Panel(child=grid_, title=titre)

