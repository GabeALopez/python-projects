import subprocess

def generate_html_with_js(filename):
    # HTML content with embedded JavaScript
    html_content = """
    <html>
    <head>
        <script type="text/javascript">
            // Function to execute when PDF is opened
            function executeOnOpen() {
                app.alert("Hello from JavaScript!");
            }
            // Call executeOnOpen function when the document is opened
            this.openDoc({cPath: this.path, oDoc: this, cJS: 'executeOnOpen();'});
        </script>
    </head>
    <body>
        <h1>This is an HTML page with JavaScript</h1>
    </body>
    </html>
    """
    
    # Write HTML content to file
    with open(filename, 'w') as f:
        f.write(html_content)

def convert_html_to_pdf(html_filename, pdf_filename):
    # Call wkhtmltopdf to convert HTML to PDF
    subprocess.run(['wkhtmltopdf', html_filename, pdf_filename])

if __name__ == "__main__":
    html_filename = "example.html"
    pdf_filename = "example.pdf"
    
    # Generate HTML file with JavaScript
    generate_html_with_js(html_filename)
    
    # Convert HTML to PDF
    convert_html_to_pdf(html_filename, pdf_filename)
    
    print(f"PDF file '{pdf_filename}' created successfully.")
