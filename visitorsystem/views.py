from pyexpat.errors import messages
from django.shortcuts import render,redirect
from login.models import Newuser
from visitor.models import Visitor,Department
from django.contrib import messages
from datetime import datetime
from datetime import date, datetime
from django.utils.dateparse import (
    parse_date, parse_datetime, parse_duration, parse_time,
)
now = datetime.now()
def indexpage(request):
    return render(request,'index.html')
def Userreg_view(request):
    if request.method=='POST':
        Username=request.POST['Username']
        email=request.POST['email']
        Password=request.POST['Password']
        Newuser(Username=Username, email=email,Password=Password).save()
        messages.success(request,"The New user "+request.POST['Username']+ "is saved successfully")
        return render(request,"Signup.html")
    else:
        return render(request, "Signup.html")

def loginpage(request):
    if request.method=="POST":
        try:
            UserDetails=Newuser.objects.get(email=request.POST['email'], Password=request.POST['Password'])
            print("Username",UserDetails)
            request.session['email']=UserDetails.email
            return render (request, 'Index.html')
        except Newuser.DoesNotExist as e:
             messages.success(request,"Username / Password Invaid ")
    return render(request, "login.html")
def logout(request):
    try:
        del request.session['email']
    except:
        return render (request,'index.html')
    return render (request,'index.html')
def view(request):
    User=Newuser.objects.all()
    print(User)
    return render(request, "view.html", {'User':User})

def view_dept(request):
    Dept=Department.objects.all()
    return render(request, "view_dept.html", {'Dept':Dept})
def Visitorentry_view(request):
    

    if request.method=='POST':
        
        
        Visitor_Name=request.POST.get('Visitor Name')
        Visitor_CNIC=request.POST.get('Visitor CNIC')
        Visitor_Mobile=request.POST.get('Visitor Mobile')
        Visitor_Company=request.POST.get('Visitor Company')
        Visitor_Address=request.POST.get('Visitor Address')
        Meeting_With=request.POST.get('Meeting With')
        Department_id=request.POST.get('Department_ID')
        Department_Id=Department.objects.get(Department_ID=Department_id)
        #print(Department_ID)
        #Department_ID=Department_Id
        Check_In=datetime.now()
        #Check_Out=request.POST.get('Check Out')
        Purpose_Of_Meeting=request.POST.get('Purpose of Meeting')
        Visitor.objects.create(Visitor_Name=Visitor_Name, Visitor_CNIC=Visitor_CNIC,Visitor_Mobile=Visitor_Mobile, Visitor_Company=Visitor_Company, Visitor_Address=Visitor_Address,Check_In=Check_In,Meeting_With=Meeting_With,Department_ID=Department_Id,Purpose_Of_Meeting=Purpose_Of_Meeting)
        messages.success(request,"The New visitor entry "+request.POST['Visitor Name']+ "is saved successfully")
        return redirect("/viewvisitor")
        #dispDept=Department.objects.all()
        #return render(request,'visitorentry.html',{'Department':dispDept})
        
    else:
        dispDept=Department.objects.all()
        return render(request,'visitorentry.html',{'Department':dispDept})

def CheckOut_visitor_entry(request, id):
    visitor=Visitor.objects.get(Visitor_ID=id)
    visitor.Check_Out=datetime.now()
    visitor.save()
    messages.info(request,"Updated successfully")
    return redirect("/viewvisitor")

        

def DeptEntry_view(request):
    if request.method=='POST':
        
        Department_Name=request.POST.get('Department_Name')
        Department.objects.create(Department_Name=Department_Name)
        messages.success(request,"The New department "+request.POST['Department_Name']+ "is saved successfully")
        return render(request,"deptentry.html")
        return redirect("/viewdept")
        # return render(request,"view.html")
    else:
        return render(request, "deptentry.html")

def view_visitor(request):
    visitor=Visitor.objects.all()
    return render(request, "view_visitor.html", {'visitor':visitor})

def delete(request, id):
    User=Newuser.objects.get(User_ID=id)
    User.delete()
    return redirect("/view")

def edit(request, id):
    User=Newuser.objects.get(User_ID=id)
    #pi=User.objects.get(pk=id)
    return render(request,'edit.html',{'User' :User})
    

def update(request, id):
    User=Newuser.objects.get(User_ID=id)
    User.Username = request.POST['Username']
    User.email=request.POST['email']
    User.Password=request.POST['Password']
    User.save()
    messages.info(request,"Updated successfully")
    return redirect("/view")



def delete_visitor(request, id):
    visitor=Visitor.objects.get(Visitor_ID=id)
    visitor.delete()
    return redirect("/viewvisitor")

def edit_visitor(request, id):
    visitor=Visitor.objects.get(Visitor_ID=id)
    dept=Department.objects.all()
    #pi=User.objects.get(pk=id)
    return render(request,'edit_visitor.html',{'Visitor' :visitor,'dept':dept})


    

def update_visitor(request, id):
    visitor=Visitor.objects.get(Visitor_ID=id)
    visitor.Visitor_Name=request.POST['Visitor Name']
    visitor.Visitor_CNIC=request.POST['Visitor CNIC']
    visitor.Visitor_Mobile=request.POST['Visitor Mobile']
    visitor.Visitor_Company=request.POST['Visitor Company']
    visitor.Visitor_Address=request.POST['Visitor Address']
    visitor.Meeting_With=request.POST['Meeting With']
    Department_id=request.POST.get('Department_ID')
    Department_Id=Department.objects.get(Department_ID=Department_id)
    visitor.Department_ID=Department_Id
    
    visitor.Check_In=datetime.now()
    visitor.Check_Out=datetime.now()

    visitor.Purpose_Of_Meeting=request.POST['Purpose_Of_Meeting']
    visitor.save()
    messages.info(request,"Updated successfully")
    return redirect("/viewvisitor")

def delete_dept(request, id):
    Dept=Department.objects.get(Department_ID=id)
    Dept.delete()
    return redirect("/viewdept")

def edit_dept(request, id):
    Dept=Department.objects.get(Department_ID=id)
    #pi=User.objects.get(pk=id)
    return render(request,'edit_dept.html',{'Dept' :Dept})
    

def update_dept(request, id):
    Dept=Department.objects.get(Department_ID=id)
    Dept.Department_Name = request.POST['Department_Name']
    Dept.save()
    messages.info(request,"Updated successfully")
    return redirect("/viewdept")

