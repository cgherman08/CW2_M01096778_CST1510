import altair as alt
import pandas as pd
import streamlit as st
from services.database_manager import DatabaseManager

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'username' not in st.session_state:
    st.session_state['username'] = ''

st.title('Cyber Incidents Dashboard')

if not st.session_state['logged_in']:
    st.switch_page('pages/1_🔐 _Login.py')


data = DatabaseManager().get_all_cyber_incidents()

with st.sidebar:
    st.header('Filters')
    severity_options = sorted(data['severity'].dropna().unique())
    status_options = sorted(data['status'].dropna().unique())
    severity_selected = st.multiselect('Severity', severity_options, default=severity_options)
    status_selected = st.multiselect('Status', status_options, default=status_options)

    data['timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')
    min_date = data['timestamp'].min().date() if not data.empty else None
    max_date = data['timestamp'].max().date() if not data.empty else None
    date_range = st.date_input('Date range', (min_date, max_date)) if min_date and max_date else None

mask = (
    data['severity'].isin(severity_selected)
    & data['status'].isin(status_selected)
)

if date_range and len(date_range) == 2:
    start_date, end_date = pd.to_datetime(date_range[0]), pd.to_datetime(date_range[1])
    mask = mask & (data['timestamp'].dt.date >= start_date.date()) & (data['timestamp'].dt.date <= end_date.date())

filtered = data.loc[mask].copy()

st.caption(f"Showing {len(filtered):,} incidents (of {len(data):,})")

# Summary charts
status_counts = filtered['status'].value_counts().reset_index()
status_counts.columns = ['status', 'count']

severity_counts = filtered['severity'].value_counts().reset_index()
severity_counts.columns = ['severity', 'count']

category_counts = filtered['category'].value_counts().reset_index()
category_counts.columns = ['category', 'count']

timeline = (
    filtered.dropna(subset=['timestamp'])
    .groupby(pd.Grouper(key='timestamp', freq='D'))
    .size()
    .reset_index(name='incidents')
)

col1, col2 = st.columns(2)

with col1:
    st.markdown('**Incidents by status**')
    chart_status = (
        alt.Chart(status_counts)
        .mark_bar(color='#4b8bf4')
        .encode(
            x=alt.X('count:Q', title='Count'),
            y=alt.Y('status:N', sort='-x', title='Status'),
            text='count:Q'
        )
        .mark_bar()
    )
    st.altair_chart(chart_status, width='stretch')

with col2:
    st.markdown('**Incidents by severity**')
    chart_severity = (
        alt.Chart(severity_counts)
        .mark_bar(color='#f97316')
        .encode(
            x=alt.X('count:Q', title='Count'),
            y=alt.Y('severity:N', sort='-x', title='Severity'),
            text='count:Q'
        )
    )
    st.altair_chart(chart_severity, width='stretch')

st.markdown('**Incidents by category**')
chart_category = (
    alt.Chart(category_counts)
    .mark_bar(color='#10b981')
    .encode(
        x=alt.X('category:N', sort='-y', title='Category'),
        y=alt.Y('count:Q', title='Count'),
        tooltip=['category', 'count']
    )
)
st.altair_chart(chart_category, width='stretch')

st.markdown('**Timeline**')
chart_timeline = (
    alt.Chart(timeline)
    .mark_line(point=True, color='#6366f1')
    .encode(
        x=alt.X('timestamp:T', title='Date'),
        y=alt.Y('incidents:Q', title='Incidents per day'),
        tooltip=['timestamp:T', 'incidents:Q']
    )
)
st.altair_chart(chart_timeline, width='stretch')

st.subheader('Filtered incidents')
st.dataframe(
    filtered.sort_values(by='timestamp'),
    width='stretch',
)
 
 
 