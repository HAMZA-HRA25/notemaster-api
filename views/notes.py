import uuid
from flask import Blueprint, request, jsonify

# Création d'un Blueprint pour la fonctionnalité des notes
notes_bp = Blueprint('notes_api', __name__)

# "Base de données" en mémoire sous forme de liste
notes_db = []

@notes_bp.route('/notes', methods=['POST'])
def create_note():
    """
    Crée une nouvelle note.
    Attend un JSON avec "title" et "content".
    """
    data = request.get_json()
    if not data or not 'title' in data or not 'content' in data:
        return jsonify({'error': 'Le titre et le contenu sont requis.'}), 400

    new_note = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'content': data['content']
    }
    notes_db.append(new_note)
    return jsonify(new_note), 201

# --- NOUVEAU CODE CI-DESSOUS ---

@notes_bp.route('/notes', methods=['GET'])
def get_all_notes():
    """
    Retourne la liste de toutes les notes.
    """
    return jsonify(notes_db)

@notes_bp.route('/notes/<note_id>', methods=['GET'])
def get_note_by_id(note_id):
    """
    Retourne une note spécifique par son ID.
    """
    # Recherche de la note dans la "base de données" en mémoire
    note = next((note for note in notes_db if note['id'] == note_id), None)
    
    if note:
        return jsonify(note)
    else:
        # Si la note n'est pas trouvée, retourner une erreur 404
        return jsonify({'error': 'Note non trouvée.'}), 404
