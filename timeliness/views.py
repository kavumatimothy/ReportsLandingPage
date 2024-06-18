from django.shortcuts import render
import pandas as pd
from analytics import TableRequest
from config import config
from django.http import HttpResponseServerError
import plotly.graph_objs as go

def timeliness(request):
    try:
        table_request = TableRequest.TableRequest(config)
        df = table_request.get_table()
        df = df.groupby('date')['entered_on_time'].apply(lambda x: (x == 'Yes').mean() * 100).reset_index()
        df.rename(columns={'Response': 'entered_on_time'}, inplace=True)

        # Create a Plotly figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['date'], y=df['entered_on_time'], mode='lines+markers',  name='reports',    line=dict(color='#FF9800'),  # Set line color here
    marker=dict(color='#FF9800', size=5)))

        # Customize layout
        fig.update_layout(
            title='Proportion of Reports Entered on Time',
            xaxis_title='Period',
            yaxis_title='Reports Entered on Time(%)',
            showlegend=True,
            template='plotly_white'  # Choose a Plotly theme (optional)
        )

        # Convert Plotly figure to JSON
        plot_div = fig.to_html(full_html=True)

        context = {
            'plot_div': plot_div
        }
        return render(request, 'timeliness.html', context)
    except Exception as e:
        return HttpResponseServerError(f"An error occurred: {e}")