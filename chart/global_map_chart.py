import plotly.express as px

from data.global_map_data import get_chart_data

df = get_chart_data()
def map_plot():
    fig = px.scatter_mapbox(df, lat="lat", lon="lon",
                            color="Radiation Level (mGy/h)",
                            size="Radiation Level (mGy/h)",
                            color_continuous_scale=["blue", "yellow", "red"],
                            range_color=(0, 10),
                            size_max=15,
                            zoom=10,
                            hover_name='Local',
                            hover_data=['User'],
                            mapbox_style='open-street-map'
                            )
    #
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(
        hoverlabel=dict(
            font_size=16
        )
    )
    # fig.show()
    return fig

# styles objects are: open - street - map, white - bg, carto - positron, carto - darkmatter, stamen - terrain, stamen - toner, stamen - watercolor
# The built - in Mapbox styles are: basic, streets, outdoors, light, dark, satellite, satellite - streets

# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
