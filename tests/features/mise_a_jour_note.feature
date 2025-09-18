# language: fr
Fonctionnalité: Mise à jour d'une note
  Pour permettre aux utilisateurs de modifier les informations existantes
  En tant qu'utilisateur de l'API
  Je veux pouvoir mettre à jour une note en utilisant son ID.

  Scénario: Mise à jour réussie d'une note existante
    Étant donné qu'une note avec l'ID "note-a-modifier-123" existe
    Quand je fais une requête PUT à "/notes/note-a-modifier-123" avec le titre "Titre mis à jour" et le contenu "Contenu mis à jour."
    Alors la réponse doit avoir le statut 200
    Et le corps de la réponse doit contenir la note avec le titre "Titre mis à jour"

  Scénario: Tentative de mise à jour d'une note inexistante
    Quand je fais une requête PUT à "/notes/id-inexistant-789" avec des données valides
    Alors la réponse doit avoir le statut 404
    Et le corps de la réponse doit contenir un message d'erreur de note non trouvée

  Scénario: Tentative de mise à jour d'une note avec un titre manquant
    Étant donné qu'une note avec l'ID "note-a-valider-456" existe
    Quand je fais une requête PUT à "/notes/note-a-valider-456" avec un titre manquant et le contenu "Contenu valide."
    Alors la réponse doit avoir le statut 400
    Et le corps de la réponse doit contenir un message d'erreur pour le champ "titre"
