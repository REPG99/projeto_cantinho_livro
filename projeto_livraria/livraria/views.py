from django.shortcuts import render
from .models import Livro

def index(request):
    todos_os_livros = Livro.objects.all()
    quantidade_total = len(todos_os_livros)
    
    lista_de_livros = []
    for item in todos_os_livros:
        item_id = item.id
        item_nome = item.nome
        item_preco = item.preco
        item_estoque = item.estoque
        item_autor = item.autor
        
        dicionario_item = {
            'id': item_id,
            'nome': item_nome,
            'preco': item_preco,
            'estoque': item_estoque,
            'autor': item_autor,
        }
        lista_de_livros.append(dicionario_item)

    contexto = {
        'livros': lista_de_livros,
        'total': quantidade_total,
    }
    return render(request, 'index.html', contexto)

def detalhe(request, id):
    livro_encontrado = Livro.objects.get(id=id)
    
    id_livro = livro_encontrado.id
    nome_livro = livro_encontrado.nome
    preco_livro = livro_encontrado.preco
    estoque_livro = livro_encontrado.estoque
    autor_livro = livro_encontrado.autor

    dicionario_resposta = {
        'id': id_livro,
        'nome': nome_livro,
        'preco': preco_livro,
        'estoque': estoque_livro,
        'autor': autor_livro,
    }

    return render(request, 'detalhe.html', dicionario_resposta)