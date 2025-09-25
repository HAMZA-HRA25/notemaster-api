# Hamza asked me to write this
from flask import Flask
from views.notes import notes_bp

# Initialisation de l'application Flask
app = Flask(__name__)

# Enregistrement du Blueprint pour les notes
# Toutes les routes définies dans notes_bp seront préfixées par / si url_prefix n'est pas défini.
app.register_blueprint(notes_bp)

# Point d'entrée pour l'exécution directe (pour le développement local)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
