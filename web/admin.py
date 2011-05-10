from web.models import Aplikasi
from web.models import Kategori
from django.conf import settings
from django.contrib import admin

class AplikasiAdmin(admin.ModelAdmin):
	fields = ['nama_aplikasi', 'id_kategori', 'keterangan', 'gambar_aplikasi', 'link_unduh']
	list_filter = ['id_kategori', 'tanggal_ditambahkan']
	date_hierarchy = 'tanggal_ditambahkan'
	list_display = ('nama_aplikasi', 'keterangan', 'id_kategori', 'tanggal_ditambahkan', 'link_unduh', 'gambar_aplikasi')

class KategoriAdmin(admin.ModelAdmin):
	fields = ['nama_kategori']
   	list_display = ['nama_kategori']
   	
admin.site.register(Aplikasi, AplikasiAdmin)
admin.site.register(Kategori, KategoriAdmin)