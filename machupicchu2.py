
import random

verses = [
    ["Machu Picchu, high in the clouds, ", 
     "Ancient city, mysteries it shrouds.", 
     "Inca stones, whispering tales, ",
     "Echoes of time, on mountain trails."],
    ["Stone walls reaching, to touch the sun, ",
     "Terraces green, where waters run.",
     "Among the peaks, a sacred place, ",
     "Machu Picchu, full of grace."],
    ["Andean winds, carry a song, ",
     "Whispers of the past, all day long.",
     "Llamas roaming, condors high, ",
     "Machu Picchu, against the sky."]
]

choruses = [
    ["Zippity, zoppity, zeeba dee doo, ", 
     "Machu Picchu, I'm coming for you!", 
     "Beeba dee bop, a zwee zwee zee, ",
     "Scatting in the Andes, wild and free!"]
] 

def generate_jazz_song():
    """Generates a random jazz song about Machu Picchu."""

    random.shuffle(verses)
    print("\n".join(verses[0]))
    print("\n".join(choruses[0]))
    print("\n".join(verses[1]))
    print("\n".join(choruses[0]))
    print("\n".join(verses[2]))
    print("\n".join(choruses[0]))
    print("MACHU PICCHU! Wait, where is that?")

def analyze_song(song_lyrics):
    """Analyzes the song lyrics and counts lines with scatting."""
    scat_count = 0
    scat_words = ["zippity", "zoppity", "zeeba", "dee", "doo", "beeba", "bop", "zwee"]

    for line in song_lyrics.split("\n"):
        words = line.lower().split()
        if any(scat_word in words for scat_word in scat_words):
            scat_count += 1

    return scat_count

if __name__ == "__main__":
    song = generate_jazz_song()  # Generate the song first
    scat_lines = analyze_song(song)
    print(f"\nThe song has {scat_lines} lines with scatting.")