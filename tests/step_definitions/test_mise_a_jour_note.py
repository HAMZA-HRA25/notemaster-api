from pytest_bdd import scenario, given, when, then, parsers

# Scénarios
@scenario('../features/mise_a_jour_note.feature', "Mise à jour réussie d'une note existante")
def test_mise_a_jour_reussie():
    pass

@scenario('../features/mise_a_jour_note.feature', "Tentative de mise à jour d'une note inexistante")
def test_mise_a_jour_note_inexistante():
    pass

@scenario('../features/mise_a_jour_note.feature', "Tentative de mise à jour d'une note avec un titre manquant")
def test_mise_a_jour_avec_validation_erreur():
    pass


# Étapes (Steps)

# Given (réutilisé de test_lecture_notes)
@given(parsers.parse('qu\'une note avec l\'ID "{note_id}" existe'))
def given_une_note_specifique_existe(api_client, note_id):
    api_client.clear_notes()
    api_client.add_note({"id": note_id, "title": "Titre original", "content": "Contenu original"})

# When
@when(parsers.parse('je fais une requête PUT à "{endpoint}" avec le titre "{title}" et le contenu "{content}"'))
def put_request_success(api_client, response_context, endpoint, title, content):
    payload = {"title": title, "content": content}
    response_context['response'] = api_client.put(endpoint, json=payload)

@when(parsers.parse('je fais une requête PUT à "{endpoint}" avec des données valides'))
def put_request_valid_data(api_client, response_context, endpoint):
    payload = {"title": "Titre valide", "content": "Contenu valide"}
    response_context['response'] = api_client.put(endpoint, json=payload)

@when(parsers.parse('je fais une requête PUT à "{endpoint}" avec un titre manquant et le contenu "{content}"'))
def put_request_missing_title(api_client, response_context, endpoint, content):
    payload = {"content": content}
    response_context['response'] = api_client.put(endpoint, json=payload)


# Then (réutilisés)
@then(parsers.parse("la réponse doit avoir le statut {status_code:d}"))
def check_status_code(response_context, status_code):
    assert response_context['response'].status_code == status_code

@then(parsers.parse('le corps de la réponse doit contenir la note avec le titre "{title}"'))
def check_response_body_title(response_context, title):
    data = response_context['response'].json()
    assert data['title'] == title

@then("le corps de la réponse doit contenir un message d'erreur de note non trouvée")
def check_response_is_not_found_error(response_context):
    data = response_context['response'].json()
    assert 'error' in data
    assert "not found" in data['error'].lower()

@then(parsers.parse('le corps de la réponse doit contenir un message d\'erreur pour le champ "{field}"'))
def check_response_body_error(response_context, field):
    data = response_context['response'].json()
    assert 'errors' in data
    assert field in data['errors']
