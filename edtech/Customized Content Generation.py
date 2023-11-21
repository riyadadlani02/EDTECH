import openai
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier


openai.api_key = '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'


learning_data = {
    'text': [
        "This is a visual way to learn. Use diagrams and charts.",
        "I prefer reading textbooks for learning.",
        "I learn best through hands-on experiences.",
        # Add more learning styles and content here
    ],
    'learning_style': ['Visual', 'Reading', 'Hands-on']  # Learning style labels
}


df = pd.DataFrame(learning_data)


def generate_content(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['text'])


clf = RandomForestClassifier()
clf.fit(X, df['learning_style'])


def generate_personalized_content(student_input):
   
    input_vector = vectorizer.transform([student_input])
    predicted_style = clf.predict(input_vector)[0]

    
    content_prompt = f"Generate content for a {predicted_style} learner: {student_input}"
    generated_content = generate_content(content_prompt)
    return generated_content


student_input = "I find it easier to understand concepts through visual representations."
personalized_content = generate_personalized_content(student_input)
print(personalized_content)
