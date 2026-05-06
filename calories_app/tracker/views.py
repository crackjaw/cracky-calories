from django.shortcuts import render, redirect, get_object_or_404
from .models import CalorieEntry
from .forms import CalorieEntryForm
from django.db.models import Sum

def index(request):
    entries = CalorieEntry.objects.all().order_by('-date')

    # Group by date for totals
    daily_totals = (
        CalorieEntry.objects.values('date')
        .annotate(total=Sum('calories'))
        .order_by('-date')
    )

    if request.method == 'POST':
        form = CalorieEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CalorieEntryForm()

    context = {
        'entries': entries,
        'daily_totals': daily_totals,
        'form': form,
    }
    return render(request, 'tracker/index.html', context)

def delete_entry(request, entry_id):
    entry = get_object_or_404(CalorieEntry, id=entry_id)
    if request.method == 'POST':
        entry.delete()
        return redirect('index')
    return render(request, 'tracker/confirm_delete.html', {'entry': entry})
