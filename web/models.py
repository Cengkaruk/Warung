from django.db import models

# Create your models here.	
class Kategori(models.Model):
	id_kategori = models.AutoField(primary_key=True)
	nama_kategori = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.nama_kategori

class Aplikasi(models.Model):
	id_aplikasi = models.AutoField(primary_key=True)
	nama_aplikasi = models.CharField(max_length=50)
	gambar_aplikasi = models.CharField(max_length=100)
	keterangan = models.TextField()
	link_unduh = models.CharField(max_length=100)
	id_kategori = models.ForeignKey(Kategori, verbose_name="Kategori")
	tanggal_ditambahkan = models.DateTimeField(auto_now_add = True)
	jumlah_unduh = models.IntegerField(default=0)	