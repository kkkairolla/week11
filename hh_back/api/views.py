from django.http import JsonResponse
from django.shortcuts import render
from api.models import Company, Vacancy

# Create your views here.
def get_all_companies(request):
    companies = Company.objects.all()
    return JsonResponse([company.to_json() for company in companies], safe=False)

def get_one_company(request, company_id):
    return JsonResponse(Company.objects.get(id = company_id).to_json(), safe=False)

def get_vacancies_by_company(request, company_id):
    vacancies = Vacancy.objects.filter(company = Company.objects.get(id = company_id))
    return JsonResponse([vacancy.to_json() for vacancy in vacancies], safe=False)

def get_all_vacancies(request):
    vacancies = Vacancy.objects.all()
    return JsonResponse([vacancy.to_json() for vacancy in vacancies], safe=False)

def get_one_vacancy(request, vacancy_id):
    return JsonResponse(Vacancy.objects.get(id = vacancy_id).to_json(), safe=False)

def get_top_ten_vacancies(request):
    vacancies = Vacancy.objects.order_by('-salary')[:10]
    return JsonResponse([vacancy.to_json() for vacancy in vacancies], safe=False)