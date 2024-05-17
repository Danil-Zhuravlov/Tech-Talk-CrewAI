import json
import os

import requests
from langchain.tools import tool



class SearchTools():

    @tool("Search the internet")
    def search_internet(query):
        """Useful to search the internet
        about a a given topic and return relevant results"""
        top_result_to_return = 4
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        # check if there is an organic key
        if 'organic' not in response.json():
            return "Sorry, I couldn't find anything about that, there could be an error with you serper api key."
        else:
            results = response.json()['organic']
            string = []
            for result in results[:top_result_to_return]:
                try:
                    string.append('\n'.join([
                        f"Title: {result['title']}", f"Link: {result['link']}",
                        f"Snippet: {result['snippet']}", "\n-----------------"
                    ]))
                except KeyError:
                    next

            return '\n'.join(string)

class ScrapeWebsite():

    @tool("Scrape website")
    def scrape_website(url):
        """Scrapes a given website URL and returns the content"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to retrieve content from {url}"


class SearchWikipedia():

    @tool("Search Wikipedia")
    def search_wikipedia(query):
        """Search Wikipedia for a given query and return the summary"""
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"Title: {data['title']}\nSummary: {data['extract']}\nLink: {data['content_urls']['desktop']['page']}"
        else:
            return f"Failed to retrieve information from Wikipedia for query: {query}"

class SearchNews():

    @tool("Search news")
    def search_news(query):
        """Search the latest news for a given query and return relevant articles"""
        url = "https://newsapi.org/v2/everything"
        params = {
            'q': query,
            'apiKey': os.getenv('NEWS_API_KEY'),
            'sortBy': 'relevancy',
            'pageSize': 4
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            articles = response.json()['articles']
            results = []
            for article in articles:
                results.append(f"Title: {article['title']}\nLink: {article['url']}\nSnippet: {article['description']}\n-----------------")
            return '\n'.join(results)
        else:
            return f"Failed to retrieve news for query: {query}"

# Use this code if you don't have semantics scholar API key

#    @tool("Search for academic papers")
#    def search_academic_papers(query):
#        """Search for academic papers related to a given topic"""
#        url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit=5"
#        response = requests.get(url)
#        if response.status_code != 200:
#            return "Sorry, I couldn't retrieve academic papers at this time."
#        
#        papers = response.json().get('data', [])
#        if not papers:
#            return "No academic papers found for the query."
#        
#        results = []
#        for paper in papers:
#            title = paper.get('title', 'No title')
#            authors = ', '.join([author.get('name', 'Unknown') for author in paper.get('authors', [])])
#            url = paper.get('url', 'No URL')
#            results.append(f"Title: {title}\nAuthors: {authors}\nURL: {url}\n-----------------")
#        
#        return '\n'.join(results)


# Use this code if you have semantic scholar API key

class SearchAcademicPapers():

    @tool("Search academic papers")
    def search_academic_papers(query):
        """Search for academic papers related to a given query"""
        url = "https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            'query': query,
          'fields': 'title,abstract,authors,url',
            'limit': 4
        }
        headers = {
            'x-api-key': os.getenv('SEMANTIC_SCHOLAR_API_KEY')
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            papers = response.json()['data']
            results = []
            for paper in papers:
               authors = ', '.join(author['name'] for author in paper['authors'])
               results.append(f"Title: {paper['title']}\nAuthors: {authors}\nAbstract: {paper['abstract']}\nLink: {paper['url']}\n-----------------")
            return '\n'.join(results)
        else:
            return f"Failed to retrieve academic papers for query: {query}"
