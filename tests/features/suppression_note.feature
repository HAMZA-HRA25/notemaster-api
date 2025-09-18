# language: fr
Fonctionnalité: Suppression d'une note
  Pour permettre aux utilisateurs de supprimer des informations devenues inutiles
  En tant qu'utilisateur de l'API
  Je veux pouvoir supprimer une note en utilisant son ID.

  Scénario: Suppression réussie d'une note existante
    Étant donné qu'une note avec l'ID "note-a-supprimer-123" existe
    Quand je fais une requête DELETE à "/notes/note-a-supprimer-123"
    Alors la réponse doit avoir le statut 204
    Et la note avec l'ID "note-a-supprimer-123" ne doit plus exister

  Scénario: Tentative de suppression d'une note inexistante
    Étant donné qu'aucune note avec l'ID "id-inexistant-999" n'existe
    Quand je fais une requête DELETE à "/notes/id-inexistant-999"
    Alors la réponse doit avoir le statut 404
    Et le corps de la réponse doit contenir un message d'erreur de note non trouvée
