import random

verses = [
    ["Brushin' my teeth, every day and night, ", 
     "Keep 'em pearly, shiny, and bright. ", 
     "Flossin' too, it's the way to go, ",
     "Healthy gums, best smile I know! "],

    ["Molars, incisors, and canines too, ",
     "Each with a job, important to do. ",
     "Chew and smile, they're my pearly crew, ", 
     "Gonna keep 'em healthy, it's true! "],

    ["Sugar, beware, you're my teeth's worst foe, ",
     "Cavities and decay, oh no! ",
     "But with good habits, I'll keep 'em strong, ", 
     "My teeth and I, we'll get along! "]
]

choruses = [
    ["WHOA! Teeth, teeth, strong and white, ", 
     "Keep 'em clean, they'll shine so bright. ", 
     "Brush and floss, let's take a stand, ",
     "For healthy teeth, lend a hand! "],

    ["Teeth, oh teeth, let's give a cheer, ",
     "WHOA! Brush and floss, no need to fear. ", 
     "Smile wide, show 'em off with glee, ",
     "Healthy teeth, the way to be! "],

    ["Healthy teeth, WHOA! what a sight, ",
     "Keep 'em clean, morning, noon, and night. ",
     "A smile so bright, it takes the lead, ",
     "Happy teeth, that's all we need! "]
]

def generate_song():
    """Generates a random song about teeth."""

    random.shuffle(verses)
    random.shuffle(choruses)

    print("\n".join(verses[0]))  # Print a random verse
    print("\n".join(choruses[0])) # Print a random chorus
    print("\n".join(verses[1]))  # Print another random verse
    print("\n".join(choruses[0])) # Print the chorus again

if __name__ == "__main__":
    generate_song()