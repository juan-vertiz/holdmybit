from django.shortcuts import render

from .forms import ContactForm

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
    context = {}

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # TODO: Handle email sending
            context["success"] = True
            context["form"] = ContactForm()
        else:
            for field in form.errors:
                form[field].field.widget.attrs["class"] += " is-invalid"
            context["form"] = form
    else:
        context["form"] = ContactForm()

    return render(request=request, template_name="main/contact.html", context=context)