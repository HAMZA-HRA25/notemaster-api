from flask import Blueprint, jsonify, request

# Création d'un Blueprint pour les notes
notes_bp = Blueprint('notes', __name__, url_prefix='/notes')

# Données en mémoire pour simuler une base de données
notes = [
    {"id": 1, "title": "Note Initiale 1", "content": "Ceci est une note d'exemple."},
    {"id": 2, "title": "Note Initiale 2", "content": "Ceci est une autre note d'exemple."}
]
next_id = 3

@notes_bp.route('/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    """Met à jour une note existante."""
    # Recherche de la note dans notre "base de données" en mémoire
    note = next((note for note in notes if note['id'] == note_id), None)

    # Si la note n'est pas trouvée, retourner une erreur 404
    if note is None:
        return jsonify({'error': 'Note not found'}), 404

    # Récupérer les données JSON de la requête
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid data'}), 400

    # Mettre à jour les champs de la note
    # Utilise .get() pour garder l'ancienne valeur si une nouvelle n'est pas fournie
    note['title'] = data.get('title', note['title'])
    note['content'] = data.get('content', note['content'])

    # Retourner la note mise à jour avec le statut 200 OK
    return jsonify(note), 200
