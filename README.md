# 🎵 Music Recommender Simulation

## Project Summary

Given a list of songs with features, this app recommends list of songs to the user, ordered by a score based on user preferences, song features like genre, mood, etc.

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

The music recommendation system uses user profile data and song features to recommend songs to the user in ranked order. Basically,
- it __scores__ each song individually, and
- it __ranks__ the order of the items once all scores are assigned.

The simulation uses two main data objects:

- Song: a song record with these features:
  - id
  - title
  - artist
  - genre
  - mood
  - energy
  - tempo_bpm
  - valence
  - danceability
  - acousticness

- UserProfile: a user taste profile with these attributes:
  - favorite_genre
  - favorite_mood
  - target_energy
  - likes_acoustic

For recommendation scoring, the system mainly uses genre, mood, energy, and acousticness. The other fields are stored for completeness or for future extensions.

### Scoring rules

For scoring each song, it uses a combination of song features and user taste preference. 
* Primary features used - genre, mood, energy, acousticness
* Secondary features not used in this release but useful for next version - valence, danceability, tempo_bpm.
* Features not used for recommendation - id, title, artist as they do not directly indicate similarity from user standpoint. 

* Each feature is assigned a weighted score. Weights are defined as follows based on how we perceive user would like this.
   - Genre 40%
   - Mood 25%
   - Energy 20%
   - Acoustic 15%

This is because genre and mood are the strongest signals of taste. Energy is also important, acousticness is useful but slightly less important.

* Numerical values like energy and acousticness are converted to a similarity score. eg. User energy level preference=t, song energy level=x. 
Distance /difference d = x-t
Similarity s = 1-d 
i.e. s_energy = 1−∣x−t∣

* Category features like mood and genre are assigned score of 0 or 1 based on user preference. eg. if user profile has genre=pop and song genre=pop, s_genre=1. If song genre = hiphop, s_genre = 0.


_score = 0.40 * s_ genre + 0.25 * s_mood + 0.20 * s_energy +0.15 * s_acoustic_
​
s_genre = genre score, 0 or 1
s_mood = mood score, 0 or 1
s_energy = energy score, between 0-1
s_acoustic = acousticness score, between 0-1

where 0.4 is the weight for genre, 0.25 for mood...

### Ranking
After all songs are scored, the system:
- sorts them in descending order
- returns top k songs.

### Difference from real world systems
Real world systems uses richer data and prioritze for business goals and user behaviour signal.
* Collaborative filtering - they get data from multiple users and provide recommendation on what users with similar preferences have liked.
* Contextual data - systems use time of the day (bedtime v/s afternoon), user action (eg. if user is exercising) to change recommnedations.
* User behaviour signals - real world systems get feedback from user in terms of skips, likes, follows, etc. and update recommendation accordingly.

### What this version prioritizes
* Feature similarity - it prioritizes songs that are similar to the ones user has a taste preference for.
* Predictabile experience - since features are static and not dynamic (like acitivty or other user actions), the system will not recommend very different songs. 

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



