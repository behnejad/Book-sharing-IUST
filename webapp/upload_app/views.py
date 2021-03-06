from django.http import HttpResponse
from django.shortcuts import render_to_response
from upload_app.models import PDF
from mysite.forms import UploadForm
from books.models import Books
def list(request):
    try:
        user=request.session['user']
        if user.is_authenticated() :
            # Handle file upload
            if request.method == 'POST':
                form = UploadForm(request.POST, request.FILES)
                if form.is_valid():
                    cd = form.cleaned_data
                    the_name=cd['name']
                    the_author=cd['author']
                    the_comment=cd['comment']
                    newbook = PDF(docfile = request.FILES['docfile'],name=the_name,
                    author=the_author,comment=the_comment            )
                    newbook.save()
                    allbooks=PDF.objects.all()
                    books_list=Books.objects.all()
                    return render_to_response('upload.html',{'uploadedpdf':allbooks,'name':user.username})
            else:
                form=UploadForm()
                return render_to_response('upload.html',{'form':form,'name':user.username})
    except:
        return HttpResponse("you're not logged in")
