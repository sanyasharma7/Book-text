from generate_mcqs import generate_mcqs

def write_mcqs_to_file(input_file="raw_text.txt", output_file="output_mcqs.txt"):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    mcqs = generate_mcqs(text)

    with open(output_file, "w", encoding="utf-8") as f:
        for i, mcq in enumerate(mcqs):
            f.write(f"Q{i+1}: {mcq['question']}\n")
            for opt in mcq['options']:
                f.write(f"- {opt}\n")
            f.write(f"✅ Answer: {mcq['answer']}\n")
            f.write(f"💡 Explanation: {mcq['explanation']}\n\n")

if __name__ == "__main__":
    write_mcqs_to_file()
  
