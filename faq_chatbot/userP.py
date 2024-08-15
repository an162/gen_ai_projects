from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_user_profile_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, height - 100, "User Profile")

    # User Description
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 150, "Name: Lina Wafaa")
    c.drawString(100, height - 170, "Age: 25")
    c.drawString(100, height - 190, "Location: Oran, Algeria")
    
    # Common Answers
    c.drawString(100, height - 230, "Hobbies:")
    c.drawString(120, height - 250, "I enjoy hiking, reading, and painting.")
    
    c.drawString(100, height - 270, "Favorite Food:")
    c.drawString(120, height - 290, "I love Italian cuisine, especially pasta.")
    
    c.drawString(100, height - 310, "Favorite Music:")
    c.drawString(120, height - 330, "I'm a fan of classical music and jazz.")

    c.drawString(100, height - 350, "Career:")
    c.drawString(120, height - 370, "I'm currently working in remote sensing and programming.")

    c.save()

# Generate the PDF
create_user_profile_pdf("user_profile.pdf")

