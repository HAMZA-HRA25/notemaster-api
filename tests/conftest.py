import pytest
import uuid
import re

class MockResponse:
    """Une classe pour simuler une réponse HTTP."""
    def __init__(self, json_data, status_code):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data

class MockApiClient:
    """Un client d'API mocké pour simuler les appels HTTP."""
    def __init__(self):
        self.notes = {} # Stockage en mémoire pour les notes

    def clear_notes(self):
        self.notes = {}

    def add_note(self, note_data):
        self.notes[note_data['id']] = note_data

    def post(self, endpoint, json=None):
        if endpoint == "/notes":
            title = json.get("title")
            content = json.get("content")

            if not title:
                return MockResponse({"errors": {"titre": "Le titre est obligatoire"}}, 400)
            if not content:
                return MockResponse({"errors": {"contenu": "Le contenu est obligatoire"}}, 400)
            
            note_id = str(uuid.uuid4())
            note = {"id": note_id, "title": title, "content": content}
            self.add_note(note)
            return MockResponse(note, 201)
        
        return MockResponse(None, 404)

    def get(self, endpoint):
        # Cas pour GET /notes/{id}
        match = re.match(r"/notes/([\w-]+)", endpoint)
        if match:
            note_id = match.group(1)
            note = self.notes.get(note_id)
            if note:
                return MockResponse(note, 200)
            else:
                return MockResponse({"error": "Note not found"}, 404)

        # Cas pour GET /notes
        if endpoint == "/notes":
            return MockResponse(list(self.notes.values()), 200)

        return MockResponse(None, 404)


@pytest.fixture
def api_client():
    """Fixture fournissant un client d'API mocké."""
    return MockApiClient()

@pytest.fixture
def response_context():
    """Fixture pour stocker l'état de la réponse entre les étapes."""
    return {}
