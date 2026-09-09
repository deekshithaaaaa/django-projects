from django.shortcuts import render
from .models import Books
from django.http import HttpResponse
from .forms import BookForm,BookModelForm

# Create your views here.
def home(request):
    form = BookModelForm()

    if request.method == 'POST':
        form = BookModelForm(request.POST)

        if form.is_valid():
            form.save()

    books = Books.objects.all()

    context = {
        'books': books,
        'form': form
    }

    return render(request, 'home.html', context)
def edit(request,num):
    book=Books.objects.get(id=num)
    if request.method=='POST':
        title=request.POST.get('title')
        author=request.POST.get('author')
        price=int(request.POST.get('price'))
        book.title=title
        book.author=author
        book.price=price
        book.save()
    context={
            'book':book
        }
    return render(request,'edit.html',context)
            
def delete(request,num):
    book=Books.objects.get(id=num)
    book.delete()
    return HttpResponse("Book deleted")