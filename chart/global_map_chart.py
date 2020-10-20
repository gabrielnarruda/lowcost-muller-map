import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

from data.global_map_data import df
from globals.styles import colors

import plotly.express as px

fig = px.scatter_mapbox(df, lat="lat", lon="lon",
                       color="Indice Radiação (mR/h)",
                       size="Indice Radiação (mR/h)",
                       color_continuous_scale='bluered',
                       size_max=15,
                       zoom=10,
                       hover_name='Local'
                 )

fig.update_layout(mapbox_style="carto-positron",)

# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

