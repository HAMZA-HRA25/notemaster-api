from flask import Flask
from views.notes import notes_bp

# Initialisation de l'application Flask
app = Flask(__name__)

# Enregistrement du Blueprint des notes
app.register_blueprint(notes_bp)

# Point d'entrée pour l'exécution (utile pour les tests locaux)
if __name__ == '__main__':
    app.run(debug=True)
