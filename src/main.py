"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import os

from recommender import load_songs, recommend_songs


def main() -> None:
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(project_root, "data", "songs.csv")
    songs = load_songs(csv_path)
    # Print all loaded songs for verification
    print(f"Loaded {len(songs)} songs")

    # Concrete example taste profile used for comparisons
    user_profiles = [{
            "name": "normal_pop_happy",
            "favorite_genre": "pop",
            "favorite_mood": "happy",
            "target_energy": 0.7,
            "target_acousticness": 0.3,
        },
        {
            "name": "conflicting_mood_energy",
            "favorite_genre": "pop",
            "favorite_mood": "sad",
            "target_energy": 0.9,
            "target_acousticness": 0.1,
        },
        {
            "name": "extreme_boundary",
            "favorite_genre": "rock",
            "favorite_mood": "angry",
            "target_energy": 1.0,
            "target_acousticness": 0.0,
        },
        {
            "name": "no_clear_match",
            "favorite_genre": "classical",
            "favorite_mood": "upbeat",
            "target_energy": 0.2,
            "target_acousticness": 0.8,
        },
        {
            "name": "tie_trap",
            "favorite_genre": "hiphop",
            "favorite_mood": "chill",
            "target_energy": 0.5,
            "target_acousticness": 0.5,
        },
    ]

    for user_prefs in user_profiles:            
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nUser preference: {user_prefs['name']}")
        print(f"  Genre: {user_prefs['favorite_genre']}")
        print(f"  Mood: {user_prefs['favorite_mood']}")
        print(f"  Target energy: {user_prefs['target_energy']}")
        print(f"  Target acousticness: {user_prefs['target_acousticness']}")
        print("\nTop recommendations:\n")
        for rank, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{rank}. {song['title']} by {song['artist']} (Score: {score:.2f})")
            for reason in explanation.split("\n"):
                print(f"   • {reason}")
            print()
        print("-" * 40)

    adversarial_profiles = [
    ]

    for user_prefs in adversarial_profiles:            
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print("\nUser preference:")
        print(f"  Genre: {user_prefs['favorite_genre']}")
        print(f"  Mood: {user_prefs['favorite_mood']}")
        print(f"  Target energy: {user_prefs['target_energy']}")
        print(f"  Target acousticness: {user_prefs['target_acousticness']}")
        print("\nTop recommendations:\n")
        for rank, rec in enumerate(recommendations, start=1):
            song, score, explanation = rec
            print(f"{rank}. {song['title']} by {song['artist']} (Score: {score:.2f})")
            for reason in explanation.split("\n"):
                print(f"   • {reason}")
            print()
        print("-" * 40)

if __name__ == "__main__":
    main()
