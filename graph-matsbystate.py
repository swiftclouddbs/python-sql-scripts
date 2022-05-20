import pandas as pd
import plotly.express as px

df = pd.read_csv('matsbystate.csv')

fig = px.bar(df,
	x = 'State',
	y = 'Mats',
	color='Mats',
	title="Yoga Mats Sold Last Month"
)

fig.update_layout( 
	font_color="black",
	font_size=30
	)


fig.show()

fig.write_image("mats.jpeg")

