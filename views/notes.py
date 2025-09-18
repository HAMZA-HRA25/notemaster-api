import uuid
from flask import Blueprint, request, jsonify

# Création d'un Blueprint pour la fonctionnalité des notes
notes_bp = Blueprint('notes_api', __name__)

# "Base de données" en mémoire sous forme de liste
# Dans une vraie application, ce serait une base de données SQL ou NoSQL.
notes_db = []

@notes_bp.route('/notes', methods=['POST'])
def create_note():
    """
    Crée une nouvelle note.
    Attend un JSON avec "title" et "content".
    """
    # Récupérer les données JSON de la requête
    data = request.get_json()

    # Validation simple des données d'entrée
    if not data or not 'title' in data or not 'content' in data:
        return jsonify({'error': 'Le titre et le contenu sont requis.'}), 400

    # Création de la nouvelle note
    new_note = {
        'id': str(uuid.uuid4()),  # Génération d'un ID unique
        'title': data['title'],
        'content': data['content']
    }

    # Stockage de la note en mémoire
    notes_db.append(new_note)

    # Retourner la note créée avec le statut 201 Created
    return jsonify(new_note), 201
