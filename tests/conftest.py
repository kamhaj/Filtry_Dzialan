# conftest.py
# shared among all (future) apps


@pytest.fixture
def api_client():
    return APIClient