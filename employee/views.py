from django.shortcuts import render,HttpResponse,redirect
from.models import Employee


# Create your views here.
def emp_home(request):
  em=Employee.objects.all()
  context={
     'emps': em
  }
  print(context)
  return render(request,'emp_home.html',context)

def view_emp(request):
   em=Employee.objects.all()
   context={
     'emps': em
   }
   print(context)
   return render(request,'view_emp.html',context)



def delete_emp(request,emp_id=0):
  if emp_id:
    print("abc")
    try:
      emp_to_be_return=Employee.objects.get(id=emp_id)
      print("hello")
      emp_to_be_return.delete()
      return redirect('emp_home')
    except:
      return HttpResponse('Please enter a valid EMP_ID')
  emps=Employee.objects.all()
  context ={
    'emps':emps
  }
  print(context)
  return render(request,'delete_emp.html',context)

def add_emp(request):
    if request.method == "POST":
        
        # Process the form data here

        print("add employee")

        #data fetch
       
        name=request.POST['emp_name']
        address=request.POST['emp_address']
        emp_id=int(request.POST['emp_id'])
        phone=int(request.POST['emp_phone'])
        working = request.POST.get('emp_working', 'off') == 'on'
        department=request.POST['emp_department']

        # create model object and se the data
   
        new_employee=Employee(name=name,emp_id=emp_id,phone=phone,address=address,department=department,working=working)

        # save the data 

        new_employee.save()


        # Redirect to emp_home or another valid URL
        return redirect('emp_home')  # This assumes you have a named URL 'emp_home'
    return render(request, 'add_emp.html')


def update_emp(request,emp_id=0):
   emp=Employee.objects.get(id=emp_id)
   print('update page is open')
   if request.method == "POST":
      name=request.POST['emp_name']
      address=request.POST['emp_address']
      emp_id=int(request.POST['emp_id'])
      phone=int(request.POST['emp_phone'])
      working = request.POST.get('emp_working', 'off') == 'on'
      department=request.POST['emp_department']

      emp.name = name
      emp.emp_id = emp_id
      emp.phone = phone
      emp.address = address
      emp.department = department
      emp.working = working
      emp.save()
      return redirect('emp_home')
   else:
      context ={
         'emp':emp
      }
      return render(request,'update_emp.html',context)

def filter_emp(request):
   print("runing the filter command")

   if request.method == 'POST':
      name=request.POST.get('empname')
      print("running the post method")
      emp_id=request.POST.get('empid')
      emps=Employee.objects.all()
      if name:
          emps=emps.filter(name__icontains=name)
          print("check")

      if emp_id:
          emps=emps.filter(emp_id=emp_id) 
      context ={
        'emps': emps
      }
      print("umesh")
      return render(request,'emp_home.html',context)
   
   elif request.method=='GET':
      print("get filter ")
      return render(request,'filter_emp.html')
   else:
      print("umesh")
      return HttpResponse("An exception Occured ")
   

 
   