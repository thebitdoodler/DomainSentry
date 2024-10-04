import streamlit as st
import pandas as pd
from .domain_sentry_core import process_domains

def main():
    st.title("DomainSentry - Threat Intelligence WHOIS Extractor")

    urls = st.text_area("Enter URLs or domains (one per line):", height=200)
    
    if st.button("Extract WHOIS Information"):
        if urls:
            url_list = urls.split("\n")
            results = process_domains(url_list)
            
            df = pd.DataFrame(results)
            st.dataframe(df)
            
            csv = df.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="domainsentry_results.csv",
                mime="text/csv",
            )
        else:
            st.warning("Please enter at least one URL or domain.")

if __name__ == "__main__":
    main()