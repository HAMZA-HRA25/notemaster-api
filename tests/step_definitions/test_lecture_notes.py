from pytest_bdd import scenario, given, when, then, parsers

# Scénarios
@scenario('../features/lecture_notes.feature', "Récupération réussie de la liste des notes")
def test_lecture_liste_notes():
    pass

@scenario('../features/lecture_notes.feature', "Récupération d'une liste de notes vide")
def test_lecture_liste_vide():
    pass

@scenario('../features/lecture_notes.feature', "Récupération réussie d'une note par son ID")
def test_lecture_note_par_id():
    pass

@scenario('../features/lecture_notes.feature', "Tentative de récupération d'une note avec un ID inexistant")
def test_lecture_note_id_inexistant():
    pass


# Étapes (Steps)

# Given
@given("que plusieurs notes existent dans le système")
def given_plusieurs_notes_existent(api_client):
    api_client.clear_notes()
    api_client.add_note({"id": "note-1", "title": "Première note", "content": "Contenu 1"})
    api_client.add_note({"id": "note-2", "title": "Deuxième note", "content": "Contenu 2"})

@given("qu'aucune note n'existe dans le système")
def given_aucune_note_existe(api_client):
    api_client.clear_notes()

@given(parsers.parse('qu\'une note avec l\'ID "{note_id}" existe'))
def given_une_note_specifique_existe(api_client, note_id):
    api_client.clear_notes()
    api_client.add_note({"id": note_id, "title": "Note spécifique", "content": "Contenu spécifique"})

# When
@when(parsers.parse('je fais une requête GET à "{endpoint}"'))
def get_request(api_client, response_context, endpoint):
    response_context['response'] = api_client.get(endpoint)

# Then
@then(parsers.parse("la réponse doit avoir le statut {status_code:d}"))
def check_status_code(response_context, status_code):
    assert response_context['response'].status_code == status_code

@then("le corps de la réponse doit contenir une liste de notes")
def check_response_is_list_of_notes(response_context):
    data = response_context['response'].json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'id' in data[0]
    assert 'title' in data[0]

@then("le corps de la réponse doit être une liste vide")
def check_response_is_empty_list(response_context):
    data = response_context['response'].json()
    assert isinstance(data, list)
    assert len(data) == 0

@then(parsers.parse('le corps de la réponse doit contenir la note avec l\'ID "{note_id}"'))
def check_response_contains_note_id(response_context, note_id):
    data = response_context['response'].json()
    assert isinstance(data, dict)
    assert data.get('id') == note_id

@then("le corps de la réponse doit contenir un message d'erreur de note non trouvée")
def check_response_is_not_found_error(response_context):
    data = response_context['response'].json()
    assert 'error' in data
    assert "not found" in data['error'].lower()
