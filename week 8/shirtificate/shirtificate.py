from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

def create_shirtificate(name):
    # Create instance of FPDF class
    pdf = PDF(orientation='P', unit='mm', format='A4')

    # Add a page
    pdf.add_page()

    # Set title
    pdf.set_font("Arial", "B", 30)
    pdf.cell(0, 10, "CS50 Shirtificate", 0, 1, "C")

    # Add shirt image
    pdf.image("shirtificate.png", x=0, y=60, w=210)  # Adjust x, y, and w as needed

    # Add user's name on top of the shirt image
    pdf.set_xy(0, 140)  # Adjust y as needed
    pdf.set_font("Arial", "B", 30)
    pdf.set_text_color(255, 255, 255)  # White color
    pdf.cell(210, 10, name, 0, 1, "C")

    # Output the PDF to a file
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    # Prompt user for their name
    name = input("Enter your name: ")
    # Create the shirtificate
    create_shirtificate(f"{name} took CS50")
