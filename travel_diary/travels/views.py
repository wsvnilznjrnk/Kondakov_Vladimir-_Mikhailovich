from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import TravelEntry
from .forms import TravelEntryForm

@login_required
def create_travel_entry(request):
    if request.method == 'POST':
        form = TravelEntryForm(request.POST, request.FILES)
        if form.is_valid():
            travel_entry = form.save(commit=False)
            travel_entry.user = request.user
            travel_entry.save()
            return redirect('travel_list')
    else:
        form = TravelEntryForm()
    return render(request, 'travels/create_travel_entry.html', {'form': form})

def travel_list(request):
    travels = TravelEntry.objects.all()
    return render(request, 'travels/travel_list.html', {'travels': travels})

def travel_detail(request, travel_id):
    travel = get_object_or_404(TravelEntry, id=travel_id)
    return render(request, 'travels/travel_detail.html', {'travel': travel})
