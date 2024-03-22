from django.shortcuts import render, redirect, get_object_or_404
from .forms import PropertyForm
from .models import Property

def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property_instance = form.save(commit=False)
            property_instance.save()

            # Handle photos
            photos = request.FILES.getlist('photos')
            for photo in photos:
                property_instance.photos.create(image=photo)

            # Handle videos
            videos = request.FILES.getlist('videos')  # Assuming your form allows multiple video uploads
            for video in videos:
                property_instance.videos.create(video_url=video)

            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'property_manager/add_property.html', {'form': form})

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property_manager/property_list.html', {'properties': properties})

def update_property(request, property_id):
    property_instance = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
            form.save()
            return redirect('property_list')
    else:
        form = PropertyForm(instance=property_instance)
    return render(request, 'property_manager/update_property.html', {'form': form})

def delete_property(request, property_id):
    property_instance = get_object_or_404(Property, pk=property_id)
    if request.method == 'POST':
        property_instance.delete()
        return redirect('property_list')
    return render(request, 'property_manager/confirm_delete.html', {'property': property_instance})


