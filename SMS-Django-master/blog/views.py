from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .models import Student, About, Feedback, Contact, Insert, Update, Delete
from django.contrib.auth.models import auth, User
from django.contrib import messages

# from location_field.models.plain import PlainLocationField


def index(request):
    obj = Student.objects.all()
    data = ""
    if request.method == "POST":
        standard = request.POST["std"]
        roll = int(request.POST["rollno"])
        image = request.POST["img"]
        for i in obj:
            stand = str(i.standard)
            roll_no = int(i.roll)
            images = str(i.image)
            if standard == stand and roll == roll_no and image == images:
                data = i
            else:
                res = "No Record Found..."
        return render(request, "blog/index.html", {"data": data, "res": res})
    return render(request, "blog/index.html")


def insert(request):
    # roll=request.POST['rollno']
    if request.method == "POST":
        rollno = request.POST["rollno"]
        name = request.POST["name"]
        city = request.POST["city"]
        contact = request.POST["contact"]
        std = request.POST["std"]
        img = request.POST["img"]
        user = Insert.objects.create(
            name=name, rollno=rollno, city=city, contact=contact, std=std, img=img
        )
        user.save()
        print("User created")
        return redirect("/")
    return render(request, "blog/insert.html")


def update(request):
    return render(request, "blog/update.html")


def delete(request):
    return render(request, "blog/delete.html")


def about(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        enquiry = request.POST["enquiry"]
        phone = request.POST["phone"]
        message = request.POST["message"]

        user = About.objects.create(
            name=name, email=email, enquiry=enquiry, phone=phone, message=message
        )
        user.save()
        print("User created")
        return redirect("/")
    return render(request, "blog/about.html")


def service(request):
    return render(request, "blog/service.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        mobile = request.POST["mobile"]
        messsage = request.POST["message"]
        user = Contact.objects.create(name=name, email=email, mobile=mobile, messsage=messsage)
        user.save()
        print("User created")
        return redirect("/")
    return render(request, "blog/contact.html")


def feedback(request):
    if request.method == "POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]

        title = request.POST["title"]
        message = request.POST["message"]

        user = Feedback.objects.create(
            fname=fname, lname=lname, email=email, message=message, title=title
        )
        user.save()
        print("User created")
        return redirect("/")
    return render(request, "blog/feedback.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exists !")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exists !")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                )
                user.save()
                print("User created")
                return redirect("login")
        else:
            messages.info(request, "Password does not match !")
            return redirect("register")

    else:
        return render(request, "blog/register.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Username / Password !")
            return redirect("login")
    else:
        return render(request, "blog/login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def dashboard(request):
    return render(request, "blog/dashboard.html")
