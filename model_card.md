# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
**BeatDrop 1.0**  

---

## 2. Intended Use  

The app recommends songs from a small catalog based on a user’s favorite genre, mood, energy level, and acoustic preference. It assumes the user has one main genre, one mood, and a target energy/acousticness score. This is for classroom exploration, not for real users.

---

## 3. How the Model Works  

- Song features used: genre, mood, energy, and acousticness. 
- User preferences considered: favorite genre, favorite mood, target energy, and target acousticness.
- How it turns into a score: Each song is compared to the user's preferences on all four features, and each match earns points:
    - Genre match → exact match, +1.0 point
    - Mood match → exact match, +1.25 points
    - Energy  closeness → the closer the song's energy is to the target, the more points, up to +2.0
    - Acousticness closeness → same as energy, up to +0.75 points

All four are added together for a total score, songs are sorted highest to lowest, and the top k are recommended.

- Changes from the starter logic: The starter had genre weighted highest (2.0) with energy as a smaller booster (1.0). Now that is flipped — energy is now the strongest signal (2.0) and genre counts half as much (1.0) — so the system now favors songs that feel right energy-wise over songs that just share a genre label.

---

## 4. Data  

The catalog has 22 songs across 9 genres (mostly pop and lofi) and 17 different moods, most appearing only once. I added few songs to make it more diverse.

It's missing broader coverage of genres like hiphop, classical, and metal — so niche tastes outside pop/lofi get thin results. It's also missing features like  lyrics/language info, and more representation of different moods.

---

## 5. Strengths  

1. The system works well for users whose genre, mood, and energy/acousticness preferences all point in the same direction — e.g. the "pop + happy + energy 0.7" profile correctly surfaces Sunrise City as the top pick, since it matches on genre, mood, and is close on energy/acousticness too.

2. It also correctly captures "close but not exact" energy/acousticness taste — e.g. for the extreme high-energy rock profile, Storm Runner (energy 0.91) outranks lower-energy songs even without a mood match, which matches intuition that a near-perfect energy fit should count for a lot.

3. And when genre is the clearest signal (e.g. rock fans), it reliably keeps genre-matching songs at the top of the list ahead of same-energy songs from other genres — matching the intuition that genre should still meaningfully anchor the ranking.

---

## 6. Limitations and Bias 

1. Genre imbalance in catalog.
Certain genres have more songs/representation in the catalog than others. For eg. lofi has 5 songs and pop has 4. house, folk, synthwave have one song each. So a user who loves synthwave will only get one genre-matching candidate, whereas a user who loves pop gets 4 candidates. 

2. Mood underrepresented in catalog, no semantics.
There are 17 moods across 22 songs, which means each mood gets represented just about once. So mood-matchi can only ever boost one song for most users. 
Also, there is no semantic match for mood, which means happy<>upbeat score identically to happy<>angry. In real world, happy<>upbeat should score higher.

3. Exact string match for genre and mood.
Genre and mood require exact string and case-sensitive match. So Pop and pop, or hiphop and hip-hop will not match, leading to incorrect scoring.

4. Energy gap.
The energy gap formula causes disadvantage for users with extreme taste. Catalog has energy range from (0.28-0.95). So user with target energy=0 or 1 will never get a really good or perfect match.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

- Which user profiles you tested  
Tested the following user profiles.
    * Normal user - tests a user who loves pop, happy songs. Sunrise city and Gym Hero rank topmost since they match the genre and mood.
    * Conflicting mood/energy - tests whether a sad song with very high energy can still rank oddly well. Prefers songs with high energy like Iron Sky and Gym Hero.
    * Extreme boundary - checks how the scoring behaves at the edges of the energy/acoustic range. Other than genre match, Iron Sky and Gym Hero show up since their energy is high.
    * No clear match - tests what happens when the profile is unlikely to be satisfied by any song. Since mood and genre don't match, songs with similar energy and acoustiness show up, like Spacewalk Thoughts or Moonlit Sonata.
    * Tie - Energy 0.5 and acousticness 0.5, tests whether multiple songs end up with nearly identical scores. Outside of mood match, Midnight Drift/Sunset breeze show up since their energy and acoustiness are close to 0.5.
 
- What you looked for in the recommendations
I looked for why a particular song showed up in recommendations and how it was scored. Also looked for whether songs from a different genre or mood showed up (to make the list more )
- What surprised you  
One Pop song (Sunrise city or Gym Hero) appeared in almost every user profile recommendation.

- Any simple tests or comparisons you ran  
No need for numeric metrics unless you created some.

Yes, tested by changing weights. Reduced the weightage for pop songs and increased for energy, then verified that more variety showed up in recommendations for profiles with genre classical and hiphop.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

* Add more features to the scoring metric. For example, currently we have not considered valence, tempo, danceability. 
* Increase input song list and make it more diverse. 
* Incorporate some rules in recommender to choose say only 2 songs from each genre, or each mood to add variety to the top k results. 
* Support multiple genres or mood in user preferences instead of just 1.
* Include user feedback around like, skip, repeat.
* Allow users to customize weightage of each feature.
* Provide option for multiple recommendations (like multiple playlists) based on different ranking algorithms eg. surprise playlist v/s mood based playlist.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
