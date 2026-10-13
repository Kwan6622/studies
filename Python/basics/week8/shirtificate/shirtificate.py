# shirtificate.py
from fpdf import FPDF


def create_shirtificate(name: str):
    """Generates and saves the shirtificate PDF for a given name."""
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Title section
    pdf.set_font("Helvetica", style="B", size=24)
    # Using ln=1 moves the cursor to the next line automatically
    pdf.cell(0, 20, "CS50 Shirtificate", border=0, align="C", ln=1)

    # Shirt image centered horizontally (A4 width is 210mm; x=20 with w=170 centers it)
    pdf.image("shirtificate.png", x=20, y=60, w=170)

    # Name on shirt (White text -> RGB 255, 255, 255)
    pdf.set_font("Helvetica", style="B", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(0, 140)
    pdf.cell(210, 10, f"{name} took CS50", border=0, align="C")

    # Output result
    pdf.output("shirtificate.pdf")


def main():
    name = input("Please enter your name: ")
    create_shirtificate(name)


if __name__ == "__main__":
    main()