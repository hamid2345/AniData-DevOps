import pytest
from src.scraper import parse_anime_list

def test_parse_anime_list_with_multiple_items():
    html = '''
    <div class="anime-item">
        <span class="title">Naruto</span>
        <span class="rating">8.5</span>
        <a href="/naruto">Lien</a>
    </div>
    <div class="anime-item">
        <span class="title">One Piece</span>
        <span class="rating">9.0</span>
        <a href="/onepiece">Lien</a>
    </div>
    '''
    result = parse_anime_list(html)
    assert len(result) == 2
    assert result[0]['title'] == 'Naruto'
    assert result[1]['title'] == 'One Piece'

def test_parse_anime_list_empty():
    result = parse_anime_list("<div>rien</div>")
    assert result == []