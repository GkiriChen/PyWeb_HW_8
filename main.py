import connect_db 
from models import Author, Quote
#from add_in_db import seed_a, seed_q

def com_name(fullname):
    autor = Author.objects(fullname__istartswith=fullname).first()

    quotes = Quote.objects(author=autor)
    for quote in quotes:
        print(quote.quote)


def tag(tag):
    quotes = Quote.objects(tags__istartswith=tag)
    for quote in quotes:
        print(quote.quote)

def tags(tags_list):
    tags = tags_list.split(',')
    quotes = Quote.objects(tags__in=tags)
    for quote in quotes:
        print(quote.quote)

print(f"Я приймаю команди у наступному форматі - команда: значення")
#print(f"Приклади:\nname:Steve Martin — найти и вернуть список всех цитат автора Steve Martin;\ntag:life — найти и вернуть список цитат для тега life;\ntags:life,live — найти и вернуть список цитат, где есть теги life или live (примечание: без пробелов между тегами life,live);\nexit — закончить выполнение скрипта;")
print(f"Приклади:name: Steve Martin — знайти та повернути список всіх цитат автора Steve Martin;\ntag:life — знайти та повернути список цитат для тегу life;\ntags:life,live — знайти та повернути список цитат, де є теги life або live (примітка: без пробілів між тегами life, live);\nexit — завершити виконання скрипту;")

def app_work():
    while True:
        command = input ("Тапаз дай команду -> ")
        arg = command.split(':')[0]
        match arg:
            case 'exit':
                print("Ясненько")
                break
            case 'name':
                com_name(command.split(':')[1])
            case 'tag':
                tag(command.split(':')[1])
            case 'tags':
                print(command.split(':')[1])
                tags(command.split(':')[1])
            case _:
                print("Я тебе не розумію")




if __name__ == '__main__':

    app_work()
