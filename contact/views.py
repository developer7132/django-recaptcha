from django.shortcuts import render, HttpResponse
from .forms import ContactForm
  
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            return HttpResponse(f"Yay! you are human. email: {form.cleaned_data['email']}, password: {form.cleaned_data['password']}")
        else:
            return HttpResponse("OOPS! Bot suspected.")
            
    else:
        form = ContactForm()
          
    return render(request, 'contact.html', {'form':form})