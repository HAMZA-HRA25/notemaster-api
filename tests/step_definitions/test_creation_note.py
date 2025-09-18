from pytest_bdd import scenario, given, when, then, parsers

# Scénarios
@scenario('../features/creation_note.feature', "Création réussie d'une note avec un titre et un contenu")
def test_creation_reussie():
    pass

@scenario('../features/creation_note.feature', "Échec de la création d'une note sans titre")
def test_creation_sans_titre():
    pass

@scenario('../features/creation_note.feature', "Échec de la création d'une note sans contenu")
def test_creation_sans_contenu():
    pass


# Étapes (Steps)
@when(parsers.parse('je fais une requête POST à "{endpoint}" avec le titre "{title}" et le contenu "{content}"'))
def post_note_success(api_client, response_context, endpoint, title, content):
    payload = {"title": title, "content": content}
    response_context['response'] = api_client.post(endpoint, json=payload)

@when(parsers.parse('je fais une requête POST à "{endpoint}" avec un titre manquant et le contenu "{content}"'))
def post_note_missing_title(api_client, response_context, endpoint, content):
    payload = {"content": content}
    response_context['response'] = api_client.post(endpoint, json=payload)

@when(parsers.parse('je fais une requête POST à "{endpoint}" avec le titre "{title}" et un contenu manquant'))
def post_note_missing_content(api_client, response_context, endpoint, title):
    payload = {"title": title}
    response_context['response'] = api_client.post(endpoint, json=payload)


@then(parsers.parse("la réponse doit avoir le statut {status_code:d}"))
def check_status_code(response_context, status_code):
    assert response_context['response'].status_code == status_code

@then(parsers.parse('le corps de la réponse doit contenir la note avec le titre "{title}" et le contenu "{content}"'))
def check_response_body_success(response_context, title, content):
    data = response_context['response'].json()
    assert data['title'] == title
    assert data['content'] == content
    assert 'id' in data

@then(parsers.parse('le corps de la réponse doit contenir un message d''erreur pour le champ "{field}"'))
def check_response_body_error(response_context, field):
    data = response_context['response'].json()
    assert 'errors' in data
    assert field in data['errors']
