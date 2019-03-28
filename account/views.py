from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserProfileForm, UserForm,UserInfoForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserInfo,File
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import StreamingHttpResponse
from django.views.decorators.http import require_POST


def user_login(request):
    if request.method =="POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                return HttpResponse("Wellcome You.")
            else:
                return HttpResponse("Sorry")
        else:
            return HttpResponse("Invalid login")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, "account/login.html", {"form": login_form})


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)
            return HttpResponse('successfully')
        else:
            return HttpResponse("sorry")
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request, 'account/register.html', {'form': user_form , 'profile': userprofile_form})

@login_required(login_url='/account/login/')
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request, 'account/myself.html', {'user': user, 'userinfo': userinfo, 'userprofile': userprofile})

@login_required(login_url='/account/login')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo = UserInfo.objects.get(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid() * userprofile_form.is_valid() * userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd['email'])
            user.email = user_cd['email']
            userprofile.stunamber = userprofile_cd['stunamber']
            userprofile.major = userprofile_cd['major']
            userinfo.school = userinfo_cd['school']
            userinfo.major = userinfo_cd['major']
            userinfo.getcert = userinfo_cd['getcert']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/')
    else:
        user_form = UserForm(instance = request.user)
        userprofile_form = UserProfileForm(initial={'stunamber':userprofile.stunamber,'major':userprofile.major})
        userinfo_form = UserInfoForm(initial={'school': userinfo.school, 'major': userinfo.major, 'getcert': userinfo.getcert, 'address': userinfo.address, 'aboutme': userinfo.aboutme})
        return render(request, 'account/myself_edit.html',{'user_form':user_form,'userprofile_form':userprofile_form,'userinfo_form':userinfo_form})


@login_required(login_url='/account/login/')
def uploadimg(request):
    if request.method == 'POST':
        img = request.FILES['img']
        if img:
            user = User.objects.get(username=request.user.username)
            userprofile = UserProfile.objects.get(user=user)
            userinfo = UserInfo.objects.get(user=user)
            userinfo.img = img
            userinfo.save()
            return render(request, 'account/myself.html',{'user': user, 'userinfo': userinfo, 'userprofile': userprofile})
        else:
            return HttpResponse('fail')
    else:
        return render(request, 'account/uploadimg.html',)


def special(request):
    return render(request, "account/special.html")


def vs(request):
    return render(request, "account/vs.html")


def introduce(request):
    return render(request, "account/introduce.html")


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        new_file = File(
            file=request.FILES.get('file'),
            name=request.FILES.get('file').name
        )
        if not new_file:
            return HttpResponse("sorry")
        else:
            new_file.save()
            return render(request, 'account/success.html')
    return render(request, 'account/upload.html')


@csrf_exempt
def show_file(request):
    files = File.objects.all()
    content = {
        'files':files,
    }
    return render(request, 'account/uploadlist.html', content)


@login_required(login_url='/account/login/')
@require_POST
@csrf_exempt
def download_file(request):
    file = request.POST['file']
    try:
        def file_iterator(file, chunk_size=512):
            with open(file) as f:
                while True:
                    c = f.read(chunk_size)
                    if c:
                        yield c
                    else:
                        break
        file = "test.txt"
        response = StreamingHttpResponse(file_iterator(file))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file)
        return HttpResponse("1")
    except:
        return HttpResponse("2")