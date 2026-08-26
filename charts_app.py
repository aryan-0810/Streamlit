import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Streamlit Charts and Data Visualization")

st.header("1. Daily Step Count")

steps_data = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Steps": [6500, 7200, 8100, 7000, 9500, 11000, 8800]
})

st.line_chart(steps_data.set_index("Day"))


st.header("2. Monthly Food Orders")

orders_data = pd.DataFrame({
    "Platform": ["Zomato", "Swiggy", "Domino's"],
    "Orders": [35, 42, 28]
})

st.bar_chart(orders_data.set_index("Platform"))


st.header("3. Spotify Listening Time")

spotify_data = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Listening Time": [45, 60, 35, 70, 90, 120, 80]
})

st.area_chart(spotify_data.set_index("Day"))


st.header("4. Daily Social Media Usage")

social_media_data = pd.DataFrame({
    "Platform": ["Instagram", "YouTube", "WhatsApp"],
    "Minutes": [120, 90, 60]
})

fig = px.pie(
    social_media_data,
    names="Platform",
    values="Minutes",
    title="Daily Social Media Usage"
)

st.plotly_chart(fig)


st.header("5. WhatsApp Chat Activity")

whatsapp_data = pd.DataFrame({
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Messages Sent": [120, 150, 100, 180, 220, 250, 190],
    "Photos Shared": [10, 15, 8, 20, 25, 30, 18],
    "Calls Made": [5, 8, 4, 10, 12, 15, 9]
})

selected_columns = st.multiselect(
    "Select activities to visualize",
    ["Messages Sent", "Photos Shared", "Calls Made"],
    default=["Messages Sent"]
)

if selected_columns:
    chart_data = whatsapp_data.set_index("Day")[selected_columns]
    st.line_chart(chart_data)
else:
    st.write("Please select at least one activity.")