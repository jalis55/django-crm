
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include(apps.url))
    path('',include('accounts.urls'))
]
