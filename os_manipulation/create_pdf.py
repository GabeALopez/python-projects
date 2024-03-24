from reportlab.pdfgen import canvas

def create_pdf_with_js(filename):
    # Create a canvas
    c = canvas.Canvas(filename)

    # Add content to the PDF
    c.drawString(100, 750, "This is a PDF with JavaScript")

    # Embed JavaScript into the content stream
    js_code = """
    var msg = "Hello from JavaScript!";
    app.alert(msg);
    """
    c.setFont("Helvetica", 12)
    c.drawString(50, 50, js_code)

    # Save the PDF
    c.save()

if __name__ == "__main__":
    filename = "example.pdf"
    create_pdf_with_js(filename)
    print(f"PDF file '{filename}' created successfully.")

