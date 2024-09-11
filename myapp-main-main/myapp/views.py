from django.shortcuts import render,redirect
from .forms import LoginForm

def index(request):
	return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()  # บันทึกข้อมูลลง MySQL
            return redirect('success_page')  # เมื่อบันทึกเสร็จแล้วไปที่หน้าถัดไป
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

