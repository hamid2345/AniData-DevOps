import json
import os
import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text

def parse_anime_list(html):
    soup = BeautifulSoup(html, 'html.parser')
    animes = []
    
    for item in soup.select('.anime-item'):
        title_elem = item.select_one('.title')
        rating_elem = item.select_one('.rating')
        link_elem = item.select_one('a')
        
        anime = {
            'title': title_elem.text.strip() if title_elem else 'N/A',
            'rating': rating_elem.text.strip() if rating_elem else 'N/A',
            'url': link_elem.get('href', '') if link_elem else ''
        }
        animes.append(anime)
    
    return animes

def save_to_json(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def run_scraper(target_url, output_path):
    print(f"Scraping {target_url}...")
    html = fetch_page(target_url)
    data = parse_anime_list(html)
    save_to_json(data, output_path)
    print(f"Sauvegardé {len(data)} animes dans {output_path}")
    return len(data)