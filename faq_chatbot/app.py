import fitz  # PyMuPDF
import spacy
from flask import Flask, request, render_template
# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Function to analyze the extracted text using SpaCy
def analyze_text_spacy(text):
    faqs = {}
    
    # Process text with SpaCy
    doc = nlp(text)

    # Extract entities and classify information
    person_name = None
    organization_name = None
    location_name = None

    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            person_name = ent.text
            faqs["Who are you?"] = person_name
        elif ent.label_ == 'ORG':
            organization_name = ent.text
            faqs["Where do you work?"] = organization_name
        elif ent.label_ == 'GPE':
            location_name = ent.text
            faqs["Where are you from?"] = location_name

    # Additional personal questions based on keywords
    faqs.update(extract_additional_info(text))

    return faqs

# Helper function to extract additional information based on keywords
def extract_additional_info(text):
    faqs = {}
    keywords = {
        "hobbies": "What are your hobbies?",
        "food": "What's your favorite food?",
        "music": "What kind of music do you like?",
        "movies": "What are your favorite movies?",
        "dream vacation": "What's your dream vacation destination?",
    }

    for keyword, question in keywords.items():
        if keyword in text.lower():
            faqs[question] = extract_sentence_containing(text, keyword)

    return faqs

# Helper function to find a sentence containing a keyword
def extract_sentence_containing(text, keyword):
    doc = nlp(text)
    for sent in doc.sents:
        if keyword.lower() in sent.text.lower():
            return sent.text
    return "Answer not found in PDF."

# Example Usage
pdf_path = "user_profile.pdf"
pdf_text = extract_text_from_pdf(pdf_path)
faq_data = analyze_text_spacy(pdf_text)

# Asking the chatbot a question
def chatbot_response(question, faqs):
    return faqs.get(question, "I'm not sure how to answer that. Can you provide the answer?")

response = chatbot_response("Where are you from?", faq_data)
print(response)  # Output will depend on the content of your PDF

app = Flask(__name__)
# Home route to upload and analyze the PDF
@app.route('/', methods=['GET', 'POST'])
def home():
    faqs = None
    if request.method == 'POST':
        pdf_file = request.files['pdf_file']
        pdf_path = "uploaded_file.pdf"
        pdf_file.save(pdf_path)

        pdf_text = extract_text_from_pdf(pdf_path)
        faqs = analyze_text_spacy(pdf_text)
    
    return render_template('index.html', faqs=faqs)

# Chatbot route to answer questions
@app.route('/chat', methods=['POST'])
def chat():
    question = request.form['question']
    faqs = request.form['faqs']
    
    answer = faqs.get(question, "I'm not sure how to answer that. Can you provide the answer?")
    
    return render_template('index.html', faqs=faqs, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)