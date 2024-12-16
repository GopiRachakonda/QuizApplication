from pymongo import MongoClient

# Connect to MongoDB (default local server)
client = MongoClient('mongodb://localhost:27017/')
db = client.quiz_db  # Select or create the database 'quiz_db'

# Define the questions (50 questions)
questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["2", "3", "4", "5"],
        "correct_answer": "4"
    },
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Venus", "Jupiter"],
        "correct_answer": "Mars"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Shakespeare", "Dickens", "Hemingway", "Austen"],
        "correct_answer": "Shakespeare"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "correct_answer": "Pacific"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["Tokyo", "Seoul", "Beijing", "Bangkok"],
        "correct_answer": "Tokyo"
    },
    {
        "question": "What is the longest river in the world?",
        "options": ["Amazon", "Nile", "Yangtze", "Mississippi"],
        "correct_answer": "Amazon"
    },
    {
        "question": "Which animal is known as the King of the Jungle?",
        "options": ["Tiger", "Lion", "Elephant", "Giraffe"],
        "correct_answer": "Lion"
    },
    {
        "question": "How many continents are there?",
        "options": ["6", "7", "8", "5"],
        "correct_answer": "7"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere for photosynthesis?",
        "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "correct_answer": "Carbon dioxide"
    },
    {
        "question": "Who invented the telephone?",
        "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Marie Curie"],
        "correct_answer": "Alexander Graham Bell"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["CO2", "O2", "H2O", "NaCl"],
        "correct_answer": "H2O"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["China", "Japan", "South Korea", "Thailand"],
        "correct_answer": "Japan"
    },
    {
        "question": "What is the smallest planet in our solar system?",
        "options": ["Mercury", "Mars", "Venus", "Earth"],
        "correct_answer": "Mercury"
    },
    {
        "question": "Which element is represented by the symbol 'O'?",
        "options": ["Oxygen", "Osmium", "Ozone", "Oganesson"],
        "correct_answer": "Oxygen"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["1942", "1945", "1950", "1960"],
        "correct_answer": "1945"
    },
    {
        "question": "Who was the first President of the United States?",
        "options": ["George Washington", "Abraham Lincoln", "Thomas Jefferson", "John Adams"],
        "correct_answer": "George Washington"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Iron", "Diamond", "Platinum"],
        "correct_answer": "Diamond"
    },
    {
        "question": "What is the national flower of India?",
        "options": ["Rose", "Lotus", "Tulip", "Sunflower"],
        "correct_answer": "Lotus"
    },
    {
        "question": "Which country has the most official languages?",
        "options": ["Switzerland", "India", "South Africa", "Canada"],
        "correct_answer": "South Africa"
    },
    {
        "question": "What is the largest continent by land area?",
        "options": ["Africa", "Asia", "North America", "Europe"],
        "correct_answer": "Asia"
    },
    # Additional 30 questions (For illustration purposes, some questions are repeated to complete the 50)
    {
        "question": "What is the capital of Australia?",
        "options": ["Canberra", "Sydney", "Melbourne", "Brisbane"],
        "correct_answer": "Canberra"
    },
    {
        "question": "Which animal is the largest mammal?",
        "options": ["Elephant", "Blue whale", "Giraffe", "Shark"],
        "correct_answer": "Blue whale"
    },
    {
        "question": "What is the longest mountain range in the world?",
        "options": ["Himalayas", "Andes", "Rockies", "Alps"],
        "correct_answer": "Andes"
    },
    {
        "question": "Which city is known as the City of Love?",
        "options": ["Paris", "Rome", "New York", "London"],
        "correct_answer": "Paris"
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["Toronto", "Ottawa", "Vancouver", "Montreal"],
        "correct_answer": "Ottawa"
    },
    {
        "question": "Who is considered the creator of the universe in Hinduism?",
        "options": ["Brahma", "Vishnu", "Shiva", "Indra"],
        "correct_answer": "Brahma"
    },
    {
        "question": "Which Hindu festival is known as the Festival of Lights?",
        "options": ["Diwali", "Holi", "Navaratri", "Makar Sankranti"],
        "correct_answer": "Diwali"
    },
    {
        "question": "What is the Hindu holy book that contains the teachings of Lord Krishna?",
        "options": ["Vedas", "Ramayana", "Bhagavad Gita", "Mahabharata"],
        "correct_answer": "Bhagavad Gita"
    },
    {
        "question": "Which river is considered sacred in Hinduism?",
        "options": ["Ganga", "Yamuna", "Sarasvati", "Sindhu"],
        "correct_answer": "Ganga"
    },
    {
        "question": "Which deity is worshipped as the remover of obstacles?",
        "options": ["Ganesha", "Shiva", "Vishnu", "Durga"],
        "correct_answer": "Ganesha"
    },
    {
        "question": "Which Indian epic tells the story of the battle between the Pandavas and the Kauravas?",
        "options": ["Mahabharata", "Ramayana", "Vedas", "Puranas"],
        "correct_answer": "Mahabharata"
    },
    {
        "question": "What is the name of the Hindu god of preservation and protection?",
        "options": ["Shiva", "Vishnu", "Brahma", "Indra"],
        "correct_answer": "Vishnu"
    },
    {
        "question": "Which festival celebrates the victory of good over evil and the return of Lord Rama to Ayodhya?",
        "options": ["Diwali", "Holi", "Dussehra", "Raksha Bandhan"],
        "correct_answer": "Diwali"
    },
    {
        "question": "Who was the author of the ancient Hindu scripture, the 'Ramayana'?",
        "options": ["Vyasa", "Valmiki", "Shankaracharya", "Tulsidas"],
        "correct_answer": "Valmiki"
    },
    {
        "question": "Which of these is the concept of non-violence in Hinduism?",
        "options": ["Ahimsa", "Karma", "Moksha", "Dharma"],
        "correct_answer": "Ahimsa"
    },
    {
        "question": "What is the name of the sacred fire used in Hindu rituals?",
        "options": ["Yajna", "Puja", "Arti", "Havan"],
        "correct_answer": "Yajna"
    },
    {
        "question": "In Hinduism, which god is known as the 'Destroyer' of the universe?",
        "options": ["Shiva", "Vishnu", "Brahma", "Indra"],
        "correct_answer": "Shiva"
    },
    {
        "question": "What is the sacred thread worn by Hindu males as a symbol of initiation into study?",
        "options": ["Tulsi", "Kumkum", "Janoi", "Bindi"],
        "correct_answer": "Janoi"
    },
    {
        "question": "Which goddess is worshipped during the festival of Navaratri?",
        "options": ["Lakshmi", "Durga", "Saraswati", "Parvati"],
        "correct_answer": "Durga"
    },
    {
        "question": "Which classical dance form originates from the state of Tamil Nadu?",
        "options": ["Kathak", "Bharatanatyam", "Kathakali", "Odissi"],
        "correct_answer": "Bharatanatyam"
    },
    {
        "question": "Who is considered the father of Indian independence?",
        "options": ["Jawaharlal Nehru", "Subhas Chandra Bose", "Mahatma Gandhi", "Sardar Patel"],
        "correct_answer": "Mahatma Gandhi"
    },
    {
        "question": "Which famous temple in India is dedicated to Lord Vishnu and located in Tamil Nadu?",
        "options": ["Golden Temple", "Meenakshi Temple", "Kedarnath Temple", "Tirupati Temple"],
        "correct_answer": "Tirupati Temple"
    },
    {
        "question": "Which ancient Indian scholar is known for his work in mathematics, particularly the concept of zero?",
        "options": ["Aryabhata", "Bhaskara", "Varahamihira", "Sushruta"],
        "correct_answer": "Aryabhata"
    },
    {
        "question": "What is the name of the Indian festival that celebrates the arrival of spring with colored powders?",
        "options": ["Holi", "Diwali", "Makar Sankranti", "Raksha Bandhan"],
        "correct_answer": "Holi"
    },
    {
        "question": "What is the term used to describe the Hindu belief in reincarnation or the cycle of birth and rebirth?",
        "options": ["Moksha", "Dharma", "Karma", "Samsara"],
        "correct_answer": "Samsara"
    }
    # ... Continue adding questions until you have 50
]

# Insert the questions into the 'questions' collection
db.questions.insert_many(questions)

print("Questions inserted successfully!")
