from web.models import Kategori

def kategori_list(request):
   	kategori = Kategori.objects.all().order_by('nama_kategori')
	return {'kategori_list': kategori}
