import json

def create_question(anime_title, category, difficulty, question, correct_answer, wrong_answers, explanation):
    """
    Creates a new question and adds it to the anime_trivia.json file.
    """
    try:
        with open("anime_trivia.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    new_question = {
        "id": len(data) + 1,
        "anime_title": anime_title,
        "category": category,
        "difficulty": difficulty,
        "question": question,
        "correct_answer": correct_answer,
        "wrong_answers": wrong_answers,
        "explanation": explanation,
    }

    data.append(new_question)

    with open("anime_trivia.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Successfully created question with ID {new_question['id']}.")


if __name__ == "__main__":
    create_question(
        "My Hero Academia",
        "Anime",
        "Easy",
        "How does Izuku Midoriya become a superhero in My Hero Academia?",
        "He inherits the powers of a previous superhero",
        ["He receives superpowers from an alien source", "He trains under the guidance of a professional hero"],
        "In 'My Hero Academia', Izuku Midoriya, who was born without a 'Quirk' (superpower), inherits the power of 'One For All' from the world's greatest hero, All Might."
    )
    create_question(
        "Attack on Titan",
        "Anime",
        "Easy",
        "How do the main characters in Attack on Titan battle against the Titans?",
        "With swords and grappling hooks",
        ["With magic spells", "With giant robotic suits"],
        "The soldiers in 'Attack on Titan' use a set of equipment called Omni-Directional Mobility Gear, which allows them to navigate in a 3D space using grappling hooks and gas propulsion, and they fight with specialized swords."
    )
    create_question(
        "One Punch Man",
        "Anime",
        "Easy",
        "How does Saitama, the main character in One Punch Man, become the world’s strongest hero?",
        "He accidentally becomes too strong through his training",
        ["He’s the world’s only hero", "He is granted a wish"],
        "In 'One Punch Man', Saitama's immense power is said to be the result of a daily training regimen of 100 push-ups, 100 sit-ups, 100 squats, and a 10km run, which he did for three years."
    )
    create_question(
        "Sword Art Online",
        "Anime",
        "Medium",
        "Why does the main character in Sword Art Online become trapped in a virtual reality game?",
        "A glitch in the game’s programming prevents players from logging out",
        ["He is kidnapped and forced to play the game against his will", "He gets trapped on purpose, because he doesn’t want to leave"],
        "In 'Sword Art Online', the creator of the game, Akihiko Kayaba, intentionally removes the log out button, trapping the players in the game. It was not a glitch, but a deliberate act."
    )
    create_question(
        "Your Name",
        "Anime",
        "Medium",
        "How did the director of Your Name create the realistic backgrounds in the film?",
        "He used real-life locations and photographs as references",
        ["The backgrounds were entirely AI-generated", "The backgrounds were recycled from other projects"],
        "The director of 'Your Name', Makoto Shinkai, is known for his visually stunning films that often feature backgrounds based on real-life locations in Japan. He and his team use photographs as references to create the detailed and realistic scenery."
    )
    create_question(
        "Death Note",
        "Anime",
        "Easy",
        "In Death Note, how does Light Yagami first discover the infamous notebook?",
        "He sees it fall from the sky",
        ["It is delivered to him in a mysterious box", "He receives it as a gift from a friend"],
        "In 'Death Note', Light Yagami finds the Death Note after it is dropped into the human world by the Shinigami named Ryuk, who was bored with the Shinigami Realm."
    )
    create_question(
        "Fruits Basket",
        "Anime",
        "Easy",
        "In Fruits Basket, what is the name of the main character who lives with a family cursed to transform into animals of the Chinese zodiac?",
        "Tohru",
        ["Yuki", "Kyo"],
        "Tohru Honda is the protagonist of 'Fruits Basket'. After her mother's death, she ends up living with the Sohma family and discovers their secret curse."
    )
    create_question(
        "Haikyuu!!",
        "Anime",
        "Easy",
        "Haikyuu!! is an anime about a high school sports team, practising which sport?",
        "Volleyball",
        ["Baseball", "Hockey"],
        "'Haikyuu!!' is a popular sports anime that revolves around the Karasuno High School boys' volleyball team and their journey to the top."
    )
    create_question(
        "Paradise Kiss",
        "Anime",
        "Hard",
        "Which anime series follows the story of a young girl who dreams of becoming a fashion designer?",
        "Paradise Kiss",
        ["Nana", "Skip Beat!"],
        "'Paradise Kiss' is a manga and anime series by Ai Yazawa, which tells the story of Yukari Hayasaka, a high school student who is scouted by a group of fashion design students and becomes a model for their brand."
    )
    create_question(
        "Natsume's Book of Friends",
        "Anime",
        "Medium",
        "In Natsume’s Book of Friends, what is the name of the main character who can see spirits?",
        "Takashi Natsume",
        ["Nyanko-sensei", "Reiko Natsume"],
        "The protagonist of 'Natsume's Book of Friends' is Takashi Natsume, a boy who has been able to see yokai (spirits) since he was young. He inherits the 'Book of Friends' from his grandmother, Reiko Natsume."
    )
