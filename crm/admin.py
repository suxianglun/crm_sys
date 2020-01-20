from django.contrib import admin
from crm.models import Company, CustomerIndustry


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(CustomerIndustry)
class CustomerIndustryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
