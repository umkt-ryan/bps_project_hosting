from django.contrib import admin
from .models import Pegawai, BackgroundSetting

admin.site.site_header = "Admin KOMAS"
admin.site.site_title = "Dashboard KOMAS"
admin.site.index_title = "Selamat datang di sistem KOMAS"

@admin.register(Pegawai)
class PegawaiAdmin(admin.ModelAdmin):
    list_display = ('nip', 'nama', 'jabatan', 'golongan', 'pangkat', 'pendidikan')
    search_fields = ('nip', 'nama', 'jabatan')

@admin.register(BackgroundSetting)
class BackgroundSettingAdmin(admin.ModelAdmin):
    list_display = ('background',)
