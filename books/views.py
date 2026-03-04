from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import Book
from django.contrib.auth.decorators import login_required

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'book/list_book.html'
    context_object_name = 'books'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Book Listed Here'
        context['username'] = self.request.user.username
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/detail_book.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book/create_book.html'
    fields = ['title','description','author','published_date','image']
    success_url = reverse_lazy('list_book')
    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['author'] = 'Unknown Author'
    #     initial['title'] = 'New Book Title'
    #     return initial

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book/create_book.html'
    fields = ['title','description','author','published_date','image']
    success_url = reverse_lazy('list_book')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/delete_book.html'
    success_url = reverse_lazy('list_book')




