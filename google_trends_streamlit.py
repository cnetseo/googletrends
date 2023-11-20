import streamlit as st
import requests
import time

@st.cache_data(ttl=14400,max_entries=1)
def getGoogleTrends(keywords):
    url = 'https://serpapi.com/search.json?'
  
  
    params = {
            "engine": "google_trends",
            "q": keyword,
            "data_type": "RELATED_QUERIES",
            "date": "now 4-H",
            "geo": "US",
            "api_key": st.secrets['general']["SERPAPI_KEY"]
        }

    response = requests.get(url, params=params)
    time.sleep(0.5)  # sleep for half a second

    if response.status_code == 200:
        json = response.json()
        if 'related_queries' in json:
            for query_type in ['rising', 'top']:
                if query_type in json['related_queries']:
                    queries = [(item.get('query', 'N/A'), item.get('extracted_value', 'N/A')) for item in json['related_queries'][query_type][:10]]
                    with st.expander(f"Top 10 {query_type} queries for {keyword}"):
                         st.markdown('\n'.join(f'- [{query}](https://trends.google.com/trends/explore?date=now%204-H&geo=US&q={query.replace(" ", "%20")}&hl=en) - Value: {value}' for query, value in queries))


keywords = [
    "Best Black Friday Deals",
    "Black Friday Deals",
    "Black Friday Apple Watch Deals",
    "Best Black Friday Apple Watch Deals",
    "Black Friday TV Deals",
    "Best Black Friday TV Deals",
    "Black Friday Phone Deals",
    "Best Black Friday Phone Deals",
    "Black Friday Laptop Deals",
    "Best Black Friday Laptop Deals",
    "Black Friday Mattress Deals",
    "Best Black Friday Mattress Deals",
    "Black Friday Home Deals",
    "Best Black Friday Home Deals",
    "Best Soundbar Black Friday Deals",
    "Black Friday Soundbar Deals",
    "Apple Black Friday Deals",
    "Best Apple Black Friday Deals",
    "Best Black Friday Walmart Deals",
    "Black Friday Walmart Deals",
    "Amazon Black Friday Deals",
    "Best Amazon Black Friday Deals",
    "Black Friday Deals Under $100",
    "Black Friday Deals Under $25",
    "Black Friday Deals Under $50",
    "Black friday tech deals",
    "Best Black friday tech deals",
    "Target Black Friday Ads",
    "Black Friday iPhone Deals",
    "Black Friday iPad Deals",
    "Best Black Friday iPad Deals",
    "Black Friday Nintendo Switch Deals",
    "Best Black Friday Nintendo Switch Deals",
    "Black Friday Robot Vacuum Deals",
    "Best Black Friday Robot Vacuum Deals",
    "Black Friday Air Fryer Deals",
    "Best Black Friday Air Fryer Deals",
    "Black Friday Airpods Deals",
    "Best Black Friday Airpods Deals",
    "Best Black Friday Ps5 Deals",
    "Black Friday Ps5 Deals",
    "Black Friday Headphone Deals",
    "Best Black Friday Headphone Deals",
    "Black Friday Roku Deals",
    "Best Black Friday Roku Deals",
    "Xbox Black Friday Deals",
    "Playstation Black Friday Deals",
    "Ring Black Friday Deals",
    "Best Xbox Black Friday Deals",
    "Best Playstation Black Friday Deals",
    "Best Ring Black Friday Deals",
    "Best Buy Black Friday Deals"
]

st.title('Google Trending Topics')
st.write("""This app shows the top Google trending queries for a predetermined set of keywords""")

for keyword in keywords:
    getGoogleTrends(keyword)
