from django.urls import path
from feedbackapp import views

urlpatterns = [
    path('form/',views.form_view,name='form'),
    path('feedback/',views.feedback_view,name='feedback'),
    path('delete/<int:id>/',views.delete_feedback,name='delete_feedback'),

]