# language: fr
Fonctionnalité: Lecture des notes
  Pour permettre aux utilisateurs de consulter les informations sauvegardées
  En tant qu'utilisateur de l'API
  Je veux pouvoir récupérer la liste des notes et consulter une note spécifique par son ID.

  Scénario: Récupération réussie de la liste des notes
    Étant donné que plusieurs notes existent dans le système
    Quand je fais une requête GET à "/notes"
    Alors la réponse doit avoir le statut 200
    Et le corps de la réponse doit contenir une liste de notes

  Scénario: Récupération d'une liste de notes vide
    Étant donné qu'aucune note n'existe dans le système
    Quand je fais une requête GET à "/notes"
    Alors la réponse doit avoir le statut 200
    Et le corps de la réponse doit être une liste vide

  Scénario: Récupération réussie d'une note par son ID
    Étant donné qu'une note avec l'ID "note-existante-123" existe
    Quand je fais une requête GET à "/notes/note-existante-123"
    Alors la réponse doit avoir le statut 200
    Et le corps de la réponse doit contenir la note avec l'ID "note-existante-123"

  Scénario: Tentative de récupération d'une note avec un ID inexistant
    Quand je fais une requête GET à "/notes/id-inexistant-456"
    Alors la réponse doit avoir le statut 404
    Et le corps de la réponse doit contenir un message d'erreur de note non trouvée
