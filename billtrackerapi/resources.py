from tastypie.resources import ModelResource
from billtrackerapi.models import BillTracker
from tastypie.authorization import Authorization

class BillTrackerResource(ModelResource):
    class Meta:
        queryset = BillTracker.objects.all()
        resource_name = "billtracker"
        authorization = Authorization()