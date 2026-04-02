from django.shortcuts import render
from django.shortcuts import render, redirect
from django import forms
from .models import FaultReport
from django.shortcuts import render, redirect, get_object_or_404

class ReportForm(forms.ModelForm):
    class Meta:
        model = FaultReport
        # Added 'image' to the fields list here:
        fields = ['title', 'category', 'description', 'image', 'location_lat', 'location_lng']
        widgets = {
            'location_lat': forms.HiddenInput(),
            'location_lng': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Burst pipe on Main Rd'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'}), # Added widget for the image
        }

def dashboard(request):
    reports = FaultReport.objects.all().order_by('-created_at')
    return render(request, 'reports/dashboard.html', {'reports': reports})

def report_fault(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})

def delete_fault(request, fault_id):
    # Find the exact report by its ID, or return a 404 error if it doesn't exist
    report = get_object_or_404(FaultReport, id=fault_id)
    report.delete() # Delete it from the database
    return redirect('dashboard') # Send the user back to the updated feed

def report_fault(request):
    if request.method == "POST":
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            # THIS WILL PRINT THE HIDDEN ERROR TO YOUR TERMINAL
            print("FORM ERRORS:", form.errors) 
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})