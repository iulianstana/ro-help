from django.urls import path, include
from django.views.generic import TemplateView

from hub.views import (
    NGONeedListView,
    NGODetailView,
    NGOHelperCreateView,
    NGORegisterRequestCreateView,
    NGODonateCreateView,
)


urlpatterns = [
    # path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", NGONeedListView.as_view(), name="ngos"),
    path("ngos/register", NGORegisterRequestCreateView.as_view(), name="ngos-register-request"),
    path("ngos/<int:pk>", NGODetailView.as_view(), name="ngo-detail"),
    path("ngos/<int:ngo>/donate", NGODonateCreateView.as_view(), name="ngo-donate"),
    path("ngos/<int:ngo>/<int:need>/", NGOHelperCreateView.as_view(), name="ngo-need"),
    path("i18n/", include("django.conf.urls.i18n")),
]
