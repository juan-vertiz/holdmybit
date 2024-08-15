from django.shortcuts import render

# Create your views here.
def index(request):
    """View function for Home page"""
    context = {
        "skills": {
            "Python": 4, 
            "PHP": 3,
            "JavaScript": 3,
            "Java": 3,
            "C/C++": 2,
            "HTML/CSS": 3,
            "Docker": 3,
            "Git": 3,
            "GitHub": 4
        },
        "languages": {
            "Spanish": 5,
            "English": 3
        }
    }
    return render(request=request, template_name="main/index.html", context=context)

def contact(request):
    """View function for Contact page"""
    
    return render(request=request, template_name="main/contact.html")