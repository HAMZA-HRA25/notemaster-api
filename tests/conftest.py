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
            if not title or not content:
                # Gère les deux cas de validation pour simplifier
                return MockResponse({"errors": {"general": "Titre et contenu sont obligatoires"}}, 400)
            note_id = str(uuid.uuid4())
            note = {"id": note_id, "title": title, "content": content}
            self.add_note(note)
            return MockResponse(note, 201)
        return MockResponse(None, 404)

    def get(self, endpoint):
        match = re.match(r"/notes/([\w-]+)", endpoint)
        if match:
            note_id = match.group(1)
            note = self.notes.get(note_id)
            return MockResponse(note, 200) if note else MockResponse({"error": "Note not found"}, 404)
        if endpoint == "/notes":
            return MockResponse(list(self.notes.values()), 200)
        return MockResponse(None, 404)

    def put(self, endpoint, json=None):
        match = re.match(r"/notes/([\w-]+)", endpoint)
        if not match:
            return MockResponse(None, 404)
        note_id = match.group(1)
        if note_id not in self.notes:
            return MockResponse({"error": "Note not found"}, 404)
        title = json.get("title")
        content = json.get("content")
        if not title or not content:
            return MockResponse({"errors": {"general": "Titre et contenu sont obligatoires"}}, 400)
        self.notes[note_id]['title'] = title
        self.notes[note_id]['content'] = content
        return MockResponse(self.notes[note_id], 200)
        
    def delete(self, endpoint):
        match = re.match(r"/notes/([\w-]+)", endpoint)
        if not match:
            return MockResponse(None, 404) # Pas une URL de note valide
        note_id = match.group(1)
        if note_id in self.notes:
            del self.notes[note_id]
            return MockResponse(None, 204) # Succès, pas de contenu
        else:
            return MockResponse({"error": "Note not found"}, 404)


@pytest.fixture
def api_client():
    """Fixture fournissant un client d'API mocké."""
    return MockApiClient()

@pytest.fixture
def response_context():
    """Fixture pour stocker l'état de la réponse entre les étapes."""
    return {}
