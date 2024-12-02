from .models import VlogPost
from .forms import VlogPostForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.contrib import messages

#Vlogs
class VlogPostListView(ListView):
    model = VlogPost
    template_name = "vlog_list.html"
    context_object_name = "vlogs"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VlogPostForm()
        return context

class VlogPostDetailView(DetailView):
    model = VlogPost
    template_name = "vlog_detail.html"
    context_object_name = "vlog"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user == self.object.author: #type:ignore
            context['form'] = VlogPostForm(instance=self.object)  # type:ignore
        return context

class VlogPostCreateView(CreateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = "vlog_form.html"
    success_url = reverse_lazy("vlog_list")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        response = super().form_valid(form)

        return response
    
class VlogPostUpdateView(UpdateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = "vlog_edit.html"
   
    def get_success_url(self):
        return reverse("vlog_detail", kwargs={"pk": self.object.pk}) #type:ignore

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vlog'] = self.get_object() 
        return context

#Register
def register(request):
    messages.get_messages(request)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vlog/')
        else:
            messages.error(request, "There was an error with your registration. Please check the form.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})