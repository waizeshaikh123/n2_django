from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from baxify.models import Contact

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def blog(request):
    return render(request, 'blog.html')

def cal(request):
    # ca= ''
    # try:
    #     if request.method == "POST":
    #         val1 = eval(request.POST['val1'])
    #         val2 = eval(request.POST['val2'])
    #         opr = request.POST['opr']
    #         if opr == "+":
    #             ca = val1+val2
    #         elif opr == "-":
    #             ca = val1-val2
    #         elif opr == "*":
    #             ca = val1*val2
    #         elif opr == "/":
    #             ca = val1/val2
    # except:
    #     ca = 'invalid syntex...'
    if request.method == "POST":
        obj1 = eval(request.POST['obj1'])
        obj2 = eval(request.POST['obj2'])
        obj3 = eval(request.POST['obj3'])
        obj4 = eval(request.POST['obj4'])
        obj5 = eval(request.POST['obj5'])
        t = obj1+obj2+obj3+obj4+obj5
        p = t*100/500;
        if p >= 60:
            d = "First divi"
        elif p >= 48 :
            d = "Secound divi"
        elif p >= 35 :
            d = "Third divi"
        else:
            d = "Fale"
        
        data = {
            'total' : t, 
            'per' : p, 
            'div' : d
        }
        return render(request, 'cal.html',data)

    return render(request, 'cal.html')

def contact(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        sa = Contact(email=email, password=password)
        sa.save()
        print("Success save")        
        # return(HttpResponseRedirect, 'index.html')
    return render(request, 'contact.html')

# def submitForm(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         password = request.POST['password']
#         sa = Contact(email=email, password=password)
#         sa.save()
#         print("Success save")
#     return HttpResponse(request)