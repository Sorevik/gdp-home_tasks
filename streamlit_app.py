import streamlit as st

user_page = st.Page("user_page.py", title="Opgaver", icon=":material/add_circle:")
admin_page = st.Page("admin_page.py", title="Ny opgave", icon=":material/delete:")
dailies_page = st.Page("dailies_page.py", title="Daglige opgaver", icon=":material/delete:")
recurring_page = st.Page("recurring_page.py", title="Hyppige opgaver", icon=":material/delete:")
scoreboard = st.Page("scoreboard.py", title="Scoreboard", icon="🏆")
maintenance = st.Page("maintenance.py", title="Vedligeholdelse", icon = ":material/delete:")


pg = st.navigation([user_page, scoreboard, admin_page, dailies_page, recurring_page, maintenance])
st.set_page_config(page_title="Home tasks", page_icon=":material/edit:")
pg.run()
