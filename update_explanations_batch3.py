import json

# Load the trivia questions from the JSON file
with open('anime_trivia.json', 'r') as f:
    questions = json.load(f)

# Define the new explanations for the third batch
new_explanations = {
    21: "Satella is the infamous Witch of Envy, one of the seven Witches of Sin in the world of 'Re:Zero'. She is a mysterious and powerful silver-haired half-elf who is responsible for giving the protagonist, Subaru Natsuki, his 'Return by Death' ability. Her striking resemblance to the main heroine, Emilia, is a central mystery of the series.",
    22: "In 'A Certain Scientific Railgun', the 'Level 6 Shift Project' was a secret experiment designed to force an esper to evolve to Level 6, a theoretical level of power. The experiment required Accelerator, the most powerful Level 5 esper, to kill 20,000 clones of the third-ranked Level 5, Mikoto Misaka. The clones, known as the 'Sisters', were created for this purpose. The project was ultimately stopped by the efforts of Mikoto and Touma Kamijou.",
    23: "'Phantom Blood' is the first story arc of the long-running and highly influential manga series 'JoJo's Bizarre Adventure', created by Hirohiko Araki. It was first serialized in Shueisha's Weekly Shōnen Jump magazine from January 1, 1987, to October 26, 1987.",
    24: "Studio Bones is a highly acclaimed animation studio known for its high-quality animation and dynamic action sequences. In addition to 'Soul Eater', Bones has produced many other popular and critically successful anime, including 'Fullmetal Alchemist: Brotherhood', 'My Hero Academia', 'Mob Psycho 100', and 'Eureka Seven'.",
    25: "The main character of the 'Naruto' series is Naruto Uzumaki, a young ninja with a cheerful and boisterous personality. He is known for his signature orange jumpsuit, yellow spiky hair, and his verbal tic, 'dattebayo!' (believe it!). His lifelong dream is to become the Hokage, the leader of his village.",
    26: "The protagonist of 'Land of the Lustrous' is Phosphophyllite, often called Phos. They are the youngest of the gem-like beings known as the Lustrous. Initially, Phos is brittle and considered too weak for combat, so they are assigned the task of creating a natural history encyclopedia. The story follows their journey of self-discovery and transformation.",
    27: "The first episode of the 'Soul Eater' anime, titled 'Resonance of the Soul - Will Soul Eater Become a Death Scythe?', first aired in Japan on April 7, 2008.",
    28: "True. Peke is Lala Satalin Deviluke's robotic companion in 'To Love-Ru'. Peke's primary function is to transform into Lala's various outfits. While Peke has a male voice actor in the anime and is sometimes referred to with male pronouns, the character is officially considered a female robot.",
    29: "In 'JoJo's Bizarre Adventure', many of the superpowered abilities known as 'Stands' are named after famous musicians, bands, and songs. 'Red Hot Chili Pepper' (Part 4), 'Green Day' (Part 5), and 'Survivor' (Part 6) are all Stands in the series. While the character Esidisi from Part 2 is a localization of 'AC/DC', he is a Pillar Man, not a Stand user, and there is no Stand named AC/DC.",
    30: "'Uzumaki' is a classic horror manga written and illustrated by the master of the genre, Junji Ito. Ito is renowned for his unique brand of body horror and cosmic horror. His other most famous works include 'Tomie', a story about a beautiful, immortal girl who drives her admirers to madness, and 'Gyo', a tale of fish controlled by a sentient bacteria.",
    31: "In 'Sailor Moon', Sailor Jupiter's civilian name is Makoto Kino. She is a tall, physically strong, and seemingly tomboyish transfer student who is also a skilled cook and gardener. Her powers as a Sailor Guardian are associated with lightning and plants, reflecting the dual nature of the Roman god Jupiter (king of the gods and god of the sky) and the Japanese name for the planet, Mokusei (木星, 'Wood Star').",
    32: "Rock, the everyman salaryman who gets swept up in the world of pirates and mercenaries in 'Black Lagoon', is known for his distinctive business attire, which he continues to wear even after joining the Lagoon Company. His tie is a dark teal color, a subtle but memorable detail of his character design.",
    33: "Studio Shaft is an animation studio famous for its unique and highly stylized visual aesthetic, often referred to as 'Shaft-isms'. This style includes distinctive head tilts, surreal backgrounds, and abstract imagery. Besides 'Hidamari Sketch', Shaft is responsible for many other critically acclaimed and visually innovative anime, such as the 'Monogatari' series, 'Puella Magi Madoka Magica', and 'Sayonara, Zetsubou-Sensei'.",
    34: "Many characters and Stands in 'JoJo's Bizarre Adventure' are named after musical artists. Josuke Higashikata's Stand, 'Crazy Diamond', is named after a 1975 Pink Floyd song. Jolyne Cujoh's 'Stone Free' is named after a 1966 Jimi Hendrix song. Johnny Joestar's 'Tusk' is named after a 1979 Fleetwood Mac album. Giorno Giovanna's Stand, 'Gold Experience', is named after a 1995 Prince album, making him the only one of the four whose primary musical reference is from after 1980.",
    35: "True. Shintaro Kisaragi, the protagonist of the 'Kagerou Project' series, is almost always depicted wearing a red jersey over a black shirt. This has become his signature look across the various media adaptations of the series, including the manga, light novels, and anime.",
    36: "In the anime 'Shirobako', which provides a detailed look into the world of anime production, the main character Aoi Miyamori works as a production assistant at Musashino Animation. In the second half of the series, she is promoted to production manager for the studio's adaptation of the manga 'The Third Aerial Girls Squad'.",
    37: "Super Sonico, the mascot character for the Japanese software company Nitroplus, is known for her love of macarons. This is often mentioned in her character profiles and depicted in various media, including the 'Super Sonico' anime series.",
    38: "'Spirited Away' (2001) was written and directed by the legendary Hayao Miyazaki, a co-founder of the renowned animation powerhouse Studio Ghibli. Miyazaki is one of the most celebrated and influential animators of all time, with a filmography that includes such classics as 'My Neighbor Totoro', 'Princess Mononoke', and 'Howl's Moving Castle'.",
    39: "The English dub of the anime 'Ghost Stories', produced by ADV Films, is infamous for its comedic, ad-libbed script that bears little resemblance to the original Japanese version. The voice actors were given free rein to improvise, resulting in a show filled with pop culture references, fourth-wall breaks, and often-offensive humor. As part of this comedic reimagining, the character of Momoko Koigakubo was portrayed as a devout, born-again Pentecostal Christian, a complete fabrication for the English dub.",
    40: "In 'Fullmetal Alchemist', Edward Elric is given the title of 'Fullmetal Alchemist' by King Bradley when he becomes the youngest State Alchemist in the history of Amestris. The name is a direct and somewhat ironic reference to his prosthetic 'automail' arm and leg, which are made of steel."
}

# Update the explanations for the questions in the batch
for question in questions:
    if question['id'] in new_explanations:
        question['explanation'] = new_explanations[question['id']]

# Write the updated data back to the JSON file
with open('anime_trivia.json', 'w') as f:
    json.dump(questions, f, indent=4)

print("Explanations for batch 3 updated successfully.")
