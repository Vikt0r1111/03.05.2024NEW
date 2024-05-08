from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = ContactForm()
    return render(request, 'my_app/contact_form.html', {'form': form})

def success_page(request):
    return render(request, 'my_app/success_page.html')