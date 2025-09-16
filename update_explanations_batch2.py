import json

# Load the trivia questions from the JSON file
with open('anime_trivia.json', 'r') as f:
    questions = json.load(f)

# Define the new explanations for the second batch
new_explanations = {
    4: "The book Seto Kaiba is reading is 'Thus Spoke Zarathustra' by Friedrich Nietzsche. This is a deliberate character detail, as the book's themes of the 'Übermensch' (Overman), the will to power, and the rejection of traditional morality perfectly reflect Kaiba's arrogant, individualistic personality and his relentless drive to become the world's greatest duelist.",
    5: "Kinema Citrus is an animation studio founded in 2008 by former members of Production I.G and Bones. Besides the critically acclaimed 'Made in Abyss', the studio is also known for producing other popular anime series such as 'The Rising of the Shield Hero', 'Barakamon', and 'Tokyo Magnitude 8.0'.",
    6: "In the 9th Pokémon movie, 'Pokémon Ranger and the Temple of the Sea', the mythical Pokémon Manaphy is known as the 'Prince of the Sea'. The plot revolves around Ash and his friends protecting the Manaphy egg from the pirate Phantom, who seeks to use Manaphy to find the legendary Sea Crown and the hidden Sea Temple of Samiya.",
    7: "True. Gosho Aoyama is the celebrated manga artist who created 'Detective Conan' (also known as 'Case Closed'). His other major works include the samurai-themed adventure 'Yaiba' and the phantom thief series 'Magic Kaito', whose protagonist, Kaito Kid, frequently appears in 'Detective Conan'.",
    8: "Giorno Giovanna is the protagonist of 'Golden Wind', the fifth part of JoJo's Bizarre Adventure. He is the illegitimate son of the series' main antagonist, DIO, who had stolen the body of Jonathan Joestar. This unique parentage makes Giorno a member of the Joestar bloodline and a 'JoJo'. His dream is to become a 'Gang-Star' and reform the Italian mafia from within.",
    9: "Egoist is a Japanese pop duo that was formed specifically to produce theme music for the 2011 anime series 'Guilty Crown'. The group consists of composer Ryo of Supercell and vocalist Chelly. In the world of the anime, Egoist is a popular band fronted by the main heroine, Inori Yuzuriha.",
    10: "The original 'To Love-Ru' manga, written by Saki Hasemi and illustrated by Kentaro Yabuki, was serialized in Shueisha's Weekly Shōnen Jump magazine from April 24, 2006, to August 31, 2009. The series was followed by a sequel, 'To Love-Ru Darkness', which ran from 2010 to 2017.",
    11: "The main characters in 'Inuyasha' are searching for the scattered shards of the Shikon no Tama, or the Jewel of Four Souls. This powerful, magical jewel, born from the battle between a priestess and demons, can grant immense power to whoever possesses it. The quest to reassemble the jewel and prevent it from falling into the hands of the evil demon Naraku drives the plot of the series.",
    12: "False. The main protagonist of Kill La Kill, Ryuko Matoi, wields a giant, single-bladed red scissor blade. It is one half of a pair of 'Rending Scissors' designed to cut Life Fibers, the sentient threads that make up the superpowered Goku Uniforms in the series.",
    13: "'Bishoujo Senshi Sailor Moon' first aired on TV Asahi in Japan on March 7, 1992. The series became a global phenomenon, credited with revitalizing and popularizing the 'magical girl' genre of anime and manga worldwide.",
    14: "Kaname Chidori is the main heroine of 'Full Metal Panic!'. She is a high school student who is also one of the 'Whispered,' a select group of individuals who possess innate, advanced scientific and technological knowledge. This makes her a target for various organizations, and the series' protagonist, the young soldier Sousuke Sagara, is tasked with protecting her.",
    15: "'Akira' originated as a manga series written and illustrated by Katsuhiro Otomo. It was serialized from 1982 to 1990. The iconic 1988 anime film of the same name, also directed by Otomo, is an adaptation of the manga, though it only covers the first half of the manga's story.",
    16: "There are three known Trans-weapons in the 'To Love-Ru' series. These are living weapons with incredible transformation abilities. The first is Golden Darkness (Yami), the second is her 'sister' Mea Kurosaki, and the third is the master of the 'Darkness' ability, Nemesis.",
    17: "'Clannad' was originally a visual novel developed by the company Key, released in 2004. It was later adapted into a highly acclaimed anime series by Kyoto Animation, as well as a manga and a film.",
    18: "In 2013, the virtual pop star Hatsune Miku was featured in a major advertising campaign with Domino's Pizza in Japan. The collaboration included special pizza boxes with Miku's image, a Miku-themed pizza delivery scooter, and a mobile app that allowed users to take pictures with an augmented reality version of Miku.",
    19: "In 'Highschool DxD', Koneko Toujou is a Nekomata, a type of cat-like yōkai from Japanese folklore. Nekomata are said to be cats that have lived long enough to develop supernatural powers, including shapeshifting into human form and commanding the spirits of the dead.",
    20: "The main character of 'One Piece' is Monkey D. Luffy, a young man who gains the properties of rubber after unintentionally eating a Devil Fruit. His lifelong dream is to become the Pirate King by finding the legendary treasure left behind by the late Pirate King, Gol D. Roger."
}

# Update the explanations for the questions in the batch
for question in questions:
    if question['id'] in new_explanations:
        question['explanation'] = new_explanations[question['id']]

# Write the updated data back to the JSON file
with open('anime_trivia.json', 'w') as f:
    json.dump(questions, f, indent=4)

print("Explanations for batch 2 updated successfully.")
