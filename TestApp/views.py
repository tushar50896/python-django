from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import Post, Visitor,PostCategory
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render_to_response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import VisitorSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib import messages
# Create your views here.
'''
def single_slug(request,single_slug):
    categories=[c.category_slug for c in PostCategory.objects.all()]
    if single_slug in categories:
        return HttpResponse(f"{single_slug} is a category")
    post=[p.post_slug for p in Post.objects.all()]
    if single_slug in post:
        return HttpResponse(f"{single_slug} is a post")
    return HttpResponse(f"{single_slug} not present")
'''
#############################################################################################################
def home(request):
    return render(request, 'TestApp/home.html')

###################################################################################################################
def blog(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'TestApp/blog.html', context)
#####################################################################################################################
def post(request, slug):
    return render_to_response('TestApp/post.html',{'post':get_object_or_404(Post,post_slug=slug)})

#######################################################################################################################
def contact(request):
    if request.method =='POST':
        name=request.POST['name']
        email=request.POST['emailid']
        message = request.POST['message']
        
        try:
            validate_email(email)
            valid_email=True
        except ValidationError:
            valid_email=False
        if valid_email:
            send_mail(
                'Site Contact by  '+ name ,email + '\n\n\n' + message, settings.EMAIL_HOST_USER,['mytestid1807@gmail.com'],fail_silently=False)
            messages.success(request, 'Your password was updated successfully!')
            #return redirect('Site-Home')
        else:
            pass
            
    return render(request,'TestApp/contact.html')
################################################################################################################################

'''
class contact(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'contact.html'

    def get(self, request, pk):
        visitor = get_object_or_404(Visitor, pk=pk)
        serializer = VisitorSerializer()
        return Response({'serializer': serializer, 'visitor': visitor})

    def post(self, request, pk):
        visitor = get_object_or_404(Visitor, pk=pk)
        serializer = VisitorSerializer(visitor, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'visitor': visitor})
        serializer.save()
        return redirect('contact')
'''