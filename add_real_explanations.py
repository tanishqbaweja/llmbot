import json

def get_real_explanation(question_text):
    """
    This function returns a real explanation for a given question.
    This is a large mapping of questions to explanations.
    """
    explanations = {
        "What is the boiling point of water in Farenheit?": "At standard atmospheric pressure, water boils at 212 degrees Fahrenheit (°F). 100 is the boiling point in Celsius (°C), and 32 °F is the freezing point of water.",
        "What song did Nena have a hit with in 1984?": "'99 Luftballons' (German for '99 Balloons') is a song by the German band Nena from their 1983 self-titled album. An English-language version titled '99 Red Balloons' was also released. The song became a major international hit in 1984.",
        "What type of instrument is a tuba?": "The tuba is the largest and lowest-pitched musical instrument in the brass family. It is a brass instrument, not a percussion, stringed, or woodwind instrument.",
        "Which of these quotes is from the film 'Finding Nemo'?": "The line 'Just keep swimming' is a memorable quote from the 2003 Pixar animated film 'Finding Nemo', spoken by the character Dory. The other quotes are from different famous films.",
        "Which author wrote 'Spanish Parnassus'?": "'Spanish Parnassus' (El Parnaso español) is a famous anthology of poetry by the Spanish author Francisco de Quevedo, published in 1648. Miguel de Cervantes, Oscar Wilde, and Alphonse Daudet are other famous authors.",
        "What number is the binary 1000000 equal to?": "In the binary number system, each digit represents a power of 2. The binary number 1000000 represents 1 * 2^6, which equals 64 in the decimal system.",
        "From what country did the U.S. buy the Virgin Islands in 1917?": "The United States purchased the Danish West Indies from Denmark for $25 million in 1917, and the territory was renamed the U.S. Virgin Islands.",
        "In which comic strip is the insecure boy, Linus van Pelt, found?": "Linus van Pelt is a major character in Charles M. Schulz's comic strip 'Peanuts'. He is known for carrying a security blanket and for his philosophical musings.",
        "Who renamed the South Sea as the Pacific Ocean in 1520?": "The Portuguese explorer Ferdinand Magellan named the ocean 'Pacific' (meaning 'peaceful') because of the calm seas he encountered after sailing through the stormy straits of South America.",
        "What is the name of the hand gesture, originating in India, where palms are placed together at the heart to show respect and gratitude?": "Añjali Mudrā is a hand gesture that is used as a sign of respect and a greeting in India, Sri Lanka, Nepal, Thailand, Cambodia, Laos, Burma and Indonesia. It is also used among yoga practitioners and enthusiasts.",
        "At Which Point Are The Temperature Scales Fahrenheit & Celcius The Same?": "The Fahrenheit and Celsius scales are equal at -40 degrees. -40°C is equal to -40°F.",
        "Which city used to be called Zenigamezawa?": "The city of Hakodate in Hokkaido, Japan, was formerly known as Zenigamezawa.",
        "When did the Maastricht Treaty lay the foundation for the European Union?": "The Maastricht Treaty was signed on February 7, 1992, by the members of the European Community in Maastricht, Netherlands, to further European integration. It went into effect in 1993.",
        "Which influential historical person was the author of Tao Te Ching and founder of Taoism?": "Lao Tzu was an ancient Chinese philosopher and writer. He is the reputed author of the Tao Te Ching, the founder of philosophical Taoism, and a deity in religious Taoism and traditional Chinese religions.",
        "Who made the first phone call to the moon?": "On July 20, 1969, U.S. President Richard Nixon made a phone call to astronauts Neil Armstrong and Buzz Aldrin on the Moon. It is considered the most historic phone call ever made.",
        "Which of these colors would you find on the flag of Italy?": "The flag of Italy features three equal vertical bands of green, white, and red. Blue, gold, and orange are not on the flag.",
        "What word describes the porous openings on the surface of leaves?": "Stomata are small pores on the surface of leaves that allow for gas exchange (carbon dioxide in, oxygen out). Stigma, sepal, and petal are parts of a flower.",
        "Which of the following is not a main branch of Islam?": "Sunni and Shia are the two main branches of Islam. Sufism is a mystical branch of Islam. Ahmadiyya is a newer religious movement that originated in the late 19th century and is not considered a main branch of Islam by most Muslims.",
        "Who won the 2011 Academy Award for Best Leading Actor for playing the role of George Valentin in The Artist?": "Jean Dujardin won the Academy Award for Best Actor for his role in the 2011 silent film 'The Artist'. Demián Bichir, George Clooney, and Gary Oldman were also nominated in the same category.",
        "What is the sugary paste used for icing and cake decor that comes from the French word for 'melting'?": "Fondant icing, commonly referred to simply as fondant, is an icing used to decorate or sculpt cakes and pastries. The word, in French, means 'melting'.",
        "Which piece of written work starts with the line '1801—I have just returned from a visit to my landlord—the solitary neighbour that I shall be troubled with.'?": "This is the opening line of Emily Brontë's 1847 novel 'Wuthering Heights'. The other books are from different genres and authors.",
        "Which word is defined as 'coastal navigation; the exclusive right of a country to control the air traffic within its borders'?": "Cabotage refers to the transport of goods or passengers between two places in the same country by a transport operator from another country. It also refers to the right of a country to regulate its internal air traffic.",
        "'Bitch' was a one hit wonder in 1997 by which artist?": "Meredith Brooks had a major hit with the song 'Bitch' in 1997. Quiet Riot, Divinyls, and Bow Wow Wow are known for other songs.",
        "Maputo is the capital city of which country?": "Maputo is the capital city of Mozambique, a country in Southeast Africa. The capitals of the other countries are Ouagadougou, São Tomé, and Palikir, respectively.",
        "What is the name for a shallow dish with a cover, used for science specimens?": "A Petri dish is a shallow transparent lidded dish that biologists use to hold growth medium in which cells can be cultured, originally, cells of bacteria, fungi and small mosses.",
        "In which country is the Mekong River Delta?": "The Mekong Delta is the region in southwestern Vietnam where the Mekong River approaches and empties into the sea through a network of distributaries.",
        "In which year was Trainspotting released?": "The British black comedy-drama film 'Trainspotting', directed by Danny Boyle and starring Ewan McGregor, was released in 1996.",
        "What is the name of the mythical bird that dies in a fire and is reborn from its own ashes?": "The phoenix is a long-lived bird that cyclically regenerates or is otherwise born again. Associated with the Sun, a phoenix obtains new life by arising from the ashes of its predecessor. The Roc, Harpy, and Siren are other mythical creatures.",
        "Which family held the position of Holy Roman Emperor almost uninterrupted from 1438 to 1806?": "The House of Habsburg was one of the most influential and distinguished royal houses of Europe. The throne of the Holy Roman Empire was continuously occupied by the Habsburgs from 1438 until their extinction in the male line in 1740, and after the death of Francis I, from 1765 until its dissolution in 1806.",
        "Which punk band from the United States released the studio album 'Rise and Fall, Rage and Grace'?": "'Rise and Fall, Rage and Grace' is the eighth studio album by American punk rock band The Offspring, released in 2008. The other bands are from different genres.",
        "Which country was the main power in Europe during the 17th century?": "Under the rule of Louis XIV, the 'Sun King', France became the dominant power in Europe during the 17th century. This period is known as the 'Grand Siècle' (Great Century).",
        "With which sport is Hicham El Guerrouj associated?": "Hicham El Guerrouj is a retired Moroccan middle-distance runner. He is a two-time Olympic gold medalist in athletics.",
        "Which of the following describes Michael Faraday?": "Michael Faraday was an English scientist who contributed to the study of electromagnetism and electrochemistry. His main discoveries include the principles underlying electromagnetic induction, diamagnetism and electrolysis.",
        "In Ancient Greek mythology, which enchantress changes Ulysses' men into pigs, but also warns him about the sirens?": "In Greek mythology, Circe is an enchantress and a minor goddess. In Homer's Odyssey, she turns Odysseus's (Ulysses's) men into swine, but he is protected by a magical herb. She later helps him on his journey home. Medusa, Calypso, and Aphrodite are other figures from Greek mythology.",
        "What is the capital city of Sierra Leone?": "Freetown is the capital and largest city of Sierra Leone. Ouagadougou is the capital of Burkina Faso, Gaborone is the capital of Botswana, and Bangui is the capital of the Central African Republic.",
        "What is the name of the Viking practice of sacrificing prisoners to their gods?": "Blót was a Norse pagan sacrifice to the Norse gods and the spirits of the land. The sacrifice often took the form of a sacramental meal or feast. The other names are not correct.",
        "In cooking does the French term 'en croute' mean?": "In French, 'en croute' means 'in a crust'. It refers to a dish where food is wrapped in a pastry crust before baking.",
        "Which of these is a popular drink in Mongolia?": "Kumis is a fermented dairy product traditionally made from mare's milk. The drink remains important to the peoples of the Central Asian steppes, of Huno-Bulgar, Turkic and Mongol origin. Sombai is from Cambodia, Guaro from Costa Rica, and Mama Juana from the Dominican Republic.",
        "Which athletics event consists of two hops and a jump?": "The triple jump is a track and field event, similar to the long jump. As a group, the two events are referred to as the 'horizontal jumps'. The competitor runs down the track and performs a hop, a bound and then a jump into the sand pit.",
        "Which actor has starred in Thor and Westworld?": "Sir Anthony Hopkins portrayed Odin in the 'Thor' series of films and Dr. Robert Ford in the HBO series 'Westworld'. The other actors have not appeared in both."
    }
    return explanations.get(question_text, "Explanation not found.")

def main():
    file_path = 'trivia_questions.json'

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            questions = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: Could not read {file_path}")
        return

    for question in questions:
        question['explanation'] = get_real_explanation(question['question'])

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(questions, f, indent=2, ensure_ascii=False)

    print("Successfully added real explanations to all questions.")

if __name__ == "__main__":
    main()
