from django.shortcuts import redirect, render
from django.views.generic import ListView
from academicmeetings.models import Meeting
from .forms import MeetingModelForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class MeetingPageListView(ListView):
    model = Meeting
    paginate_by = 5
    template_name = 'meetings/meeting_list.html'
    context_object_name = 'meetings'
    queryset = Meeting.objects.all()

def meeting_list(request):
    meeting_list = Meeting.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(meeting_list, 10)
    try:
       meetings = paginator.page(page)
    except PageNotAnInteger:
        meetings = paginator.page(1)
    except EmptyPage:
        meetings = paginator.page(paginator.num_pages)
    context = {
        "meetings":meetings,
    }
    return render(request, 'meetings/meeting_list.html', context)


# def upload_document(request):
#     if request.method == "POST":
#         form = MeetingModelForm(request.POST, request.FILES)
#         documents = request.FILES.getlist('document')
#         if form.is_valid():
#             form.save()
#             for f in documents:
#                 document_instance = Meeting(document=f)
#                 document_instance.save()
#             return redirect('academic_meetings:meeting-list')
#     else:
#         form = MeetingModelForm()
#     context = {
#         'form':form
#     }
#     return render(request, 'meetings/upload_document.html',context)

def upload_document(request):
    if request.method == "POST":
        form = MeetingModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('academic_meetings:meeting-list')
    else:
        form = MeetingModelForm()
    context = {
        'form':form
    }
    return render(request, 'meetings/upload_document.html',context)