import csv
from operator import itemgetter
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass, asdict

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Returns the top k songs recommended for the given user."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Returns a human-readable explanation for why a song was recommended."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Loads songs from a CSV file and returns them as a list of dicts."""
    #print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                song = Song(
                    id=int(row["id"]),
                    title=row["title"],
                    artist=row["artist"],
                    genre=row["genre"],
                    mood=row["mood"],
                    energy=float(row["energy"]),
                    tempo_bpm=float(row["tempo_bpm"]),
                    valence=float(row["valence"]),
                    danceability=float(row["danceability"]),
                    acousticness=float(row["acousticness"]),
                )
            except (KeyError, ValueError) as e:
                print(f"Error reading row {row}: {e}")
                continue
            songs.append(asdict(song))
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Scores a single song against user preferences and returns (score, reasons)."""
    GENRE_WEIGHT = 1.0
    MOOD_WEIGHT = 1.25
    ENERGY_WEIGHT = 2.0
    ACOUSTIC_WEIGHT = 0.75

    reasons = []
    score = 0.0

    # Genre is a binary match: 1 if equal to the user's favorite, else 0
    s_genre = 1 if song["genre"] == user_prefs["favorite_genre"] else 0
    genre_points = GENRE_WEIGHT if s_genre else 0
    reasons.append(f"genre: {song['genre']}, match = +{genre_points}" if s_genre
                   else f"genre: {song['genre']}, match = 0")
    score += GENRE_WEIGHT * s_genre

    # Mood is a binary match: 1 if equal to the user's favorite, else 0
    s_mood = 1 if song["mood"] == user_prefs["favorite_mood"] else 0
    mood_points = MOOD_WEIGHT if s_mood else 0
    reasons.append(f"mood: {song['mood']}, match = +{mood_points}" if s_mood
                   else f"mood: {song['mood']}, match = 0")
    score += MOOD_WEIGHT * s_mood

    # Energy similarity shrinks toward 0 the further the song is from the target energy
    energy_distance = abs(song["energy"] - user_prefs["target_energy"])
    s_energy = max(0.0, 1.0 - energy_distance)
    energy_points = round(ENERGY_WEIGHT * s_energy, 2)
    reasons.append(f"energy: {song['energy']}, similarity = +{energy_points}")
    score += energy_points

    # Acousticness similarity shrinks toward 0 the further the song is from the target acousticness
    acoustic_distance = abs(song["acousticness"] - user_prefs["target_acousticness"])
    s_acoustic = max(0.0, 1.0 - acoustic_distance)
    acoustic_points = round(ACOUSTIC_WEIGHT * s_acoustic, 2)
    reasons.append(f"acousticness: {song['acousticness']}, similarity = +{acoustic_points}")
    score += acoustic_points

    return round(score, 2), reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Scores, ranks, and returns the top k songs for the given user preferences."""
    results = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = "\n".join(reasons)
        results.append((song, score, explanation))

    results_sorted = sorted(results, key=itemgetter(1), reverse=True)

    return results_sorted[:k]
