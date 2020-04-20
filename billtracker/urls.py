from django.contrib import admin
from django.urls import path
from billtrackerapi.resources import BillTrackerResource
from django.conf.urls import include

bill_tracker = BillTrackerResource()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('billtracker/', include(bill_tracker.urls))
]
