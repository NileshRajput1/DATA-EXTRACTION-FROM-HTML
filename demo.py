from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests
app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape',methods=['POST','GET'])

def scrape():
    url = request.form.get('url')
    keyword = request.form.get('keyword', '').lower()  # Convert keyword to lowercase for case-insensitive matching

    if not url:
        return "Please provide a URL."
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    output = []

    description = soup.find('meta', attrs={'name': 'description'})
    if description:
        output.append(f"Page Description: {description.get('content')}")
    
    keyword_count = soup.get_text().lower().count(keyword)
    output.append(f"Occurrences of '{keyword}': {keyword_count}")
    if keyword == 'title':
        title = soup.title.string if soup.title else 'No title found'
        output.append(f"Title: {title}")
    
    elif keyword == 'headings':
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        output.append("Headings:")
        for heading in headings:
            output.append(heading.text)
    
    elif keyword == 'links':
        links = soup.find_all('a')
        output.append("Links:")
        for link in links:
            output.append(link.get('href'))
    
    elif keyword == 'tables':
        tables = soup.find_all('table')
        output.append("Tables:")
        for table in tables:
            output.append(table.get_text())
    
    elif keyword == 'paragraphs':
        paragraphs = soup.find_all('p')
        output.append("Paragraphs:")
        for paragraph in paragraphs:
            output.append(paragraph.text)
    
    elif keyword == 'metadata':
        metadata = soup.find_all('meta')
        output.append("Metadata:")
        for meta in metadata:
            output.append(meta.get('content'))
    
    else:
        specific_tags = soup.find_all(keyword)
        output.append(f"{keyword.capitalize()}:")
        for tag in specific_tags:
            output.append(tag.text)
    
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
