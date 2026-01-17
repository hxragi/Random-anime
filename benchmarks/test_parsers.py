"""Benchmarks for anime parsing functions."""
import pytest
from bs4 import BeautifulSoup

from parsers import parse_anime_name, parse_anime_eps, parse_anime_genres


# Sample HTML that matches the actual selectors from config.py
# Selectors: 
# - ANIME_NAME_SELECTOR: ".anime-title > div:nth-child(1) > h1:nth-child(1)"
# - ANIME_EPISODES_SELECTOR: "dd.col-6:nth-child(4)"
# - ANIME_GENRES_SELECTOR: "dd.col-6:nth-child(8) a"
SAMPLE_HTML = """
<html>
<body>
    <div class="anime-title">
        <div>
            <h1>Test Anime Name</h1>
        </div>
    </div>
    <dl>
        <dt>First</dt>
        <dd class="col-6">Value 1</dd>
        <dt>Second</dt>
        <dd class="col-6">24 эпизода</dd>
        <dt>Third</dt>
        <dd class="col-6">Value 3</dd>
        <dt>Fourth</dt>
        <dd class="col-6">
            <a href="/genre/action">Action</a>
            <a href="/genre/comedy">Comedy</a>
            <a href="/genre/drama">Drama</a>
        </dd>
    </dl>
</body>
</html>
"""


@pytest.fixture
def sample_soup():
    """Create a BeautifulSoup object from sample HTML."""
    return BeautifulSoup(SAMPLE_HTML, "lxml")


@pytest.mark.benchmark
def test_parse_anime_name(sample_soup):
    """Benchmark parsing anime name."""
    result = parse_anime_name(sample_soup)
    assert result == "Test Anime Name"


@pytest.mark.benchmark
def test_parse_anime_eps(sample_soup):
    """Benchmark parsing anime episodes."""
    result = parse_anime_eps(sample_soup)
    assert "24" in result


@pytest.mark.benchmark
def test_parse_anime_genres(sample_soup):
    """Benchmark parsing anime genres."""
    result = parse_anime_genres(sample_soup)
    assert len(result) == 3
    assert "Action" in result


@pytest.mark.benchmark
def test_parse_all_fields(sample_soup):
    """Benchmark parsing all anime fields together."""
    name = parse_anime_name(sample_soup)
    eps = parse_anime_eps(sample_soup)
    genres = parse_anime_genres(sample_soup)
    
    assert name is not None
    assert eps is not None
    assert len(genres) > 0


@pytest.mark.benchmark
def test_beautifulsoup_parsing():
    """Benchmark BeautifulSoup HTML parsing."""
    soup = BeautifulSoup(SAMPLE_HTML, "lxml")
    assert soup is not None
    assert soup.select_one(".anime-title") is not None
