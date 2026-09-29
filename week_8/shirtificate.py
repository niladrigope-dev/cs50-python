from fpdf import FPDF


def main():
    name = input("Name: ")

    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()

    
    pdf.set_font("helvetica", "B", 28)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C")


    pdf.image("shirtificate.png", x=35, y=55, w=140)


    pdf.set_font("helvetica", "B", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_xy(35, 140)
    pdf.cell(140, 20, name, align="C")

    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
