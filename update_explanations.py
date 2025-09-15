import json

def update_explanations(file_path):
    with open(file_path, 'r') as f:
        questions = json.load(f)

    explanations = {
        "353": "In photography, overexposure is the state of being exposed to too much light, resulting in a washed-out or overly bright image. Underexposure is the opposite.",
        "354": "The French word 'poisson' translates to 'fish' in English.",
        "355": "A lute is a plucked string instrument with a deep round back enclosing a hollow cavity, usually with a sound hole or rose. It is a stringed instrument.",
        "356": "Eel (unagi and anago) is a common ingredient in Japanese cooking, often as part of a donburi dish, or as a type of sushi.",
        "357": "Marvin Lee Aday was the birth name of the American singer and actor Meat Loaf.",
        "358": "'The Government Inspector' is a satirical play by the Russian and Ukrainian dramatist and novelist Nikolai Gogol, published in 1836.",
        "359": "Woodrow Wilson was the 28th president of the United States, serving from 1913 to 1921. A member of the Democratic Party, Wilson served as the president of Princeton University and as the governor of New Jersey before winning the 1912 presidential election.",
        "360": "Riga is the capital and largest city of Latvia. Oslo is in Norway, Prague is in the Czech Republic, and Rome is in Italy.",
        "361": "\"Good Vibrations\" is a song by the American rock band the Beach Boys, released in 1966. The song was a commercial success, and is considered one of the most influential songs of the psychedelic era.",
        "362": "The Russian ruble or rouble is the official currency of the Russian Federation.",
        "363": "The Thirty Years' War was a series of wars in Central Europe between 1618 and 1648. It was one of the longest and most destructive conflicts in European history.",
        "364": "A prehensile tail is the tail of an animal that has adapted to be able to grasp or hold objects. Fully prehensile tails can be used to hold and manipulate objects, and in particular to aid arboreal creatures in finding and eating food in the trees.",
        "365": "Alchemy is an ancient branch of natural philosophy, a philosophical and protoscientific tradition practiced throughout Europe, Africa, and Asia. It aimed to purify, mature, and perfect certain objects. Common aims were chrysopoeia, the transmutation of 'base metals' (e.g., lead) into 'noble metals' (particularly gold).",
        "366": "'The Bathers' is a series of oil paintings by French artist Paul C\u00e9zanne. The paintings are considered one of the cornerstones of modern art.",
        "367": "The New York Islanders are a professional ice hockey team based in Elmont, New York. They compete in the National Hockey League (NHL).",
        "368": "Darth Vader's lightsaber is red, a color associated with the Sith, the dark side of the Force.",
        "369": "Phycology is the scientific study of algae. Also known as algology, phycology is a branch of life science.",
        "370": "Bishkek is the capital and largest city of Kyrgyzstan. The capitals of Denmark, United Arab Emirates, and Lithuania are Copenhagen, Abu Dhabi, and Vilnius respectively.",
        "371": "Italy shares land borders with France, Switzerland, Austria, and Slovenia. It also has a maritime border with Malta.",
        "372": "George Best was a Northern Irish professional footballer who played as a winger, spending most of his club career at Manchester United. A highly skilful dribbler, Best is regarded as one of the greatest players of all time."
    }

    for question in questions:
        q_id = str(question.get("ID"))
        if q_id in explanations:
            question["explanation"] = explanations[q_id]

    with open(file_path, 'w') as f:
        json.dump(questions, f, indent=2)

if __name__ == "__main__":
    update_explanations('trivia_questions.json')
