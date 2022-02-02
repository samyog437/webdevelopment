from django.shortcuts import render
from django.http import HttpResponse

picList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]

# Create your views here.
def pic(request):
    page = 'pic'
    number = 10
    context = {'page': page, 'number':number, 'pic': picList}
    return render(request, 'pic/pics.html', context)

def picture(request, pk):
    pictureObj = None
    for i in picList:
        if i['id'] == pk:
            pictureObj = i
    return render(request, 'pic/picture.html', {'picture':pictureObj}) 