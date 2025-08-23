from fastapi.testclient import TestClient
from main import app

# Initialize the TestClient with your FastAPI app
client = TestClient(app)

def test_get_cities_for_spain():
    # Mock data for testing (ensure the "data" dictionary in your app contains an entry for Spain)
    app.data = {
        "Spain": {
            "Madrid": {},
            "Barcelona": {},
            "Valencia": {}
        }
    }
    
    # Send a GET request to the route with "Spain" as the country
    response = client.get("/countries/Spain/cities")
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Extract the JSON response
    cities = response.json()

    # Assert that the response is a list (assuming cities are stored as a list in your `data`)
    assert isinstance(cities, list)

    # Example: Assert that specific cities are in the response (update these based on your actual data)
    expected_cities = ["Madrid", "Barcelona", "Valencia"]
    for city in expected_cities:
        assert city in cities

    # Assert that there are no unexpected cities
    assert set(cities) == set(expected_cities)
