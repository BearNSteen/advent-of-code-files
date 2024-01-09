import random

verses = [
   ["Ancient city, high in the sky, ",
    "Machu Picchu, where legends fly. ",
    "Stone and cloud, a mystic maze, ",
    "Echoes whisper of bygone days. "],

   ["Sunlight dances on weathered walls, ",
    "Whispering secrets of ancient falls. ",
    "Spirits roam where time stands still, ",
    "In this sacred place, dreams fulfill. "],

   ["Windswept ruins, whispering tales, ",
    "Of emperors and forgotten trails. ",
    "Mysteries unfold beneath starry skies, ",
    "In Machu Picchu's timeless eyes. "]
]

choruses = [
   ["Doo-ba-doo, ba-da-da-da-da, ", 
    "Machu Picchu, where spirits play. ", 
    "Shoo-bee-doo, ba-la-la-la-la, ", 
    "Ancient city, seize the day! "],

   ["Ski-ba-dee, ba-da-ba-ba-da, ",
    "Machu Picchu, where dreams take flight. ", 
    "La-la-loo, ba-da-da-da-da, ", 
    "Dancing shadows, bathed in moonlight. "],

   ["Boop-boop-bee-doo, ba-da-la-la-la, ",
    "Machu Picchu, secrets unfold. ", 
    "Shoo-bee-doo-wah, ba-da-ba-ba-da, ", 
    "Stories whispered, centuries old. "]
]

def generate_song():
   """Generates a random jazz song about Machu Picchu."""

   random.shuffle(verses)
   random.shuffle(choruses)

   print("\n".join(verses[0]))  # Print first verse
   print("\n".join(choruses[0])) # Print chorus
   print("\n".join(verses[1]))  # Print second verse
   print("\n".join(choruses[0])) # Print chorus again
   print("\n".join(verses[2]))  # Print third verse
   print(
       "\n".join(["MACHU PICCHU! Wait, where is that?"])
   )  # Print ending line

if __name__ == "__main__":
   generate_song()