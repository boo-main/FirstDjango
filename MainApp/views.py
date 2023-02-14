from django.shortcuts import render, HttpResponse

author_info = {
    "name": "Евгений",
    "middle": "Витальевич",
    "surname": "Юрченко",
    "email": "eyurchenko@specialist.ru",
    "phone": "+7-900-100-10-20"
}

items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 7, "name": "Картофель фри", "quantity": 0},
    {"id": 8, "name": "Кепка", "quantity": 124},
]


def home(request):
    result = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(result)


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
            result = f"""
            <h1>{item['name']}</h1>
            <p>Количество: {item['quantity']}</p>
            """
            return HttpResponse(result)
