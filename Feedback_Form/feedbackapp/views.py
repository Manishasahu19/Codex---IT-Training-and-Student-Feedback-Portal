from django.shortcuts import render,redirect
from feedbackapp.models import FeedbackModel
# Create your views here.


def form_view(request):
    submitted = False
    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST.get('feedback')
        FeedbackModel.objects.create(name = a,feedback = b)
        submitted = True
    return render(request,'form.html',{'submitted':submitted})

def feedback_view(request):
    all_feedbacks = FeedbackModel.objects.all()
    return render(request,'feedback.html',{'all_feedbacks':all_feedbacks})

def delete_feedback(request,id):
    item= FeedbackModel.objects.get(id=id)
    item.delete()
    return redirect('/feedbackapp/feedback/')