from django.shortcuts import render

def home_page(request):
    ctx = {
        'footer_class': 'footer-section-three'
    }

    return render(request, 'pages/home.html', ctx)

def contact_page(request):
    ctx = {
        'footer_class': 'footer-section-five position-relative overflow-hidden'
    }

    return render(request, 'pages/contact.html', ctx)
