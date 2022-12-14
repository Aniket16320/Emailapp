from django.urls import path
from  emailapp.views import EmailAttachementView


urlpatterns = [
    path('', EmailAttachementView.as_view(), name='emailattachment'),
    # path('send/', views.send, name='emailattachment'),
   

]