import re

from src.recommender import Song, UserProfile, Recommender


def _energy_points(explanation: str) -> float:
    match = re.search(r"Energy .* \(\+([\d.]+) pts\)", explanation)
    assert match, f"could not find energy points in explanation: {explanation!r}"
    return float(match.group(1))


def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        target_acousticness=0.2,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        target_acousticness=0.2,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""
    # song[0] is pop/happy, matching the user's favorite_genre and favorite_mood
    assert "Genre match" in explanation
    assert "Mood match" in explanation
    # song[0] energy (0.8) equals the user's target_energy (0.8), so points should be high
    assert _energy_points(explanation) > 1.5


    song = rec.songs[1]
    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""
    # song[1] is lofi/chill, mismatching the user's favorite_genre and favorite_mood
    assert "Genre mismatch" in explanation
    assert "Mood mismatch" in explanation
    # song[1] energy (0.4) is far from the user's target_energy (0.8), so points should be low
    assert _energy_points(explanation) < 1.5


