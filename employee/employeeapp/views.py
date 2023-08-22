from django.shortcuts import render
from .models import Employee
from django.http import HttpResponse

# Create your views here.
def home(request):
 return render(request,"employee.html")

def addemployee(request):
   try:
      Name=request.POST['fname']
      Address=request.POST['address']
      emplist=Employee(name=Name,address=Address)
      emplist.save()
      return render(request,"employee.html",{"msg":"Employee added"})
   except Exception as e:
     print(e)
     return render(request,"employee.html",{"msg":"Employee cannot be added"})
   
def display(request):
  empdtls=Employee.objects.all()
  return render (request,"employee.html",{'emp':empdtls})

# delete by name
# def delete(request):
#   empname=request.POST['fname']
#   empdtld=Employee.objects.filter(name=empname)
#   empdtld.delete()
#   return render(request,'employee.html',{"msg":"Successfully deleted"})

# delete by id
def empdelete(request,eid):
  empdtls=Employee.objects.get(id=eid)
  empdtls.delete()
  return HttpResponse("Deleted")

#update using filter
def update(request):
 try: 
     oldname=request.POST['oldname']
     newname=request.POST['newname']
     emp=Employee.objects.filter(name=oldname)
     if emp.exists():
       emp.update(name=newname)
       return render(request,"employee.html",{'msg':'updated'})
     else:
       return render(request,"employee.html",{'msg':'Name not found'})
 except Exception as e:
   return render(request,"employee.html",{'msg':'not updated'}) 
 
# # update using get
# def 
# empid=request.POST['empid']
# newname=request.POST['newname']

 
  
