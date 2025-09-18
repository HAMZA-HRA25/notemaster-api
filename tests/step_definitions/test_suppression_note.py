from pytest_bdd import scenario, given, when, then, parsers

# Scénarios
@scenario('../features/suppression_note.feature', "Suppression réussie d'une note existante")
def test_suppression_reussie():
    pass

@scenario('../features/suppression_note.feature', "Tentative de suppression d'une note inexistante")
def test_suppression_note_inexistante():
    pass

# Étapes (Steps)

# Given
@given(parsers.parse('qu\'une note avec l\'ID "{note_id}" existe'))
def given_une_note_specifique_existe(api_client, note_id):
    api_client.clear_notes()
    api_client.add_note({"id": note_id, "title": "Note à supprimer", "content": "Ce contenu va être supprimé."})

@given(parsers.parse('qu\'aucune note avec l\'ID "{note_id}" n\'existe'))
def given_aucune_note_specifique_existe(api_client, note_id):
    api_client.clear_notes()
    # On s'assure juste que la note n'y est pas
    if note_id in api_client.notes:
        del api_client.notes[note_id]

# When
@when(parsers.parse('je fais une requête DELETE à "{endpoint}"'))
def delete_request(api_client, response_context, endpoint):
    response_context['response'] = api_client.delete(endpoint)

# Then
@then(parsers.parse("la réponse doit avoir le statut {status_code:d}"))
def check_status_code(response_context, status_code):
    assert response_context['response'].status_code == status_code

@then(parsers.parse('la note avec l\'ID "{note_id}" ne doit plus exister'))
def check_note_is_deleted(api_client, note_id):
    assert note_id not in api_client.notes

@then("le corps de la réponse doit contenir un message d'erreur de note non trouvée")
def check_response_is_not_found_error(response_context):
    data = response_context['response'].json()
    assert 'error' in data
    assert "not found" in data['error'].lower()
