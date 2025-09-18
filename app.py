from flask import Flask
from views.notes import notes_bp

app = Flask(__name__)

# Enregistrement du Blueprint
app.register_blueprint(notes_bp)

if __name__ == '__main__':
    app.run(debug=True)
