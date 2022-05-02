from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import Student, About, Feedback, Contact
from django.contrib.auth.models import auth, User
from django.contrib import messages

# from location_field.models.plain import PlainLocationField

def index(request):
    obj = Student.objects.all()
    data = ""
    if request.method == "POST":
        roll = int(request.POST["roll"])
        standard = request.POST["standard"]
        for s in obj:
            stand = str(s.standard)
            roll_no = int(s.roll)
            
            if  roll == roll_no and  standard == stand  :
                data = s
            else:
                  return HttpResponse ("<h1>No Record Found...</h1>")
        return render(request, "blog/index.html", { "data": data} )
    return render(request, "blog/index.html")


def student(request):
    if request.method == "POST":
        # id=request.POST['id']
        roll = request.POST["roll"]
        name = request.POST["name"]
        city = request.POST["city"]
        contact = request.POST["contact"]
        standard = request.POST["standard"]
        img = request.FILES["img"]
        user = Student.objects.create(
         roll=roll, name=name, city=city, contact=contact, standard=standard, img=img
        )
        user.save()
        print("User created")
        return redirect("blog/student.html")
    return render(request, "blog/student.html")
# def search(request):
#     if request.method == "POST":
#        std = request.POST["std"]
#        stdname = request.POST["stdname"]
#        Student = Student.objects.filter(name__contains=stdname)
#        user =  search.objects.create(
#            std=std, stdname=stdname
#         )
#        user.save()
#     #    print("User created")
#        return render(request, "blog/update.html", {'stdname':stdname, "name":Student})
#     else:
#        return render(request, "blog/update.html")


def update(request):
	obj= Student.objects.all()
	obj=Student.objects.order_by().values('standard').distinct()
    # obj=Student.objects.get(name=req.POst>get('name'))
	if request.method == 'POST':
		data=[]
		s=1
		standard=request.POST['standard']
		name= request.POST['name']
		stu=Student.objects.filter(standard=standard)
		for i in stu:
			if name in i.name:
				data.append((s,i))
				s+=1
		return render(request,'blog/update.html',{'data':data})
	return render(request,'blog/update.html',{'obj':obj})



# def delete(request):
# 	obj= Student.objects.all()
# 	obj=Student.objects.order_by().values('standard').distinct()
# 	if request.method == 'POST' and 'delete' in request.POST:
# 		data=''
# 		standard=request.POST['standard']
# 		name= request.POST['name']
# 		st=Student.objects.filter(standard=standard,name=name)
# 		if st.exists():
# 			data=st.first().delete()
# 		else:
# 			HttpResponse("<h1>Data not found</h1>")
# 		return render(request,'blog/delete.html',{'data':data})
# 	return render(request,'blog/delete.html',{'obj':obj})


    
def delete(request):
	obj= Student.objects.all()
	obj=Student.objects.order_by().values('standard').distinct()
	if request.method == 'POST' and 'submit' in request.POST:
		data=''
		standard=request.POST['standard']
		name= request.POST['name']
		stu=Student.objects.filter(standard=standard,name=name)
		if stu.exists():
			data=stu.first()
		else:
			return HttpResponse("<h1>No Data Found</h1>")
		return render(request,'blog/delete.html',{'data':data})
	return render(request,'blog/delete.html',{'obj':obj})

# def delete(request):
#     context ={}
#     obj = get_object_or_404(Student)
#     if request.method =="POST":
#         obj.delete()
#         return HttpResponseRedirect('blog/delete.html')
#     return render(request, 'blog/delete.html', context)




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
