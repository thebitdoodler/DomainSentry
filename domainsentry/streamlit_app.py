import streamlit as st
import pandas as pd
import sys
import os
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from domainsentry.domain_sentry_core import process_domains

# Function to create a styled button
def styled_button(label, key, on_click=None, args=None):
    return st.button(
        label,
        key=key,
        help=f"Click to {label.lower()}",
        on_click=on_click,
        args=args,
    )

# Function to encode SVG
def get_image_base64(svg):
    return base64.b64encode(svg.encode('utf-8')).decode('utf-8')

# SVG Logo
logo_svg = '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200">
  <circle cx="100" cy="100" r="90" fill="#4a4a4a"/>
  <path d="M100 20 L180 180 H20 Z" fill="#3498db"/>
  <circle cx="100" cy="80" r="30" fill="#ecf0f1"/>
  <rect x="85" y="120" width="30" height="40" fill="#ecf0f1"/>
</svg>
'''

logo_base64 = get_image_base64(logo_svg)

def process_domain_batch(urls):
    return process_domains(urls)

def reset_app_state():
    st.session_state.results = None
    st.session_state.urls_input = ""

def main():
    st.set_page_config(page_title="DomainSentry", page_icon=":mag:", layout="wide")

    # Display logo
    st.markdown(
        f'<img src="data:image/svg+xml;base64,{logo_base64}" style="display: block; margin: auto; width: 100px; height: 100px;">',
        unsafe_allow_html=True
    )

    st.title("DomainSentry -The Ultimate WHOIS Extractor")

    # Initialize session state
    if 'results' not in st.session_state:
        st.session_state.results = None
    if 'urls_input' not in st.session_state:
        st.session_state.urls_input = ""

    # Input section
    st.header("Input")
    urls = st.text_area("Enter URLs or domains (one per line):", height=200, key="urls_input")

    col1, col2 = st.columns(2)

    with col1:
        extract_button = styled_button("Extract WHOIS Information", "extract")

    with col2:
        if st.session_state.results is not None:
            csv = pd.DataFrame(st.session_state.results).to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="domainsentry_results.csv",
                mime="text/csv",
            )

    # Process WHOIS information
    if extract_button:
        if urls:
            url_list = [url.strip() for url in urls.split("\n") if url.strip()]
            
            # Create a progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()

            # Process domains in parallel
            results = []
            with ThreadPoolExecutor(max_workers=10) as executor:
                future_to_url = {executor.submit(process_domain_batch, [url]): url for url in url_list}
                for i, future in enumerate(as_completed(future_to_url)):
                    url = future_to_url[future]
                    try:
                        data = future.result()
                        if data:
                            results.extend(data)
                    except Exception as exc:
                        st.error(f'{url} generated an exception: {exc}')
                    finally:
                        # Update progress less frequently
                        if i % 5 == 0 or i == len(url_list) - 1:
                            progress = (i + 1) / len(url_list)
                            progress_bar.progress(progress)
                            status_text.text(f"Processed {i+1}/{len(url_list)} domains")

            st.session_state.results = results
            status_text.text("Processing complete!")
            progress_bar.empty()
        else:
            st.warning("Please enter at least one URL or domain.")

    # Results section
    if st.session_state.results:
        st.header("Results")
        df = pd.DataFrame(st.session_state.results)
        st.dataframe(df)

        # Reset button after the table
        reset_button = styled_button("Extract More", "reset", on_click=reset_app_state)

if __name__ == "__main__":
    main()