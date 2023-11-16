import streamlit as st
import requests
import time

def getGoogleTrends(keywords):
    url = 'https://serpapi.com/search.json?'
  
    for keyword in keywords:
        st.write(f"## {keyword}")
        params = {
            "engine": "google_trends",
            "q": keyword,
            "data_type": "RELATED_QUERIES",
            "date": "now 1-H",
            "geo": "US",
            "api_key": "Your_API_KEY"
        }

        response = requests.get(url, params=params)
        time.sleep(0.5)  # sleep for half a second

        if response.status_code == 200:
            json = response.json()
            if 'related_queries' in json:
                for query_type in ['rising', 'top']:
                    if query_type in json['related_queries']:
                        queries = [item['query'] for item in json['related_queries'][query_type][:5]]
                        st.write(f"### Top 5 {query_type} queries for {keyword}")
                        st.write('\n'.join(queries))

keywords = ['tv deals', 'black friday deals', 'amazon deals']  # Replace with your keywords

st.title('Google Trending Topics')
st.write("""This app shows the top Google trending queries for a predetermined set of keywords""")

getGoogleTrends(keywords)