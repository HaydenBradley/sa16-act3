from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    context = {
        'biography': 'I am 22 years old and am currently studying computer science. I was born and raised in Memphis, Tn',
        'education_background': 'I went to grahamwood elementary, then moved onto White Station Highschool, and am currently enrolled at University of Memphis',
        'skills': ['Python', 'Ruby', 'Django'],  
        'achievements': 'I have acheived a highschool diploma and hopefully soon a bachelors degree',
    }
    return render(request, 'about.html', context)

def work(request):
    projects = [
        {
            'description': 'This is a project I made in 4081. The goal was to allow users to add/delete/edit test questions',
            'image_url': 'sa-16.png',
            'accomplishments': 'I was able to accomplish a fully functional webpage with edit/delete/new buttons with multiple pages',
            'technologies': ['Ruby', 'VS code', 'Ubuntu Terminal'],
        },
    ]
    return render(request, 'work.html', {'projects': projects})
def contact(request):
    contact_info = {
        'email': 'bradleyhayden6932@gmail.com',
        'phone': '9015032395',

    }
    return render(request, 'contact.html', {'contact_info': contact_info})