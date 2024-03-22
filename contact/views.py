from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add additional logic here like sending emails, etc.
            return render(request, 'contact/thanks.html')  # Render a thank you page after form submission
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})