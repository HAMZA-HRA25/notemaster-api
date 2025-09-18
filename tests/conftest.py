import pytest
import uuid

class MockResponse:
    """Une classe pour simuler une réponse HTTP."""
    def __init__(self, json_data, status_code):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data

class MockApiClient:
    """Un client d'API mocké pour simuler les appels HTTP."""
    def post(self, endpoint, json=None):
        if endpoint == "/notes":
            if not json:
                return MockResponse({"errors": {"general": "Payload manquant"}}, 400)

            title = json.get("title")
            content = json.get("content")

            if not title:
                return MockResponse({"errors": {"titre": "Le titre est obligatoire"}}, 400)
            if not content:
                return MockResponse({"errors": {"contenu": "Le contenu est obligatoire"}}, 400)
            
            # Cas de succès
            note = {
                "id": str(uuid.uuid4()),
                "title": title,
                "content": content
            }
            return MockResponse(note, 201)
        
        return MockResponse(None, 404)

@pytest.fixture
def api_client():
    """Fixture fournissant un client d'API mocké."""
    return MockApiClient()

@pytest.fixture
def response_context():
    """Fixture pour stocker l'état de la réponse entre les étapes."""
    return {}
