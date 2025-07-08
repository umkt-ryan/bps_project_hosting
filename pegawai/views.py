from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Pegawai
from .forms import LoginForm, PegawaiTambahForm, PegawaiForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nip = form.cleaned_data['nip']
            try:
                user = Pegawai.objects.get(nip=nip)
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('profil')
            except Pegawai.DoesNotExist:
                form.add_error('nip', 'NIP tidak ditemukan.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@staff_member_required
def tambah_pegawai_view(request):
    if request.method == 'POST':
        form = PegawaiTambahForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin:index')
    else:
        form = PegawaiTambahForm()
    return render(request, 'tambah_pegawai.html', {'form': form})


@login_required
def profil_view(request):
    return render(request, 'profil.html', {'pegawai': request.user})


@login_required
def edit_profil_view(request):
    user = request.user
    if request.method == 'POST':
        form = PegawaiForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = PegawaiForm(instance=user)
    return render(request, 'edit_profil.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
