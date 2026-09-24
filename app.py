import streamlit as st
from scraper import scrape_amazon


st.set_page_config(
    page_title="Amazon H1 Scraper",
    page_icon="📰",
    layout="wide"
)


st.title("Aaj Tak H1 Header Scraper")

st.write(
    "Scrape H1 headers and related information "
    "from the Amazon homepage."
)


if st.button("Scrape amazon"):

    with st.spinner("Scraping website..."):

        try:

            df = scrape_amazon()

            st.success(
                f"Scraping completed. "
                f"{len(df)} H1 headers found."
            )

            st.dataframe(
                df,
                use_container_width=True
            )

            csv_data = df.to_csv(
                index=False,
                encoding="utf-8-sig"
            )

            st.download_button(
                label="Download CSV",
                data=csv_data,
                file_name="amazon_h1_data.csv",
                mime="text/csv"
            )

        except Exception as e:

            st.error(
                f"Scraping failed: {e}"
            )