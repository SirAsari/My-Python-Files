# urls.py
from django.contrib import admin
from django.urls import path
from administrasiData.views import beranda, view_data_pasien, edit_data_pasien, add_data_pasien, delete_data_pasien

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', beranda, name='beranda'),
    path('administrasiData/<int:noRekamMedis>/', view_data_pasien, name='view_data_pasien'),
    path('administrasiData/add/', add_data_pasien, name='add_data_pasien'),
    path('administrasiData/<int:noRekamMedis>/edit/', edit_data_pasien, name='edit_data_pasien'),
    path('administrasiData/<int:noRekamMedis>/delete/', delete_data_pasien, name='delete_data_pasien'),
]
