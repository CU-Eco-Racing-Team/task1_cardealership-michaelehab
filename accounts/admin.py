from django.contrib import admin
from accounts.models import User, Dealer, Customer, Industry

admin.site.register(User)
admin.site.register(Dealer)
admin.site.register(Customer)
admin.site.register(Industry)