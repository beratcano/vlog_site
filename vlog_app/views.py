from .models import VlogPost
from .forms import VlogPostForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseForbidden

#Vlogs
class VlogPostListView(ListView):
    model = VlogPost
    template_name = "vlog_list.html"
    context_object_name = "vlogs"
    paginate_by = 10

class VlogPostDetailView(DetailView):
    model = VlogPost
    template_name = "vlog_detail.html"
    context_object_name = "vlog"

class VlogPostCreateView(CreateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = "vlog_form.html"
    success_url = reverse_lazy("vlog_list")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        return super().form_valid(form)
    
class VlogPostUpdateView(UpdateView):
    model = VlogPost
    form_class = VlogPostForm
    template_name = "vlog_edit.html"
    success_url = reverse_lazy("vlog_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vlog'] = self.get_object()  # Pass the Vlog instance to the template
        return context
    
    # def dispatch(self, request, *args, **kwargs):
    #     # Ensure the logged-in user is the author
    #     vlog = self.get_object()
    #     if vlog.author != request.user:
    #         return HttpResponseForbidden("You are not authorized to edit this vlog.")
    #     return super().dispatch(request, *args, **kwargs)

#Login and Logout
def register(request):
    messages.get_messages(request)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
        else:
            messages.error(request, "There was an error with your registration. Please check the form.")
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})