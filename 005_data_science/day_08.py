import pandas as pd 

data = [
  {
    "title": "The Silent Forest",
    "author": "Jane Hill",
    "genre": "Mystery",
    "description": "A detective uncovers secrets hidden deep in the woods while chasing a serial killer."
  },
  {
    "title": "Whispers of the Ocean",
    "author": "Liam Carter",
    "genre": "Romance",
    "description": "Two strangers meet on a remote island and discover love amidst crashing waves and forgotten dreams."
  },
  {
    "title": "Digital Shadows",
    "author": "Ava Thompson",
    "genre": "Thriller",
    "description": "A hacker gets entangled in a government conspiracy after uncovering a classified digital footprint."
  },
  {
    "title": "Echoes of Time",
    "author": "Daniel Reyes",
    "genre": "Science Fiction",
    "description": "A scientist accidentally opens a rift in time and must race to prevent the collapse of reality."
  },
  {
    "title": "The Last Heir",
    "author": "Sophie Bennett",
    "genre": "Historical Fiction",
    "description": "In the aftermath of a royal betrayal, a young noblewoman must reclaim her family’s honor and legacy."
  },
  {
    "title": "Beneath the Crimson Sky",
    "author": "Oliver Grant",
    "genre": "Adventure",
    "description": "An explorer journeys through uncharted lands searching for a lost civilization buried under red sands."
  },
  {
    "title": "The Art of Disappearing",
    "author": "Clara Nguyen",
    "genre": "Psychological Fiction",
    "description": "A woman slowly erases herself from her own life, leaving behind only cryptic journal entries."
  },
  {
    "title": "Neon City Nights",
    "author": "Marcus Cole",
    "genre": "Cyberpunk",
    "description": "In a future ruled by corporations, a street detective unravels the truth about a city built on lies."
  },
  {
    "title": "Garden of Secrets",
    "author": "Elena Brooks",
    "genre": "Drama",
    "description": "A family estate hides more than just memories when buried letters reveal decades of deception."
  },
  {
    "title": "When Stars Collide",
    "author": "Noah Patel",
    "genre": "Young Adult",
    "description": "Two teens from different worlds find their destinies intertwined under the endless summer sky."
  }
]

df = pd.DataFrame(data)
df.to_csv("books.csv", index=False)
print("✅ Book dataset created")
