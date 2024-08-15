import PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text


def analyze_text(text):
    # This is a placeholder for more complex NLP analysis
    faqs = {}
    
    # Example: Extract responses based on keywords
    if "hobbies" in text.lower():
        faqs["What are your hobbies?"] = "I enjoy hiking, reading, and painting."
    
    if "favorite food" in text.lower():
        faqs["What's your favorite food?"] = "I love Italian cuisine, especially pasta."

    return faqs


class FAQChatbot:
    def __init__(self, faqs):
        self.faqs = faqs

    def get_response(self, question):
        for key in self.faqs:
            if key.lower() in question.lower():
                return self.faqs[key]
        return "I'm not sure how to answer that. Can you provide the answer?"

# Example usage
pdf_text = extract_text_from_pdf("user_profile.pdf")
faq_data = analyze_text(pdf_text)
chatbot = FAQChatbot(faq_data)

# Example interaction
question = "What are your hobbies?"
response = chatbot.get_response(question)
print(response)






