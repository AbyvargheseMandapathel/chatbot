import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .chatbot import chatbot
from .models import SliderImage, Event, Course, Teachers, Announcements


# # Define the URL of the webpage to scrape for FAQs
# FAQ_URL = 'https://chatbot--akashvinod098.repl.co/'

# # Send a GET request to the FAQ URL and parse the HTML response
# faq_response = requests.get(FAQ_URL)
# faq_soup = BeautifulSoup(faq_response.content, 'html.parser')

# # Find all the FAQ cards on the page
# faq_cards = faq_soup.find_all('div', class_='card')

# # Define a function to search for an answer to a question in the FAQ cards
# def search_faq(question, faq_cards):
#     # Loop over each FAQ card
#     for card in faq_cards:
#         # Get the question and answer text from the card
#         card_question = card.find('a').text
#         card_answer = card.find('p').text
#         # Check if the user's query is in the card's question
#         if question.lower() in card_question.lower():
#             return card_answer

#     # Loop over each FAQ card again to check the tags
#     for card in faq_cards:
#         # Get the tags from the card
#         tags = card.find_all('span', class_='tags')
#         tag_names = set([tag.text.strip() for tag in tags])
#         # Check if any tag matches the user's query words
#         for word in question.split():
#             if word.lower() in tag_names:
#                 return card_answer

#     # If no matching question or tag is found, return None
#     return None

# # Define a function to handle user input and return a response
# def handle_input(user_input, faq_cards):
#     answer = search_faq(user_input, faq_cards)
#     if answer:
#         return answer
#     else:
#         # Break down user input into individual words
#         query_words = user_input.lower().split()
#         # Loop over each FAQ card to check the tags against the query words
#         for card in faq_cards:
#             # Get the tags from the card
#             tags = card.find_all('span', class_='tags')
#             tag_names = set([tag.text.strip() for tag in tags])
#             # Check if any tag matches the query words
#             if any(word in tag_names for word in query_words):
#                 return card.find('p').text
        
#         return "I'm sorry, I don't have an answer for that."



    



def home(request):
    sliders = SliderImage.objects.all()
    events = Event.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', {'sliders': sliders, 'events': events, 'courses': courses})

def index(request):
    return render(request, 'home.html')

def get_response(request):
    if request.method == 'GET':
        message = request.GET.get('message')
        if message:
            response = chatbot(request, message)
            return HttpResponse(response)
        else:
            return HttpResponse('Please provide a message')
    else:
        return HttpResponse('Invalid request method')


def courses(request):
    courses = Course.objects.all()
    paginator = Paginator(courses, 9) # Show 9 courses per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'courses.html', {'courses': page_obj})

def events(request):
    event_list = Event.objects.all()
    paginator = Paginator(event_list, 3) # 3 events per page
    page = request.GET.get('page')
    events = paginator.get_page(page)
    return render(request, 'event.html', {'events': events})

def teachers(request):
    teachers_list = Teachers.objects.all()
    paginator = Paginator(teachers_list, 10) # Show 10 teachers per page
    page = request.GET.get('page')
    teachers = paginator.get_page(page)
    return render(request, 'teachers.html', {'teachers': teachers})

def announcements(request):
    announcements_list = Announcements.objects.all().order_by('-date', '-time')
    paginator = Paginator(announcements_list, 10)  # 10 items per page
    page = request.GET.get('page')
    announcements_page = paginator.get_page(page)
    context = {'announcements_page': announcements_page}
    return render(request, 'announcements.html', context)

def teacher_details(request, teacher_id):
    teacher = get_object_or_404(Teachers, pk=teacher_id)
    return render(request, 'teacher_details.html', {'teacher': teacher})



def course_detail(request, course_name):
    course = get_object_or_404(Course, name=course_name)
    return render(request, 'course_details.html', {'course': course})

def events_detail(request, events_name):
    event = get_object_or_404(Event, name=events_name)
    return render(request, 'events_details.html', {'event': event})

def faq(request):
    return render(request, 'faq.html')