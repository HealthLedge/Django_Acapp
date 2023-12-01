from django.http import HttpResponse

def index(request):
    line = '<h1 style="text-align: center">Wayn\'s Blog<h1/>'
    line2 = '<img src="https://cdn.acwing.com/media/user/profile/photo/265085_lg_f75c5abe88.jpg" width=400></img>'
    line3 = '<hr>'
    line4 = '<a href="/play/">进入游戏界面</a>'
    return HttpResponse(line + line4 + line3 + line2)

def play(request):
    line1 = '<h1 style="text-align: center">游戏界面</h1>'
    line3 = '<a href="/">返回主界面</a>'
    line4 = '<hr>'
    line2 = '<img src="https://cdn.acwing.com/media/user/profile/photo/372632_lg_6415226271.jpg"></img>'
    return HttpResponse(line1 + line3 + line4 + line2)
