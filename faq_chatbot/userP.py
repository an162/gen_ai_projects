from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

def create_user_profile_pdf(output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()

    # Define the content of the paragraph
    content = """
    <b>User Profile</b><br/><br/>
    My name is <b>Lina Wafaa</b>, and I am 25 years old, living in the beautiful city of Oran, Algeria. I have a deep passion for <b>hiking, reading, and painting</b>, which are some of my favorite hobbies. When it comes to food, I can't resist <b>Italian cuisine</b>, especially pasta—it’s simply delicious! Music is another love of mine, and I particularly enjoy listening to <b>classical music and jazz</b>.<br/><br/>
    Professionally, I am currently involved in <b>remote sensing and programming</b>, which allows me to explore new technologies and innovate in my field.
    """

    # Create a paragraph object
    paragraph = Paragraph(content, styles['BodyText'])

    # Build the PDF with the paragraph
    doc.build([paragraph])

# Generate the PDF
create_user_profile_pdf("user_profile.pdf")
