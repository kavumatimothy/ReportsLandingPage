from django.shortcuts import render
from home.models import Report, Department
from django.db.models import Q


def home(request):
    reports = Report.objects.all()
    departments = Department.objects.all()

    context = {
        'home': reports,
        'departments': departments
    }
    return render(request, 'home.html', context)


def search(request):
    keyword = request.GET.get("keyword")
    reports = Report.objects.order_by('-date_created').filter(Q(report_detail__icontains=keyword) | Q(report_name__icontains=keyword))
    report_count = reports.count()

    context = {
        'reports': reports,
        'report_count': report_count,
        'keyword': keyword
    }
    return render(request, 'home.html', context)
