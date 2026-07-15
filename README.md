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

* Each feature is assigned a point score. Points are defined as follows based on how we want this system to balance preference signals.
   - Genre = 2.0 points
   - Mood = 1.25 points
   - Energy similarity = 1.0 point
   - Acousticness similarity = 0.75 points

This means genre remains the strongest signal, mood is still important, and energy/acousticness act as continuous similarity boosters.

* Numerical values like energy and acousticness are converted to a similarity score. For example, if the user target energy is `t` and the song energy is `x`:
  - `distance = abs(x - t)`
  - `s_energy = max(0.0, 1.0 - distance)`
  - `s_acoustic = max(0.0, 1.0 - abs(x_acousticness - t_acousticness))`

* Category features like mood and genre are assigned score of 0 or 1 based on user preference. For example, if the user profile has `genre=pop` and the song genre is `pop`, then `s_genre=1`; otherwise `s_genre=0`.


_score = 2.0 * s_genre + 1.25 * s_mood + 1.0 * s_energy + 0.75 * s_acoustic_

where:
- `s_genre` = genre score, 0 or 1
- `s_mood` = mood score, 0 or 1
- `s_energy` = energy similarity score, between 0 and 1
- `s_acoustic` = acousticness similarity score, between 0 and 1

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
* It does take a genre-first approach and prioritizes that. It gives some weight to mood though.
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
(.venv) priyankashah@Priyankas-MacBook-Air src % python3 -m main
Loaded 22 songs

User preference:
  Genre: pop
  Mood: happy
  Target energy: 0.7
  Target acousticness: 0.3

Top recommendations:

1. Sunrise City by Neon Echo (Score: 4.79)
   • genre: pop, match = +2.0
   • mood: happy, match = +1.25
   • energy: 0.82, similarity = +0.88
   • acousticness: 0.18, similarity = +0.66

2. Gym Hero by Max Pulse (Score: 3.33)
   • genre: pop, match = +2.0
   • mood: intense, match = 0
   • energy: 0.93, similarity = +0.77
   • acousticness: 0.05, similarity = +0.56

3. Iron Sky by Crimson Ash (Score: 3.30)
   • genre: pop, match = +2.0
   • mood: defiant, match = 0
   • energy: 0.95, similarity = +0.75
   • acousticness: 0.04, similarity = +0.55

4. Golden Meadow by Harbor Light (Score: 3.22)
   • genre: pop, match = +2.0
   • mood: hopeful, match = 0
   • energy: 0.58, similarity = +0.88
   • acousticness: 0.84, similarity = +0.34

5. Rooftop Lights by Indigo Parade (Score: 2.90)
   • genre: indie pop, match = 0
   • mood: happy, match = +1.25
   • energy: 0.76, similarity = +0.94
   • acousticness: 0.35, similarity = +0.71

(.venv) priyankashah@Priyankas-MacBook-Air src % 
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



