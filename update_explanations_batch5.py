import json

# Load the trivia questions from the JSON file
with open('anime_trivia.json', 'r') as f:
    questions = json.load(f)

# Define the new explanations for the fifth batch
new_explanations = {
    42: "In the first episode of the Pokémon anime, 'Pokémon, I Choose You!', it is stated that trainers can begin their journey at the age of 10. Ash Ketchum famously oversleeps on his 10th birthday and misses the opportunity to choose one of the three starter Pokémon. Despite the many years that have passed in the real world, Ash's age has remained a consistent 10 years old throughout the series, a fact that has become a running gag and a topic of much fan debate.",
    43: "The undefeated gaming duo of Sora and Shiro are known in the online world as 'Blank' (空白, Kūhaku). This name comes from their practice of leaving their in-game names empty. The name is also a clever pun, as the Japanese word 'kūhaku' is written with the kanji for 'sky' (空, sora) and 'white' (白, shiro), the names of the two main characters.",
    44: "True. The protagonist of 'Humanity Has Declined' is a nameless narrator who refers to herself in the first person as 'I' (watashi). This is a deliberate stylistic choice by the author, Romeo Tanaka, which reflects the series' themes of fading identity and the protagonist's cynical, detached perspective on the absurd, post-apocalyptic world she inhabits.",
    45: "False. While often compared to the works of Studio Ghibli, 'Wolf Children' and 'The Boy and the Beast' were actually directed by the acclaimed director Mamoru Hosoda and animated by his studio, Studio Chizu. Studio Ghibli, co-founded by Hayao Miyazaki, is famous for films such as 'Spirited Away', 'My Neighbor Totoro', and 'Princess Mononoke'.",
    46: "'Yare yare daze' (やれやれだぜ) is the iconic catchphrase of Jotaro Kujo, the protagonist of 'Stardust Crusaders', the third part of 'JoJo's Bizarre Adventure'. The phrase, which roughly translates to 'Gimme a break...' or 'What a pain...', perfectly encapsulates Jotaro's cool, stoic, and often exasperated personality. It is one of the most famous and beloved catchphrases in all of anime.",
    47: "True. In the sequel series, 'To Love-Ru Darkness', it is revealed that the true name of the powerful assassin Golden Darkness, or 'Yami', is Eve. She was created by the scientist Tearju Lunatique, and her name is a direct reference to the character Eve from the manga 'Black Cat', which was also created by 'To Love-Ru' illustrator Kentaro Yabuki.",
    48: "Medaka Kurokami's Abnormality is called 'The End'. This incredibly powerful ability allows her to learn any skill or superpower she sees or hears about, and to master it to a level of 'perfection' that surpasses the original user. This reflects her character concept as a 'perfect' human being who can overcome any challenge.",
    49: "Seiji Kishi is a prolific anime director who has helmed many popular series. He directed 'Humanity Has Declined', 'Assassination Classroom', and 'Danganronpa: The Animation'. 'Another', a horror mystery series, was directed by Tsutomu Mizushima.",
    51: "Josuke Higashikata is the protagonist of 'Diamond is Unbreakable', the fourth part of 'JoJo's Bizarre Adventure'. He is the illegitimate son of Joseph Joestar, the protagonist of the second part, 'Battle Tendency'. Josuke's Stand is 'Crazy Diamond', which has the ability to restore objects and living things to a previous state, a power he often uses to heal injuries and repair objects.",
    52: "'Mob Psycho 100' was animated by Studio Bones, a studio renowned for its high-quality animation and action sequences. Bones is also responsible for other acclaimed series such as 'Fullmetal Alchemist: Brotherhood', 'My Hero Academia', 'Soul Eater', and 'Eureka Seven'.",
    53: "'Uzumaki', the classic horror manga about a town obsessed with spirals, was written and illustrated by the master of horror, Junji Ito. Ito is famous for his unique and terrifying brand of body horror and cosmic horror, and his other major works include 'Tomie' and 'Gyo'.",
    54: "True. In 2003, 'Spirited Away' won the Academy Award for Best Animated Feature, becoming the first, and to date, the only hand-drawn, non-English language animated film to win the prestigious award. This historic win helped to introduce a new generation of Western audiences to the world of anime."
}

# Update the explanations for the questions in the batch
for question in questions:
    if question['id'] in new_explanations:
        question['explanation'] = new_explanations[question['id']]

# Write the updated data back to the JSON file
with open('anime_trivia.json', 'w') as f:
    json.dump(questions, f, indent=4)

print("Explanations for batch 5 updated successfully.")
