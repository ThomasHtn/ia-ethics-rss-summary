
# Éthique et Intelligence Artificielle 

## Qu’est-ce que l’éthique de l’IA ?

L’éthique est un ensemble de principes moraux qui nous aident à distinguer le bien du mal. L’éthique de l’IA est un domaine pluridisciplinaire qui étudie comment optimiser l’impact bénéfique de l’intelligence artificielle (IA) tout en réduisant ses risques et ses effets indésirables.

## Les principes de l’éthique IA

**Respect des personnes :** ce principe reconnaît l’autonomie des individus et permet aux chercheurs de protéger les personnes dont l’autonomie est réduite, ce qui peut être dû à diverses circonstances telles que la maladie, un handicap mental, des restrictions d’âge. Ce principe touche principalement l’idée de consentement. Les personnes doivent être conscientes des risques et des avantages potentiels de toute expérience à laquelle elles participent, et elles doivent pouvoir choisir de participer ou de s’en retirer à tout moment avant et pendant l’expérience.

**Bienveillance :** ce principe sort du cadre de l’éthique des soins de santé, où les médecins prêtent serment de « ne pas nuire ». Cette idée peut être facilement appliquée à l’intelligence artificielle, où les algorithmes peuvent amplifier les préjugés liés à la race, au genre, aux opinions politiques, etc., malgré l’intention de faire le bien et d’améliorer un système donné.

**Justice :** ce principe traite de questions telles que l’équité et l’égalité. Qui doit profiter des avantages de l’expérimentation et du machine learning ? Le rapport Belmont propose cinq façons de répartir les charges et les avantages :
  - Partage équitable
  - Besoin individuel
  - Effort individuel
  - Contribution sociétale
  - Mérite

