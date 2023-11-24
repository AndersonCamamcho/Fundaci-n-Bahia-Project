
from django.contrib import admin
from django.urls import path
from loginapp.views import registro, Home, panel_padrino, process_beneficiary_form, salir, ingresar, view_beneficiary_records, edit_record

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('registro/', registro),
    path('panel_padrino/', panel_padrino, name='habla'),
    path('employee_panel/', process_beneficiary_form),
    path('employee_panel/', view_beneficiary_records, name='view_beneficiary_records'),
    path('employee_panel/<int:id>', edit_record, name='edit'),
    path('salir/', salir),
    path('ingresar/', ingresar),

]
