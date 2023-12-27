from django.shortcuts import render, redirect
from .models import User
from app.models import Question
# Home page / Time line
def home(request, user_id): 
    user = User.objects.get(id=user_id)
    print(user.first_name)
    return render(request,"index.html", {
        'user': user,
        'userName': user.first_name 
        })


def addQuestion(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        image_file = request.FILES.get('image_file')

        # Yeni bir Question nesnesi oluştur ve veritabanına kaydet
        question = Question(question_text=text, question_image=image_file)
        question.save()
    return render(request,'addQuestion.html')
    #    return HttpResponse('Question uploaded successfully!')
   # else:
     #   return HttpResponse('Please use POST method to upload.')

# Login page
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:    
            user = User.objects.filter(email=email).filter(password=password)
            if user:
                id = User.objects.get(email=email).id
                return redirect('home/' + str(id))
            else:
                return redirect('login')
        except:
            print("Failed to query from models")
            return render(request, "login.html")
    else:
        return render(request, "login.html")

# Register page
def register(request):
    if request.method == "POST":
        try: 
            first_name = request.POST.get("firstName")
            last_name = request.POST.get("lastName")
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = User(first_name=first_name, last_name=last_name, email=email, password=password)
            user.save()
            return redirect('home')
        except:
            # Burada bir hata mesaji gonderilecek. 
            return redirect('register')
    else:
        return render(request, "register.html")
    

# Lessons pages
def lessons(request):
    return render(request,"lessons.html")

# Lessons detial
def lessonDetails(request):
    return render(request,"details.html")

# Profile page
def profile(request, user_id):
    user = User.objects.get(id=user_id)

    return render(request, "profile.html", {
        'user':user
    })

def addQuestion(request):
    return render(request, "addQuestion.html")

def questionDetail(request):
    return render(request, "details.html")

def index(request):
    question = Question.objects.all()  # Tüm kişileri getir
    print(question)

    question_data = []
    for data in reversed(question):
        question_info = {
            'text': data.question_text,
            'image_url': data.question_image.url if data.question_image else None
        }
        question_data.append(question_info)

    return render(request, 'index.html', {'question': question_data})

def save_question(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        image_file = request.FILES.get('image_file')
        if username:
            data = Question(question_text=username,question_image=image_file)
            data.save()
            #return JsonResponse({'message': 'Username saved successfully'})
        #else:
            #return JsonResponse({'message': 'Username not provided'}, status=400)
    return render(request, 'addQuestion.html')