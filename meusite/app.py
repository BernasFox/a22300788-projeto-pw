from flask import Flask, request, send_file
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meu Site</title>
        <style>
            /* Estilos CSS */
        </style>
    </head>
    <body>
        <!-- Layout do cabeçalho -->
        <header>
            <h1>Sobre Mim</h1>
        </header>
        <!-- Conteúdo da página -->
        <div id="content" style="position: relative; width: 100%; height: 0; padding-top: 141.4286%; padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden; border-radius: 8px; will-change: transform;">
            <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
                src="https://www.canva.com/design/DAGCaKpqcBA/V9xgU03RIOccfSNa6ybY8Q/view?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
            </iframe>
        </div>
        <button id="downloadPDF">Imprimir como PDF</button>

        <!-- Script JavaScript para baixar o PDF -->
        <script>
            document.getElementById("downloadPDF").addEventListener("click", function() {
                // Faça uma solicitação GET para o servidor Flask
                window.location.href = "/download_template";
            });
        </script>
    </body>
    </html>
    """

@app.route('/download_template')
def download_template():
    # URL do template do Canva
    canva_url = "https://www.canva.com/design/DAGCaKpqcBA/V9xgU03RIOccfSNa6ybY8Q/view"

    # Solicita o conteúdo do Canva
    response = requests.get(canva_url)

    # Retorna o conteúdo como um arquivo PDF
    return send_file(response.content, mimetype='application/pdf', as_attachment=True, attachment_filename='meu_template.pdf')

if __name__ == '__main__':
    app.run(debug=True)
