from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("""
        <html>
            <body>
                <h1>hello 这是第一个视图</h1>
            </body>
        </html>
    """)
