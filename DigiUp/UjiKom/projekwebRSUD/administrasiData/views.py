from django.shortcuts import render, get_object_or_404, redirect
from .models import DataPasien
from .forms import DataPasienForm 

def beranda(request):
    return render(request, 'beranda.html')

def view_data_pasien(request, noRekamMedis):
    data = get_object_or_404(DataPasien, noRekamMedis=noRekamMedis)
    return render(request, 'view_data_pasien.html', {'Data': data})

def add_data_pasien(request):
    if request.method == 'POST':
        form = DataPasienForm(request.POST)
        if form.is_valid():
            new_data = form.save()
            return redirect('view_data_pasien', noRekamMedis=new_data.noRekamMedis)
    else:
        form = DataPasienForm()
    return render(request, 'add_data_pasien.html', {'form': form})

def edit_data_pasien(request, noRekamMedis):
    data = get_object_or_404(DataPasien, noRekamMedis=noRekamMedis)
    if request.method == 'POST':
        form = DataPasienForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('beranda')
    else:
        form = DataPasienForm(instance=data)
    return render(request, 'edit_data_pasien.html', {'form': form, 'Data': data})

def delete_data_pasien(request, noRekamMedis):
    data = get_object_or_404(DataPasien, noRekamMedis=noRekamMedis)
    if request.method == 'POST':
        data.delete()
        return redirect('beranda')
    return render(request, 'delete_data_pasien.html', {'Data': data})
