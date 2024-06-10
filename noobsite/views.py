from django.http import HttpResponse

def index_view(request):
    site = """
    <html>
        <head>
            <style>
                body {
                    background-color: #f0f0f0;
                }
            </style>
        </head>
        <body>
        <!-- Fiz deste modo, pois existem browsers que caso o site nãp possua css(ou style) não apresentão corretamente o site -->
            <p> Olá n00b, esta é a página web mais básica do mundo!</p>
        </body>
    </html>
    """


    return HttpResponse(site)