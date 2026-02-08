from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Project, Experience, ContactMessage
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = 'core/home.html'

class AboutView(TemplateView):
    template_name = 'core/about.html'

class ExperienceView(ListView):
    model = Experience
    template_name = 'core/experience.html'
    context_object_name = 'experiences'

class ProjectListView(ListView):
    model = Project
    template_name = 'core/projects.html'
    context_object_name = 'projects'

class ContactView(CreateView):
    model = ContactMessage
    form_class = ContactForm
    template_name = 'core/contact.html'
    success_url = reverse_lazy('core:contact')

    def form_valid(self, form):
        messages.success(self.request, "Your message has been sent successfully!")
        return super().form_valid(form)
