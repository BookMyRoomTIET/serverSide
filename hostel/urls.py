from django.urls import path
from .views import allocationAlgoView, availableHostelsView, hostelInfoView,roomInformationView,specificHostelView,preferenceFormView

urlpatterns = [
    path('', hostelInfoView.as_view(), name='hostels'),
    path('hostel/', specificHostelView.as_view(), name='hostel'),
    path('rooms/', roomInformationView.as_view(), name='rooms'),
    path('yearallocation/', roomInformationView.as_view(), name='yearallocation'),
    path('available/', availableHostelsView.as_view(), name='available'),
    path('preference/', preferenceFormView.as_view(), name='preference'),
    path('allocationalgo/',allocationAlgoView.as_view(), name='allocationalgo'),
]
