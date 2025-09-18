# language: fr
Fonctionnalité: Création d'une note
  Pour permettre aux utilisateurs de sauvegarder des informations
  En tant qu'utilisateur de l'API
  Je veux pouvoir créer une nouvelle note

  Scénario: Création réussie d'une note avec un titre et un contenu
    Quand je fais une requête POST à "/notes" avec le titre "Ma première note" et le contenu "Ceci est le contenu de ma note."
    Alors la réponse doit avoir le statut 201
    Et le corps de la réponse doit contenir la note avec le titre "Ma première note" et le contenu "Ceci est le contenu de ma note."

  Scénario: Échec de la création d'une note sans titre
    Quand je fais une requête POST à "/notes" avec un titre manquant et le contenu "Note sans titre."
    Alors la réponse doit avoir le statut 400
    Et le corps de la réponse doit contenir un message d'erreur pour le champ "titre"

  Scénario: Échec de la création d'une note sans contenu
    Quand je fais une requête POST à "/notes" avec le titre "Note sans contenu" et un contenu manquant
    Alors la réponse doit avoir le statut 400
    Et le corps de la réponse doit contenir un message d'erreur pour le champ "contenu"
