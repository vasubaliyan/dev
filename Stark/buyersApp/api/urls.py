from django.urls import path,include
from rest_framework.routers import DefaultRouter
from.import views

router=DefaultRouter()
router.register(r'login',views.LoginOtpViewset)


urlpatterns=[
    path("",include(router.urls))
]