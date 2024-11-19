from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from superadmin.helper import renderhelper, is_ajax
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from superadmin.custom_permision import LoginRequiredMixin, AdminLoginRequiredMixin
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from superadmin.models import *
# from superadmin.serializer import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.db.models import Q

from django.http import JsonResponse
from django.template.loader import render_to_string, get_template

from itertools import chain
from django.core.files.base import ContentFile
from django.urls import reverse
from django.http import HttpResponseRedirect

# from superadmin.helper import renderhelper, is_ajax, sendQAPushNotification,link_callback
# from docx import Document
from datetime import datetime
import random



# Create your views here.
class index(View):
    def get(self, request):
        context = {}
        if request.user.id:
            return redirect('superadmin:dashboard')
        else:
            return renderhelper(request, 'login', 'login', context)

    def post(self, request):
        context = {}
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        # return HttpResponse(user)

        if user:
            login(request, user)
            return redirect('superadmin:dashboard')
        else:
            context['username'] = username
            context['password'] = password
            messages.info(request, 'Invalid Username or Password')
            return renderhelper(request, 'login', 'login', context)




class dashboard(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        return renderhelper(request, 'home', 'index', context)

class Logout(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return redirect('superadmin:login')

class profile(LoginRequiredMixin,View):
    def get(self, request):
        context = {}
        return renderhelper(request, 'login', 'profile',context)
    
    def post(self, request):
        password_to_check = request.POST['oldpassword']
        newpassword = request.POST['newpassword']
        conpassword = request.POST['conpassword']
        password_matches = check_password(password_to_check, request.user.password)
        if password_matches:
            if newpassword == conpassword:
                user = User.objects.get(id=request.user.id)
                new_password = conpassword  # Replace 'new_password' with the new password
                user.set_password(new_password)
                user.pass_text = conpassword
                user.save()
                messages.info(request, 'Password changed')
                return renderhelper(request, 'login', 'profile')
            else:
                messages.info(request, 'new password not matching')
                context = {'oldpass': password_to_check, 'newpassword': newpassword, 'conpassword': conpassword}
                return renderhelper(request, 'login', 'profile', context)

        else:
            messages.info(request, 'Your old password is incorrect')
            context = {'oldpass': password_to_check,'newpassword':newpassword,'conpassword':conpassword}
            return renderhelper(request, 'login', 'profile', context)
        


class userlist(LoginRequiredMixin,View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()
        # context['previllage'] = check_previllage(request, 'Course')
        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            # search = request.GET.get("search")
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = User.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                User.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            # if search:
            #     conditions &= Q(eng_title__icontains=search)
            if status:
                conditions &= Q(is_active=status)
            data_list = User.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/users/course-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = User.objects.filter(user_type=4).order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num

        return renderhelper(request, 'users', 'users-view',context)

class usercreate(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        try:
            context['data'] =data= User.objects.get(id=id)
            

        except:
            context['data'] = None
        return renderhelper(request, 'users', 'users-create', context)

    def post(self, request, id=None):
        try:
            data = User.objects.get(id=id)
            messages.info(request, 'Successfully Updated')
        except:
            data = User()
            data.save()
            data.unique_id = 'FF'+str(data.id)+str(random.randint(0000,9999))
            messages.info(request, 'Successfully Added')

        image = request.FILES.get('imagefile')
        if image:
            data.image=image


       

        data.firstname=request.POST['firstname']
        data.lastname=request.POST['lastname']
        data.phone=request.POST['mobile']
        data.email=request.POST['email']
        data.profession=request.POST['profession']
        data.user_type=4
        

        data.save()



        return redirect('superadmin:userlist')


class courselist(LoginRequiredMixin,View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()
        # context['previllage'] = check_previllage(request, 'Course')
        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            # search = request.GET.get("search")
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = Courses.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                Courses.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            # if search:
            #     conditions &= Q(eng_title__icontains=search)
            if status:
                conditions &= Q(is_active=status)
            data_list = Courses.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/course/course-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = Courses.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num

        return renderhelper(request, 'course', 'course-view',context)

class coursecreate(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        try:
            context['data'] = Courses.objects.get(id=id)
        except:
            context['data'] = None
        return renderhelper(request, 'course', 'course-create', context)

    def post(self, request, id=None):
        try:
            data = Courses.objects.get(id=id)
            messages.info(request, 'Successfully Updated')
        except:
            data = Courses()
            messages.info(request, 'Successfully Added')

        image = request.FILES.get('imagefile')
        if image:
            data.image=image


       

        data.type=request.POST['course_type']
        data.title=request.POST['course_name']
        data.subtitle=request.POST['sub_content']
        data.phone=request.POST['mobile_number']
        data.email=request.POST['email_id']
        data.profession=request.POST['profession']
        

        data.save()



        return redirect('superadmin:courselist')




class instructorlist(LoginRequiredMixin,View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()
        
        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            # search = request.GET.get("search")
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = Instructors.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                Instructors.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            # if search:
            #     conditions &= Q(eng_title__icontains=search)
            if status:
                conditions &= Q(is_active=status)
            data_list = Instructors.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/instructor/instructor-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = Instructors.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num

        return renderhelper(request, 'instructor', 'instructor-view',context)

class instructorcreate(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        try:
            context['data'] =data= Instructors.objects.get(id=id)
            context['mycourse'] = [int(course) for course in data.course]
        except:
            context['data'] = None
        context['course'] = Courses.objects.filter(is_active=True)
        return renderhelper(request, 'instructor', 'instructor-create', context)

    def post(self, request, id=None):
        try:
            data = Instructors.objects.get(id=id)
            messages.info(request, 'Successfully Updated')
        except:
            data = Instructors()
            messages.info(request, 'Successfully Added')

        image = request.FILES.get('imagefile')
        

        title = request.POST.get('name')
        designation = request.POST.get('designation')
        course = request.POST.getlist('course')
        data.name=title
        data.designation=designation
        data.course=course
        if image:
            data.image=image


        data.save()



        return redirect('superadmin:instructorlist')




class categorybloglist(LoginRequiredMixin,View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()
        
        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            # search = request.GET.get("search")
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = BlogCategory.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                BlogCategory.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            # if search:
            #     conditions &= Q(eng_title__icontains=search)
            if status:
                conditions &= Q(is_active=status)
            data_list = BlogCategory.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/blog-category/blogcategory-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = BlogCategory.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num

        return renderhelper(request, 'blog-category', 'categoryblog-view',context)

class categoryblogcreate(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        try:
            context['data'] =data= BlogCategory.objects.get(id=id)
        except:
            context['data'] = None
        return renderhelper(request, 'blog-category', 'categoryblog-create', context)

    def post(self, request, id=None):
        try:
            data = BlogCategory.objects.get(id=id)
            messages.info(request, 'Successfully Updated')
        except:
            data = BlogCategory()
            messages.info(request, 'Successfully Added')

        

        title = request.POST.get('title')
        data.title = title

        data.save()




        return redirect('superadmin:categorybloglist')



class bloglist(LoginRequiredMixin,View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()
        
        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            # search = request.GET.get("search")
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = BlogCategory.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                BlogCategory.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            # if search:
            #     conditions &= Q(eng_title__icontains=search)
            if status:
                conditions &= Q(is_active=status)
            data_list = BlogCategory.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/blog/blog-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = BlogCategory.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num

        return renderhelper(request, 'blog', 'blog-view',context)

class blogcreate(LoginRequiredMixin, View):
    def get(self, request, id=None):
        context = {}
        try:
            context['data'] =data= BlogCategory.objects.get(id=id)
        except:
            context['data'] = None
        return renderhelper(request, 'blog', 'blog-create', context)

    def post(self, request, id=None):
        try:
            data = BlogCategory.objects.get(id=id)
            messages.info(request, 'Successfully Updated')
        except:
            data = BlogCategory()
            messages.info(request, 'Successfully Added')

        

        title = request.POST.get('title')
        data.title = title

        data.save()




        return redirect('superadmin:bloglist')



class paymentlist(LoginRequiredMixin,View):
    def get(self, request, id=None):
        context = {}
        conditions = Q()
        
        if is_ajax(request):
            page = request.GET.get('page', 1)
            context['page'] = page
            status = request.GET.get('status')
            # search = request.GET.get("search")
            type = request.GET.get('type')
            if type == '1':
                id = request.GET.get('id')
                vl = request.GET.get('vl')
                cat = Instructors.objects.get(id=id)
                if vl == '2':
                    cat.is_active = False
                else:
                    cat.is_active = True
                cat.save()
                messages.info(request, 'Successfully Updated')
            elif type == '2':
                id = request.GET.get('id')
                Instructors.objects.filter(id=id).delete()
                messages.info(request, 'Successfully Deleted')
            # if search:
            #     conditions &= Q(eng_title__icontains=search)
            if status:
                conditions &= Q(is_active=status)
            data_list = Instructors.objects.filter(conditions).order_by('-id')
            paginator = Paginator(data_list, 15)

            try:
                datas = paginator.page(page)
            except PageNotAnInteger:
                datas = paginator.page(1)
            except EmptyPage:
                datas = paginator.page(paginator.num_pages)
            context['datas'] = datas
            template = loader.get_template('superadmin/instructor/instructor-table.html')
            html_content = template.render(context, request)
            return JsonResponse({'status': True, 'template': html_content})

        data = Instructors.objects.all().order_by('-id')
        p = Paginator(data, 15)
        page_num = request.GET.get('page', 1)
        try:
            page = p.page(page_num)
        except EmptyPage:
            page = p.page(1)
        context['datas'] = page
        context['page'] = page_num

        return renderhelper(request, 'payments', 'payment-list',context)
