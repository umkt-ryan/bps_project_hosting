from django import forms 
from .models import Pegawai

class LoginForm(forms.Form):
    nip = forms.CharField(label='NIP')

from django import forms
from .models import Pegawai

class PegawaiForm(forms.ModelForm):
    class Meta:
        model = Pegawai
        fields = [
            'nama', 'jabatan', 'golongan', 'pangkat', 'pendidikan',
            'tim_kerja', 'tmt', 'angker_2024', 'foto'
        ]


class PegawaiTambahForm(forms.ModelForm):
    nip = forms.CharField(label='NIP')

    class Meta:
        model = Pegawai
        fields = ['nip', 'nama', 'jabatan', 'foto', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
