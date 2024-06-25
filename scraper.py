import PyPDF2
import requests
from bs4 import BeautifulSoup

# all pdfs scraped from arxiv

def scrape_pdf(pdf_url):
    pdf = pypdf.PdfFileReader(pdf_url)
    text = pdf.get_text()
    return text

def scrape_arxiv():
    url = 'https://arxiv.org/search/?query=deep+learning&searchtype=all&source=header'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pdf_links = soup.find_all('a', {'title': 'Download PDF'})
    pdf_links = [link['href'] for link in pdf_links]
    pdf_texts = [scrape_pdf(link) for link in pdf_links]
    return pdf_texts

if __name__ == '__main__':
    pdf_texts = scrape_arxiv()
    print(pdf_texts)

