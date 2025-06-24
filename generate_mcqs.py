import re

def generate_mcqs(text):
    questions = []
    sentences = text.split(".")

    for sentence in sentences:
        sentence = sentence.strip()
        if " is " in sentence and len(sentence.split()) > 5:
            parts = sentence.split(" is ")
            question = f"What is {parts[0].strip()}?"
            answer = parts[1].strip().split(".")[0]
            options = [answer, "Option A", "Option B", "Option C"]
            explanation = f"{parts[0].strip()} is {answer}"
            questions.append({
                "question": question,
                "options": options,
                "answer": answer,
                "explanation": explanation
            })
    return questions
  
