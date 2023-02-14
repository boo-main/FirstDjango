from django.shortcuts import render, HttpResponse

author_info = {
    "name": "Евгений",
    "middle": "Витальевич",
    "surname": "Юрченко",
    "email": "eyurchenko@specialist.ru",
    "phone": "+7-900-100-10-20"
}


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
