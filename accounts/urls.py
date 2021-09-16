from django.urls import path
from accounts.views import DealerRegistrationView, DealerList, CustomerRegistrationView, CustomerList, IndustryRegistrationView, IndustryList, pass_position, give_admin_permissions
from contracts.views import ContractView
from cars.views import CarView, DealView
from rest_framework import routers

app_name = 'accounts'

router = routers.DefaultRouter()
#Main Data Urls
router.register('contracts', ContractView)
router.register('dealers', DealerList)
router.register('customers', CustomerList)
router.register('industries', IndustryList)
router.register('cars', CarView)
router.register('deals', DealView)

urlpatterns = [
    #Registration Urls
    path('register/dealer/', DealerRegistrationView.as_view(), name='register-dealer'),
    path('register/customer/', CustomerRegistrationView.as_view(), name='register-customer'),
    path('register/industry/', IndustryRegistrationView.as_view(), name='register-industry'),

    #Pass Position Url
    path('owner/pass/<id>', pass_position),

    #Give Administrative Permissions Url
    path('owner/promote/<id>', give_admin_permissions)
]+router.urls