import plotly.express as px

from data.global_map_data import get_chart_data

df=get_chart_data()

fig = px.scatter_mapbox(df, lat="lat", lon="lon",
                       color="Radiation Level (mR/h)",
                       size="Radiation Level (mR/h)",
                       color_continuous_scale=["blue", "yellow", "red"],
                       size_max=15,
                       zoom=10,
                       hover_name='Local'
                 )

fig.update_layout(mapbox_style="carto-positron",)

# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

