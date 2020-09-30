from bs4 import BeautifulSoup
import requests

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import College

# Create your views here.

def home_page(request):
    colleges = College.objects.all()

    url = 'https://www.worldometers.info/coronavirus/usa/california/'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    cali = ['Los Angeles', 'Riverside', 'Orange', 'San Diego', 'Santa Barbara', 'Yolo', 'Alameda', 'Merced', 'Santa Cruz', 'San Francisco']
    counties = []

    for county in soup.find_all('tr'):
        cases = []
        for county_info in county.find_all('td'):
            county_info = county_info.text.strip('\n')
            cases.append(county_info.strip())
        if cases != []:
            counties.append(cases[:len(cases)-1])

    counties = counties[:int(len(counties)/2)]
    for x in counties:
        if x[0] in cali:
                college = College.objects.get(county_name=x[0])
                college.county_total_cases = x[1]
                college.county_new_cases = x[2]
                college.county_total_deaths = x[3]
                college.county_active_cases = str(x[5])
                college.county_total_deaths = x[6]

    context = {
        'colleges': colleges,
    }

    return render(request, 'home/home.html', context)

class BarChart(APIView):

    def get(self, request, format=None):
        colleges = College.objects.all()

        college_names = []
        total_cases = []
        total_deaths = []
        total_tests = []

        for college in colleges:
            college_names.append(college.county_name)
            total_cases.append(college.county_total_cases)
            total_deaths.append(college.county_total_deaths)
            total_tests.append(college.county_total_tests)

        data = {
            'college_names': college_names,
            'total_cases': total_cases,
            'total_deaths': total_deaths,
            'total_tests': total_tests,
        }

        return Response(data)

def irvine(request):
    college = College.objects.get(college_name='University of California, Irvine')

    url = 'https://uci.edu/coronavirus/'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    cases = soup.find('table', class_='table')

    covid = []

    for x in cases.find_all('tr'):
        for y in x.find_all('td'):
            covid.append(y.text)

    total_cases = sum(int(num) for num in covid)
    college.college_total_cases = total_cases

    context = {
        'college': college,
    }

    return render(request, 'home/cases.html', context)

def riverside(request):
    college = College.objects.get(college_name='University of California, Riverside')

    url = 'https://ehs.ucr.edu/coronavirus/cases'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    covid = []

    for case in soup.find_all('tr'):
        cases = []
        for info in case.find_all('td'):
            if info.h6 is not None:
                cases.append(info.h6.strong.text)
        if cases != []:
            covid.append(cases)

    college.college_total_cases = covid[0][1]

    context = {
        'college': college,
    }

    return render(request, 'home/cases.html', context)

def santa_cruz(request):
    college = College.objects.get(college_name='University of California, Santa Cruz')

    url = 'https://recovery.ucsc.edu/reporting-covid/'
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')

    covid = []

    for case in soup.find_all('tr'):
        covid.append(case.find('td').text)

    college.college_total_cases = covid[0]

    context = {
        'college': college,
    }

    return render(request, 'home/cases.html', context)

def view_college(request, pk):
    college = College.objects.get(id=pk)

    context = {
        'college': college,
    }

    return render(request, 'home/cases.html', context)
