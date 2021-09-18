from flask import url_for
from werkzeug.wrappers import response

def test_home(client):
    # make a request to our application
    response = client.get('/')
    assert response.status_code == 200
    assert 'Welcome to StockApp' in str(response.data)

def test_search(client):
    response = client.post(url_for('home.search'), data={ 'ticker': 'AAPL' })
    assert response.status_code == 302
    assert response.location == url_for('stock.quote', ticker='AAPL', _external=True)
