import json

def append_questions(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Find the highest existing ID
    max_id = 0
    for question in data:
        if question['ID'].startswith('IND'):
            try:
                num_part = int(question['ID'][3:])
                if num_part > max_id:
                    max_id = num_part
            except ValueError:
                continue

    new_questions = [
        {
            "ID": f"IND{max_id + 1}",
            "category": "Geography",
            "difficulty": "Medium",
            "question_text": "Which is the highest peak in India?",
            "correct_answer": "Kangchenjunga",
            "wrong_answers": [
                "Nanda Devi",
                "K2",
                "Mount Everest"
            ],
            "explanation": "Kangchenjunga, located in the Himalayas on the border of Nepal and the Indian state of Sikkim, is the highest peak in India and the third highest in the world. While K2 is higher, it is located in Pakistan-occupied Kashmir. Mount Everest is in Nepal."
        },
        {
            "ID": f"IND{max_id + 2}",
            "category": "History",
            "difficulty": "Medium",
            "question_text": "The Jallianwala Bagh massacre took place in which Indian city in 1919?",
            "correct_answer": "Amritsar",
            "wrong_answers": [
                "Lahore",
                "Delhi",
                "Jalandhar"
            ],
            "explanation": "The Jallianwala Bagh massacre occurred in Amritsar, Punjab, on 13 April 1919, when troops of the British Indian Army under the command of Colonel Reginald Dyer fired rifles into a crowd of unarmed Indian civilians who had gathered in a public garden."
        },
        {
            "ID": f"IND{max_id + 3}",
            "category": "Culture",
            "difficulty": "Medium",
            "question_text": "Which Indian state is famous for its 'Pattachitra' style of cloth-based scroll painting?",
            "correct_answer": "Odisha",
            "wrong_answers": [
                "West Bengal",
                "Bihar",
                "Rajasthan"
            ],
            "explanation": "Pattachitra is a traditional, cloth-based scroll painting based in the eastern Indian states of Odisha and West Bengal. In the Sanskrit language, 'Patta' means 'cloth' and 'Chitra' means 'picture'. It is known for its intricate details as well as mythological narratives and folktales."
        },
        {
            "ID": f"IND{max_id + 4}",
            "category": "Film",
            "difficulty": "Medium",
            "question_text": "Who is often called the 'First Lady of Indian Cinema'?",
            "correct_answer": "Devika Rani",
            "wrong_answers": [
                "Nargis",
                "Madhubala",
                "Meena Kumari"
            ],
            "explanation": "Devika Rani was a pioneering actress in Indian cinema who was active during the 1930s and 1940s. Widely acknowledged as the 'First Lady of Indian Cinema', she was a co-founder of the Bombay Talkies studio. Nargis, Madhubala, and Meena Kumari were other legendary actresses from a later era."
        },
        {
            "ID": f"IND{max_id + 5}",
            "category": "Cuisine",
            "difficulty": "Medium",
            "question_text": "What is the key ingredient in the sweet dish 'Gajar ka Halwa'?",
            "correct_answer": "Carrots",
            "wrong_answers": [
                "Semolina",
                "Lentils",
                "Bottle Gourd"
            ],
            "explanation": "'Gajar ka Halwa' is a carrot-based sweet dessert pudding from the Indian subcontinent. 'Gajar' is the Hindi word for carrot. Semolina is used for 'Sooji Halwa', and bottle gourd for 'Dudhi Halwa'."
        },
        {
            "ID": f"IND{max_id + 6}",
            "category": "Geography",
            "difficulty": "Medium",
            "question_text": "The city of Mumbai is located on which coast of India?",
            "correct_answer": "West Coast",
            "wrong_answers": [
                "East Coast",
                "South Coast",
                "North Coast"
            ],
            "explanation": "Mumbai, the financial capital of India, is a major port city located on the west coast of India, along the Arabian Sea."
        },
        {
            "ID": f"IND{max_id + 7}",
            "category": "History",
            "difficulty": "Hard",
            "question_text": "Who was the last Mughal emperor of India?",
            "correct_answer": "Bahadur Shah Zafar",
            "wrong_answers": [
                "Aurangzeb",
                "Shah Jahan",
                "Akbar II"
            ],
            "explanation": "Bahadur Shah Zafar was the last Mughal emperor. He was a nominal ruler, as the Mughal Empire existed in name only and his authority was limited only to the city of Delhi. He was deposed by the British and exiled to Burma following the Indian Rebellion of 1857."
        },
        {
            "ID": f"IND{max_id + 8}",
            "category": "Science & Technology",
            "difficulty": "Medium",
            "question_text": "India's first nuclear test was conducted in 1974 under what code name?",
            "correct_answer": "Smiling Buddha",
            "wrong_answers": [
                "Operation Shakti",
                "Project 596",
                "Trinity"
            ],
            "explanation": "Smiling Buddha was the assigned code name of India's first successful nuclear bomb test on 18 May 1974. Operation Shakti was the code name for the second series of tests in 1998. Trinity was the code name for the first US nuclear test."
        },
        {
            "ID": f"IND{max_id + 9}",
            "category": "Culture",
            "difficulty": "Medium",
            "question_text": "The 'Golden Temple', the holiest shrine in Sikhism, is located in which city?",
            "correct_answer": "Amritsar",
            "wrong_answers": [
                "Anandpur Sahib",
                "Ludhiana",
                "Patna"
            ],
            "explanation": "The Golden Temple, also known as Harmandir Sahib, is a gurdwara located in the city of Amritsar, Punjab, India. It is the preeminent spiritual site of Sikhism."
        },
        {
            "ID": f"IND{max_id + 10}",
            "category": "Sports",
            "difficulty": "Medium",
            "question_text": "Who is the first Indian woman to win a medal at the Olympics?",
            "correct_answer": "Karnam Malleswari",
            "wrong_answers": [
                "P. T. Usha",
                "Mary Kom",
                "Saina Nehwal"
            ],
            "explanation": "Karnam Malleswari won a bronze medal in weightlifting at the 2000 Sydney Olympics, making her the first Indian woman to win an Olympic medal. Mary Kom and Saina Nehwal won medals in later Olympics, and P.T. Usha narrowly missed a medal in 1984."
        },
        {
            "ID": f"IND{max_id + 11}",
            "category": "Geography",
            "difficulty": "Medium",
            "question_text": "The 'Sundarbans', the world's largest mangrove forest, is located in which Indian state?",
            "correct_answer": "West Bengal",
            "wrong_answers": [
                "Odisha",
                "Andhra Pradesh",
                "Gujarat"
            ],
            "explanation": "The Sundarbans is a mangrove area in the delta formed by the confluence of the Ganges, Brahmaputra and Meghna Rivers in the Bay of Bengal. It spans from the Hooghly River in India's state of West Bengal to the Baleswar River in Bangladesh."
        },
        {
            "ID": f"IND{max_id + 12}",
            "category": "History",
            "difficulty": "Medium",
            "question_text": "Who was the first President of India?",
            "correct_answer": "Rajendra Prasad",
            "wrong_answers": [
                "Sarvepalli Radhakrishnan",
                "Zakir Husain",
                "V. V. Giri"
            ],
            "explanation": "Rajendra Prasad was an Indian independence activist, lawyer, scholar and subsequently, the first president of India, in office from 1950 to 1962. The other individuals were also presidents of India who served in later years."
        },
        {
            "ID": f"IND{max_id + 13}",
            "category": "Culture",
            "difficulty": "Medium",
            "question_text": "The festival of 'Onam' is predominantly celebrated in which Indian state?",
            "correct_answer": "Kerala",
            "wrong_answers": [
                "Tamil Nadu",
                "Karnataka",
                "Andhra Pradesh"
            ],
            "explanation": "Onam is an annual harvest festival celebrated in the Indian state of Kerala. It is a major annual event for Keralites and is the official festival of the state."
        },
        {
            "ID": f"IND{max_id + 14}",
            "category": "Cuisine",
            "difficulty": "Medium",
            "question_text": "Which Indian city is famous for its sweet, spongy, cheese-based dessert called 'Rasgulla'?",
            "correct_answer": "Kolkata",
            "wrong_answers": [
                "Delhi",
                "Mumbai",
                "Chennai"
            ],
            "explanation": "Rasgulla is a syrupy dessert popular in the Indian subcontinent and regions with South Asian diaspora. It is made from ball-shaped dumplings of chhena and semolina dough, cooked in light syrup made of sugar. It is strongly associated with the city of Kolkata in West Bengal."
        },
        {
            "ID": f"IND{max_id + 15}",
            "category": "Geography",
            "difficulty": "Medium",
            "question_text": "Which union territory of India is a former French colony?",
            "correct_answer": "Puducherry",
            "wrong_answers": [
                "Goa",
                "Daman and Diu",
                "Andaman and Nicobar Islands"
            ],
            "explanation": "Puducherry (formerly Pondicherry) is a union territory of India. It was formed out of four territories of former French India, namely Pondichéry, Karikal, Mahé and Yanaon. Goa, Daman and Diu were former Portuguese colonies."
        },
        {
            "ID": f"IND{max_id + 16}",
            "category": "Science & Technology",
            "difficulty": "Medium",
            "question_text": "Who is known as the 'Missile Man of India' for his work on the development of ballistic missile and launch vehicle technology?",
            "correct_answer": "A. P. J. Abdul Kalam",
            "wrong_answers": [
                "Vikram Sarabhai",
                "Homi J. Bhabha",
                "C. V. Raman"
            ],
            "explanation": "Dr. A. P. J. Abdul Kalam, who served as the 11th President of India, was an aerospace scientist who played a leading role in the development of India's missile and nuclear weapons programs. He is affectionately known as the 'Missile Man of India'."
        },
        {
            "ID": f"IND{max_id + 17}",
            "category": "History",
            "difficulty": "Medium",
            "question_text": "The 'Green Revolution' in India, which led to a significant increase in food grain production, was primarily led by which scientist?",
            "correct_answer": "M. S. Swaminathan",
            "wrong_answers": [
                "Verghese Kurien",
                "Norman Borlaug",
                "C. Subramaniam"
            ],
            "explanation": "M. S. Swaminathan is an Indian geneticist and administrator, known for his leadership and success in introducing and further developing high-yielding varieties of wheat in India. He is known as the 'Father of the Green Revolution in India'. Verghese Kurien led the 'White Revolution' (milk production)."
        },
        {
            "ID": f"IND{max_id + 18}",
            "category": "Culture",
            "difficulty": "Hard",
            "question_text": "Which of these is a form of traditional shadow puppetry from the state of Andhra Pradesh?",
            "correct_answer": "Tholu Bommalata",
            "wrong_answers": [
                "Yakshagana",
                "Kathputli",
                "Pavakoothu"
            ],
            "explanation": "Tholu Bommalata is the shadow puppet theatre tradition of the state of Andhra Pradesh. Its performers are part of a group of wandering entertainers and peddlers who pass through villages for a few weeks in a year. Yakshagana is a theatre form from Karnataka, Kathputli is a string puppet tradition from Rajasthan, and Pavakoothu is a glove puppet tradition from Kerala."
        },
        {
            "ID": f"IND{max_id + 19}",
            "category": "Film",
            "difficulty": "Medium",
            "question_text": "Who composed the acclaimed soundtrack for the film 'Slumdog Millionaire', winning two Academy Awards?",
            "correct_answer": "A. R. Rahman",
            "wrong_answers": [
                "Anu Malik",
                "Pritam",
                "Shankar-Ehsaan-Loy"
            ],
            "explanation": "A. R. Rahman, a renowned Indian music composer, won two Academy Awards for the 2008 film 'Slumdog Millionaire' - one for Best Original Score and another for Best Original Song ('Jai Ho'). The other individuals are also popular Bollywood music composers."
        },
        {
            "ID": f"IND{max_id + 20}",
            "category": "Cuisine",
            "difficulty": "Medium",
            "question_text": "Which spice is a key ingredient in the Indian dish 'Vindaloo'?",
            "correct_answer": "Chili Peppers",
            "wrong_answers": [
                "Turmeric",
                "Cardamom",
                "Cloves"
            ],
            "explanation": "Vindaloo is an Indian curry dish, popular in the region of Goa. The defining characteristic of a vindaloo is its fiery heat, which comes from the generous use of chili peppers, often combined with vinegar. While other spices are used, the chili is paramount."
        }
    ]

    # Remove placeholders
    data = [q for q in data if q.get('category') != 'Placeholder']

    data.extend(new_questions)

    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    append_questions('india_trivia.json')