[Source](https://www.ibm.com/fr-fr/think/topics/ai-ethics)

## ✅ Bonnes pratiques éthiques

- **Respecter les droits fondamentaux et la vie privée**  
  Ne collectez que les données nécessaires, informez clairement les utilisateurs et obtenez leur consentement.
  [Source](https://www.lumenova.ai/blog/perspectives-on-ai-governance-dos-and-donts)

- **Assurer l’équité et éviter les biais**  
  Vérifiez que les données d’entraînement sont diversifiées. Mettez en place des mécanismes pour détecter et corriger les discriminations.
    [Source](https://www.pmi.org/blog/top-10-ethical-considerations-for-ai-projects)

- **Garantir la transparence et l’explicabilité**  
  Expliquez aux utilisateurs comment l’IA arrive à ses décisions. Intégrer des outils d’« Explainable AI » pour surmonter l’effet de boîte noire.
      [Source](https://www.pmi.org/blog/top-10-ethical-considerations-for-ai-projects)

- **Maintenir l’humain dans la boucle**  
  Privilégiez le jugement humain, surtout pour les décisions à forts enjeux (santé, justice, emploi…).
  [Source](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics)
  

- **Assurer sécurité, robustesse et durabilité**  
  Protégez les systèmes contre les attaques et minimisez leur impact environnemental.

- **Établir responsabilité et gouvernance**  
  Documentez et auditez les systèmes d’IA, définissez qui est responsable en cas de problème.
    [Source](https://www.unesco.org/en/artificial-intelligence/recommendation-ethics)

- **Favoriser la collaboration et consultation**  
  Impliquez parties prenantes, experts et utilisateurs dès la conception, adoptez une approche multidisciplinaire.
  [Source](https://en.wikipedia.org/wiki/Joy_Buolamwini)
  

- **Concevoir centré sur les valeurs humaines**  
  Utilisez des méthodes comme le *Value Sensitive Design* pour intégrer les valeurs morales dès le départ.
    [Source](https://en.wikipedia.org/wiki/Value_sensitive_design)

## 🚫 À éviter (Don’ts)

- **Ne pas se reposer aveuglément sur l’IA**  
  L’automatisation complète sans supervision humaine peut conduire à des erreurs graves.
  [Source](https://www.instituteofaistudies.com/insights/ai-ethics-the-dos-and-donts-of-ai)

- **Ne pas ignorer les biais des données**  
  Se passer de contrôle ou d’audit introduit des biais non détectés.

- **Ne pas violer la vie privée**  
  Évitez les collectes excessives sans raison ni consentement.

- **Ne pas sacrifier la sécurité**  
  Compromettre la sécurité pour l’innovation expose à des risques éthiques et légaux.

- **Ne pas se contenter d’une gouvernance à cocher**  
  Un cadre rigide ou trop bureaucratique empêche l’innovation et ne s’adapte pas.

- **Ne pas donner trop de pouvoir à l’IA**  
  Ne laissez jamais l’IA prendre des décisions affectant directement les droits ou la vie des personnes.

- **Ne pas négliger l’impact environnemental**  
  Les modèles IA gourmands en énergie doivent être optimisés ou compensés.
    [Source](https://unsceb.org/sites/default/files/2022-09/Principles%20for%20the%20Ethical%20Use%20of%20AI%20in%20the%20UN%20System_1.pdf)

## 🎨 En design (UX, design créatif…)

- **Déclarer l’usage de l’IA**  
  Soyez transparent, mentionnez quand un visuel ou un texte est généré.

- **Ne pas remplacer la recherche utilisateur**  
  L’IA ne doit pas se substituer aux méthodes qualitatives (entretiens, observations).

- **Privilégier une IA comme assistant**  
  L’IA génère des propositions, le designer les critique, les filtre et les enrichit.

- **Cultiver la diversité et l’inclusion**  
  Intégrez des perspectives plurielles pour éviter biais et stéréotypes visuels.


## 📚 Pour aller plus loin

- **UNESCO** : recommandations centrées sur les droits humains  
- **Toptal** : équité, transparence et responsabilité en design  
- **IA ACT** : [La loi européenne sur l'intelligence artificielle](https://artificialintelligenceact.eu/fr/)

# Types de Modèles en Intelligence Artificielle

## 1. Classification

La classification est une tâche supervisée où le modèle apprend à attribuer une étiquette ou une classe à chaque observation en fonction de ses caractéristiques.  
Elle est utilisée lorsque la variable cible est **catégorielle** (ex : "chat" ou "chien", "spam" ou "non-spam").

**Exemples :**
- Reconnaissance d’images (chien, chat, voiture, etc.)
- Détection de spam dans les e-mails
- Diagnostic médical (malade / sain)

---

## 2. Régression

La régression est une tâche supervisée où le modèle prédit une **valeur numérique continue** à partir des caractéristiques d’entrée.  
Elle est utilisée lorsque la variable cible est **quantitative** (ex : prix, température, poids).

**Exemples :**
- Prédiction du prix de l’immobilier
- Prévision de la demande énergétique
- Estimation de la consommation d’essence

---

## 3. Clustering (Regroupement)

Le clustering est une tâche **non supervisée** qui consiste à regrouper automatiquement les données en **clusters** (groupes) selon leur similarité.  
Le modèle ne connaît pas les étiquettes à l’avance, il découvre des structures naturelles dans les données.

**Exemples :**
- Segmentation de clients selon leur comportement
- Regroupement de documents similaires
- Détection d’anomalies

# Quel modèle chosir pour notre besoin  ?

## Objectif
Pour rappel, notre objectif est d'identifier automatiquement, parmi des articles RSS, ceux qui correspondent à la thématique  "éthique de l'IA". On aura donc une notion "binaire" -> l'article est-il pertinent ? oui / non

## Classification supervisée (texte)
D'après notre objectif et les définitions citées précédemment, le modèle optimal pour ce projet semble être la **Classification supervisée**. En effet, le but ici, va être d'attribuer une étiquette à nos articles
- **Classe 1 :** articles pertinents sur l'éthique de l’IA
- **Classe 0 :** articles non pertinents

Nous avons donc pas besoin de prédire une valeur numérique. On oublie le modèle de **Régression**. Et nous n'avons pas besoin de regrouper les articles par thème car ils sont déjà filtrer par thématique en amont. On peut donc éliminer le **Clustering**.

## Enregistrement des articles
Afin d'entrainer notre futur modèle, nous allons avoir besoin d'enregistrer tous nos articles dans une base de données.

| id   | source                | title      | Body
| ---  | --------------------- | ---------- | -------------------------
| 1    | http://mon-article.fr | Mon titre  | Le contenue de mon article

Pour cela, il est possible de passer par une libraire [feedparser](https://pypi.org/project/feedparser/)

exemple de code : 
```python
# Lecture du flux RSS
rss_url = "https://example.com/rss"  # Remplace par l'URL de ton flux RSS
feed = feedparser.parse(rss_url)

# Lecture des articles pour récupérer la data à ajouter dans notre table
for entry in feed.entries:
    title = entry.get("title", "")
    content = entry.get("summary", "")  # parfois "content[0].value"
    url = entry.get("link", "")
    published_at = entry.get("published", "")
    source = feed.feed.get("title", "Unknown Source")  # titre du flux RSS
```
## Nettoyage des données
Afin d'entrainer au mieux notre futur modèle, nous aurons besoin de filtrer et de nettoyer nos données.

- Supprimer les articles qui n'ont pas de contenu
- Supprimer les doublons
- Supprime les articles très courts (len(content) < 100 caractères)
- Uniquement en français 🤔 ?
- Supprimer le html dans le contenue
- Supprimer les liens dans le contenue
- Conserver uniquement les lettres et les espaces dans le contenue

**Résultat :**

| titre               | contenu nettoyé          | pertinent |
| ------------------- | ------------------------ | --------- |
| L’éthique de l’IA   | ethique intelligence ... | 1         |
| Nouveaux GPU Nvidia | nouveau gpu nvidia ...   | 0         |


## Comment mesurer la pertinence d'un article

**1. Recherche par mots clés** 
L'idée est de constuire une liste de mots-clés (ex : "IA responsable", "biais algorithmiques", "transparence", etc.) et marquer l'article comme pertient si celui-ci contient ces mots dans le titre, le résumé ou le corps

**2. Utiliser un modèle pré-entraîné pour comparer notre modèle**
Il existe des modèles comme **facebook/bart-large-mnli** pour estimer directement la pertinence sans entraînement préalable. Il serait alors possible de comparer les performances de notre modèle.