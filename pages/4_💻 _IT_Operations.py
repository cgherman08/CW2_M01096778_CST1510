import altair as alt
import pandas as pd
import streamlit as st
from services.database_manager import DatabaseManager

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'username' not in st.session_state:
    st.session_state['username'] = ''

st.title('IT Operations Dashboard')

if not st.session_state['logged_in']:
    st.switch_page('pages/1_🔐 _Login.py')

tickets = DatabaseManager().load_tickets()

with st.sidebar:
    st.header('Filters')
    priority_options = sorted(tickets['priority'].dropna().unique())
    status_options = sorted(tickets['status'].dropna().unique())
    assigned_options = sorted(tickets['assigned_to'].dropna().unique())
    priority_selected = st.multiselect('Priority', priority_options, default=priority_options)
    status_selected = st.multiselect('Status', status_options, default=status_options)
    assigned_selected = st.multiselect('Assigned to', assigned_options, default=assigned_options)

filtered = tickets[
    tickets['priority'].isin(priority_selected)
    & tickets['status'].isin(status_selected)
    & tickets['assigned_to'].isin(assigned_selected)
].copy()

st.caption(f"Showing {len(filtered):,} tickets (of {len(tickets):,})")

# Summary counts
priority_counts = filtered['priority'].value_counts().reset_index()
priority_counts.columns = ['priority', 'count']

status_counts = filtered['status'].value_counts().reset_index()
status_counts.columns = ['status', 'count']

assignee_counts = filtered['assigned_to'].value_counts().reset_index()
assignee_counts.columns = ['assigned_to', 'count']

timeline = (
    filtered.dropna(subset=['created_at'])
    .groupby(pd.Grouper(key='created_at', freq='W'))
    .size()
    .reset_index(name='tickets')
)

col1, col2 = st.columns(2)

with col1:
    st.markdown('**Tickets by priority**')
    chart_priority = (
        alt.Chart(priority_counts)
        .mark_bar(color='#f59e0b')
        .encode(
            x=alt.X('count:Q', title='Count'),
            y=alt.Y('priority:N', sort='-x', title='Priority'),
            tooltip=['priority', 'count']
        )
    )
    st.altair_chart(chart_priority, width='stretch')

with col2:
    st.markdown('**Tickets by status**')
    chart_status = (
        alt.Chart(status_counts)
        .mark_bar(color='#3b82f6')
        .encode(
            x=alt.X('count:Q', title='Count'),
            y=alt.Y('status:N', sort='-x', title='Status'),
            tooltip=['status', 'count']
        )
    )
    st.altair_chart(chart_status, width='stretch')

st.markdown('**Tickets by assignee**')
chart_assignee = (
    alt.Chart(assignee_counts)
    .mark_bar(color='#10b981')
    .encode(
        x=alt.X('assigned_to:N', sort='-y', title='Assignee'),
        y=alt.Y('count:Q', title='Count'),
        tooltip=['assigned_to', 'count']
    )
)
st.altair_chart(chart_assignee, width='stretch')

st.markdown('**Weekly ticket volume**')
chart_timeline = (
    alt.Chart(timeline)
    .mark_line(point=True, color='#6366f1')
    .encode(
        x=alt.X('created_at:T', title='Week'),
        y=alt.Y('tickets:Q', title='Tickets per week'),
        tooltip=['created_at:T', 'tickets:Q']
    )
)
st.altair_chart(chart_timeline, width='stretch')
