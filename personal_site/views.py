# personal_site/views.py
from django.shortcuts import render

def home(request):
    context = {
        'name': 'P NAGASRI SREYA',
        'email': 'punnavajhalanagasrisreya@gmail.com',
        'phone': '8309678389',
        'hobbies': 'Sports(basketball), Painting, Music',
        'bio': 'I am a B-Tech second year student who is always enthusiastic about learning, I am a team player who understands and supports the insight and view of others. I take keen intrest in programing and have participated in many technical fests conducted by our University. I have also participated in many technical projects that help us in our day to day lives.',
        'LinkedIn':' www.linkedin.com/in/punnavajhala-nagasrisreya-02521b32b',
        'GitHub':' https://github.com/nagasrisreya'
    }
    return render(request, 'home.html', context)

# Resume view
def resume(request):
    context = {
        'name': 'P NAGASRI SREYA',
        'experience': [
            {'position': 'Web Developer', 'Techinical_Fests': 'AVINYA and IVERNA', 'years': '2023 - 2027'},
            {'position': 'Web Developer', 'Techinical_Fests': 'EDU Guide', 'years': '2023 - 2027'},
            {'position': 'Team member', 'Techinical_Fests': 'Blind man sick', 'years': '2023 - 2027'},
            {'position': 'Team member', 'Techinical_Fests': 'Sleep detector in Car', 'years': '2023 - 2027'}
            
        ],
        'education': [
            {'degree': 'B - Tech in Artificial Inteigence and Data Science', 'institution': 'KL University', 'years': '2023 - 2027'},
        ],
        'skills': ['Python', 'Django', 'JavaScript', 'HTML', 'CSS']
    }
    return render(request, 'resume.html', context)

