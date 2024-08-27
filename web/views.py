from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from web.forms import UserRegistrationForm
from .models import Departamento, Extra
from .forms import DepartamentoForm, DepartamentoEditForm, ExtraForm
from datetime import datetime


@login_required
def index(request):
    departamentos = Departamento.objects.filter(user=request.user)

    if request.user.is_staff:
        departamentos = Departamento.objects.all()
    
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    start_date_str = str(start_date)
    end_date_str = str(end_date)

    total_ggcc = 0
    departamentos_info = []
    for dpto in departamentos:
        ggcc_base = dpto.metros_2 * 1000
        ggcc_extra = sum(extra.porcentaje * ggcc_base for extra in dpto.extras.all())
        ggcc = int(ggcc_base + ggcc_extra)
        departamentos_info.append({
            'id':dpto.id,
            'numero': dpto.numero,
            'metros_2': dpto.metros_2,
            'user': dpto.user,
            'ggcc': ggcc
        })

        if start_date and end_date:
            try:
                start = datetime.strptime(start_date_str, '%Y-%m-%d')
                end = datetime.strptime(end_date_str, '%Y-%m-%d')
                if start > end:
                    messages.error(request, 'La fecha de inicio debe ser anterior a la fecha de fin.')
                else:
                    total_months = (end.year - start.year)*12 + (end.month-start.month)
                    total_ggcc = total_months * sum(dpto['ggcc'] for dpto in departamentos_info)            
            except ValueError:
                messages.error(request, 'Fechas no válidas.')
        
    context = {
        'dptos': departamentos_info,
        'total_ggcc' : total_ggcc,
    }
    
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()

    context = {
        'form':form,
    }
    return render(request, 'registration/register.html', context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')

@login_required
def add_dpto(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            departamento = form.save(commit=False)
            departamento.user = request.user
            departamento.save()
            messages.success(request, 'Departamento añadido correctamente.')
            return redirect('index')
    else:
        form = DepartamentoForm()
    
    context = {
        'form':form,
    }
    return render(request, 'departamento_form.html', context)

@login_required
def edit_dpto(request, id):
    departamento = get_object_or_404(Departamento, id=id)
    if request.user != departamento.user and not request.user.is_staff:
        messages.error(request, 'No estas autorizado a editar este departamento.')
        return redirect('index')

    if request.method == 'POST':
        form = DepartamentoEditForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Departamento actualizado correctamente.')
            return redirect('index')
    else:
        form = DepartamentoEditForm(instance=departamento)
    
    context = {
        'form': form,
    }
    return render(request, 'departamento_form.html', context)

@user_passes_test(lambda u: u.is_staff)
def add_extra(request):
    if request.method == 'POST':
        form = ExtraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Extra agregado correctamente.')
            return redirect('extra_list')
    else:
        form = ExtraForm()

    context = {
        'form': form,
    }
    return render(request, 'extra_form.html', context)

@user_passes_test(lambda u: u.is_staff)
def edit_extra(request, id):
    extra = get_object_or_404(Extra, id=id)
    if request.method == 'POST':
        form = ExtraForm(request.POST, instance=extra)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{extra.nombre}" actualizado correctamente.')
            return redirect('extra_list')
    else:
        form = ExtraForm(instance=extra)

    context = {
        'form': form,
    }    
    return render(request, 'extra_form.html', context)

@login_required
def extra_list(request):
    extras = Extra.objects.all()
    
    if request.method == 'POST':
        form = ExtraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Extra añadido correctamente.')
            return redirect('extra_list')
    else:
        form = ExtraForm()
    
    context = {
        'extras': extras,
        'add_extra_form': form
    }
    
    return render(request, 'extra_list.html', context)

@user_passes_test(lambda u: u.is_staff)
def remove_extra(request, id):
    extra = get_object_or_404(Extra, id=id)
    if request.method == 'POST':
        extra.delete()
        messages.success(request, f'"{extra.nombre}" eliminado correctamente.')
        return redirect('extra_list')
    return render(request, 'confirm_delete.html', {'extra': extra})