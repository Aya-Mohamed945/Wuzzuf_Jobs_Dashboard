import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def top5_jobs(df):
    """Bar chart of top 5 jobs"""
    job_counts = df.groupby('job_title').size().reset_index(name='count')
    job_counts = job_counts.sort_values(by='count', ascending=False)
    top5_jobs = job_counts.head(5)

    fig = px.bar(
        top5_jobs,
        x='job_title',
        y='count',
        title="Top 5 Jobs On Wuzzuf",
        color='count',
        color_continuous_scale='Blues'
    )
    fig.update_layout(
        xaxis_title="Job Title",
        yaxis_title="Number of Jobs",
        showlegend=False
    )
    return fig

def work_mode_pie(df):
    """Pie chart of work modes distribution"""
    freq_work_mode = df.groupby("work_modes").size().reset_index(name='count')
    freq_work_mode = freq_work_mode.dropna()

    fig = px.pie(
        freq_work_mode,
        names='work_modes',
        values='count',
        title="Distribution of Work Modes",
        color_discrete_sequence=px.colors.sequential.Blues_r,
        hole=0.3
    )
    fig.update_traces(textposition='inside', textinfo='percent+label')
    return fig

def employment_types_chart(df):
    """Bar chart of employment types"""
    emp_types = df.groupby('employment_types').size().reset_index(name='count')
    emp_types = emp_types.sort_values('count', ascending=False)

    fig = px.bar(
        emp_types,
        x='employment_types',
        y='count',
        title="Employment Types Distribution",
        color='count',
        color_continuous_scale='Blues'
    )
    return fig

def jobs_per_country_line(df):
    """Line chart of jobs per country"""
    jobs_by_country = df.groupby('country').size().reset_index(name='count')
    jobs_by_country = jobs_by_country.sort_values('count', ascending=False)

    fig = px.line(
        jobs_by_country,
        x='country',
        y='count',
        markers=True,
        title='Number of Jobs per Country',
        line_shape='linear'
    )
    fig.update_traces(line_color='#1f77b4', marker=dict(size=8))
    fig.update_layout(
        xaxis_title="Country",
        yaxis_title="Number of Jobs",
        xaxis={'tickangle': 45}
    )
    return fig

def jobs_per_city(df):
    """Horizontal bar chart of jobs per Egyptian city"""
    egypt_cities_jobs = df[df['country'] == 'Egypt']
    job_by_city = egypt_cities_jobs.groupby('city').size().reset_index(name='count')
    job_by_city = job_by_city.sort_values('count', ascending=True)

    fig = px.bar(
        job_by_city,
        x='count',
        y='city',
        orientation='h',
        title="Jobs per City in Egypt",
        color='count',
        color_continuous_scale='Blues'
    )
    fig.update_layout(
        xaxis_title="Number of Jobs",
        yaxis_title="City",
        height=500
    )
    return fig

def choropleth_map(df):
    """World map of job distribution with log scale"""
    country_counts = df.groupby('country').size().reset_index(name='count')
    country_counts['log_count'] = np.log1p(country_counts['count'])

    fig = px.choropleth(
        country_counts,
        locations='country',
        locationmode='country names',
        color='log_count',
        color_continuous_scale='Blues',
        title='Number of Jobs per Country (Log Scale)',
        labels={'log_count': 'Log(Jobs+1)', 'country': 'Country'}
    )

    # Add country labels
    for _, row in country_counts.iterrows():
        fig.add_trace(
            go.Scattergeo(
                locations=[row['country']],
                locationmode='country names',
                text=[f"{row['country']}: {row['count']}"],
                mode='text',
                showlegend=False,
                textfont=dict(size=9, color='black')
            )
        )

    fig.update_layout(height=600)
    return fig

def remote_jobs_city(df):
    """Bar chart of remote jobs by city"""
    remote_jobs = df[df['work_modes'] == 'Remote']
    
    if remote_jobs.empty:
        # Create empty figure with message
        fig = go.Figure()
        fig.add_annotation(
            text="No remote jobs found in the dataset",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False
        )
        return fig
    
    remote_by_city = remote_jobs.groupby('city').size().reset_index(name='#remote jobs')
    remote_by_city = remote_by_city.sort_values('#remote jobs', ascending=False)

    fig = px.bar(
        remote_by_city,
        x='city',
        y='#remote jobs',
        title="Remote Jobs by City",
        color='#remote jobs',
        color_continuous_scale='Blues'
    )
    fig.update_layout(
        xaxis_title="City",
        yaxis_title="Number of Remote Jobs",
        xaxis={'tickangle': 45}
    )
    return fig

def skills_wordcloud(df):
    """Generate word cloud data from skills (simplified version)"""
    all_skills = df['skills'].dropna().str.cat(sep=' ')
    skill_list = all_skills.replace(',', ' ').replace('·', ' ').split()
    skill_freq = pd.Series(skill_list).value_counts().head(20).reset_index()
    skill_freq.columns = ['skill', 'count']
    
    fig = px.bar(
        skill_freq,
        x='count',
        y='skill',
        orientation='h',
        title="Top 20 Skills Mentioned",
        color='count',
        color_continuous_scale='Blues'
    )
    return fig