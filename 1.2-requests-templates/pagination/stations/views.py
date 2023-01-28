from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations = []
    with open ('data-398-2018-08-30.csv', newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            bus_station = {
                    'Name': str(row['Name']),
                    'Street': str(row['Street']),
                    'District': str(row['District'])
                }
            bus_stations.append(bus_station)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations, 10)
    page = paginator.get_page(page_number)
    page_obj = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page_obj,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
