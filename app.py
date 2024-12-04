import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px


data_file = "formatted_sales_data.csv"
df = pd.read_csv(data_file)


df["date"] = pd.to_datetime(df["date"])


df = df.sort_values(by="date")


app = Dash(__name__)


fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Sales Trends of Pink Morsels by Date",
    labels={"date": "Date", "sales": "Total Sales ($)"}
)


app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(figure=fig),
    html.P(
        "Note: Observe the sales trends before and after the price increase on January 15, 2021.",
        style={"textAlign": "center", "marginTop": "20px"}
    )
])


if __name__ == "__main__":
    app.run_server(debug=True)
