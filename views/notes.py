from flask import Blueprint, jsonify, request

notes_bp = Blueprint('notes', __name__, url_prefix='/notes')

# Données en mémoire pour simuler une base de données
notes = [
    {"id": 1, "title": "Note à supprimer", "content": "Ce contenu est destiné à être supprimé."},
    {"id": 2, "title": "Autre note", "content": "Celle-ci restera."}
]

@notes_bp.route('/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    """Supprime une note existante."""
    global notes
    # Recherche de la note dans la liste
    note = next((note for note in notes if note['id'] == note_id), None)

    # Si la note n'est pas trouvée, retourner une erreur 404
    if note is None:
        return jsonify({'error': 'Note not found'}), 404

    # Supprimer la note de la liste
    notes.remove(note)

    # Retourner une réponse vide avec le statut 204 No Content
    return '', 204
