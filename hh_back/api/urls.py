from api import views
from django.urls import path

urlpatterns = [
    path('companies/', views.get_all_companies),
    path('companies/<int:company_id>/', views.get_one_company),
    path('companies/<int:company_id>/vacancies/', views.get_vacancies_by_company),
    path('vacancies/', views.get_all_vacancies),
    path('vacancies/<int:vacancy_id>/', views.get_one_vacancy),
    path('vacancies/top_ten/', views.get_top_ten_vacancies)
]