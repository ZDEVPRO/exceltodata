from django.shortcuts import render, redirect

from home.forms import UpdateForm, SendDataForm
from home.models import ExeltoData, AllData
from home.resources import ExeltoDataResources
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse


def simple_upload(request):
    exceltodata = ExeltoData.objects.all()

    if request.method == 'POST':
        person_resource = ExeltoDataResources()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.error(request, 'Bu excel file emas!')
            return redirect('upload')

        import_data = dataset.load(new_person.read(), format='xlsx')
        for data in import_data:
            value = ExeltoData(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
            )
            value.save()
        return redirect('temp-data')
    context = {
        'exceltodata': exceltodata,
    }
    return render(request, 'upload.html', context)


def update(request, id):
    table_update = ExeltoData.objects.get(ID=id)
    table_form = UpdateForm(instance=table_update)

    if request.method == 'POST':
        table_form = UpdateForm(request.POST, instance=table_update)
        if table_form.is_valid():
            table_form.save()
            messages.success(request, 'Muvoffaqiyatli o`zgartirildi.')
            return redirect('temp-data')

    context = {
        'table_form': table_form,
        'table_update': table_update
    }
    return render(request, 'update.html', context)


# data = AllData()
# data.DATE = request.POST['DATE']
# data.INN = request.POST['INN']
# data.FIRMA = request.POST['FIRMA']
# data.SUMDA = request.POST['SUMDA']
# data.KURS = request.POST['KURS']
# data.DOLLAR = request.POST['DOLLAR']
# data.CLIENT = request.POST['CLIENT']
# data.REGION = request.POST['REGION']
# data.MANAGER = request.POST['MANAGER']
# data.save()

def delete(request, id):
    data_delte = ExeltoData.objects.get(ID=id)
    data_delte.delete()
    messages.success(request, 'Muvoffaqiyatli o`chirildi!')
    return redirect('temp-data')


def temp_data(request):
    exceltodata = ExeltoData.objects.all()
    context = {
        'exceltodata': exceltodata
    }
    return render(request, 'temp_data.html', context)


def send_data(request):
    exceltodata = ExeltoData.objects.all()

    if request.method == 'POST':
        exceltodata = ExeltoData.objects.all()

        for data in exceltodata:
            value = AllData(
                DATE=data.DATE,
                INN=data.INN,
                FIRMA=data.FIRMA,
                SUMDA=data.SUMDA,
                KURS=data.KURS,
                DOLLAR=data.DOLLAR,
                CLIENT=data.CLIENT,
                REGION=data.REGION,
                MANAGER=data.MANAGER,
            )
            value.save()

        for olddata in exceltodata:
            value = ExeltoData(
                ID=olddata.ID,
                DATE=olddata.DATE,
                INN=olddata.INN,
                FIRMA=olddata.FIRMA,
                SUMDA=olddata.SUMDA,
                KURS=olddata.KURS,
                DOLLAR=olddata.DOLLAR,
                CLIENT=olddata.CLIENT,
                REGION=olddata.REGION,
                MANAGER=olddata.MANAGER,
            )
            value.delete()

        messages.success(request, 'Malumotlar muvoffaqiyatli bazaga saqlandi!')
        return redirect('send-data')

    context = {
        'exceltodata': exceltodata,
    }
    return render(request, 'send_data.html', context)


def all_data(request):
    alldata = AllData.objects.all()
    context = {
        'alldata': alldata,
    }
    return render(request, 'all_data.html', context)
