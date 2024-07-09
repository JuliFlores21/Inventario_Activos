# activos/views.py

from django.shortcuts import render
from .forms import UploadFileForm
import csv

def escanear_archivo(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            archivo_csv = request.FILES['archivo_csv']
            categorias = {
                'Datos / Información': ['png', 'jpg', 'pdf', 'xml', 'datos', 'información', 'assets', 'files'],
                'Servicios': ['mail', 'vpn', 'sftp', 'server', 'https', 'http', 'help', 'api', 'service', 'domain', 'relay', 'google', 'aws', 'amazon', 'dns'],
                'Software - Aplicaciones informáticas': ['exe', 'msi', 'software', 'application', 'app', 'test', 'desktop', 'android', 'gateway'],
                'Personal': ['@', 'phone', 'contact', 'name', 'email', 'personnel']
            }

            cid_values = {
                'Datos / Información': {'confidencialidad': 3, 'integridad': 4, 'disponibilidad': 3},
                'Servicios': {'confidencialidad': 2, 'integridad': 3, 'disponibilidad': 4},
                'Software - Aplicaciones informáticas': {'confidencialidad': 4, 'integridad': 5, 'disponibilidad': 3},
                'Personal': {'confidencialidad': 3, 'integridad': 5, 'disponibilidad': 2}
            }

            # Procesar el archivo CSV
            resultados = []
            reader = csv.reader(archivo_csv.read().decode('utf-8').splitlines(), delimiter=',', quotechar='"')
            for row in reader:
                categoria_asignada = None
                for categoria, palabras_clave in categorias.items():
                    for palabra_clave in palabras_clave:
                        if palabra_clave.lower() in row[1].lower():
                            categoria_asignada = categoria
                            break
                    if categoria_asignada:
                        resultados.append({
                            'nombre': row[0],
                            'descripcion': row[1],
                            'tipo': categoria_asignada,
                            'confidencialidad': cid_values[categoria_asignada]['confidencialidad'],
                            'integridad': cid_values[categoria_asignada]['integridad'],
                            'disponibilidad': cid_values[categoria_asignada]['disponibilidad']
                        })
                        break
            return render(request, 'activos/resultados.html', {'resultados': resultados})
    else:
        form = UploadFileForm()
    return render(request, 'activos/escanear_archivo.html', {'form': form})
