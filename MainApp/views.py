from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
from MainApp.models import Item


def home(request):
    context = {
        "name": "Евгений",
        "email": "email@test.ru"
    }
    return render(request, 'index.html', context)


def about(request):
    result = f"""
    Имя: <b>{author_info['name']}</b><br>
    Отчество: <b>{author_info['middle']}</b><br>
    Фамилия: <b>{author_info['surname']}</b><br>
    телефон: <b>{author_info['phone']}</b><br>
    email: <b>{author_info['email']}</b><br>
    """
    return HttpResponse(result)


# url: /item/1
# url: /item/2
def get_item(request, id):
    for item in items:
        if item['id'] == id:
            context = {
                'item': item
            }
            return render(request, 'item-page.html', context)

    return HttpResponseNotFound(f"Item with id={id} not found")


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, 'items-list.html', context)
