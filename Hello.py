import streamlit as st
import datetime
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# :balloon: Welcome to Streamlit! 👋")
    start = st.sidebar.selectbox(
    'Starting Point',
    ('Email', 'Home phone', 'Mobile phone'))
    destinations = st.sidebar.multiselect(
    'Destination',
    ['Green', 'Yellow', 'Red', 'Blue'])
    today = datetime.datetime.now()
    next_year = today.year + 1
    jan_1 = datetime.date(next_year, 1, 1)
    dec_31 = datetime.date(next_year, 12, 31)

    duration = st.sidebar.date_input(
        "Duration Date",
        (jan_1, datetime.date(next_year, 1, 7)),
        jan_1,
        dec_31,
        format="MM.DD.YYYY",
    )
    cost = st.sidebar.slider('Managing Your Trip Costs', 3000, 20000, 10000, 1000)
    trip_type = st.sidebar.multiselect(
    'Trip Type',
    ['Green', 'Yellow', 'Red', 'Blue'])
    additional_trip = st.text_input('Additional Trip Type')


if __name__ == "__main__":
    run()
