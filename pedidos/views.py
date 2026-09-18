from django.shortcuts import render
from pedidos.models import CategoriaIngrediente, Ingrediente

def tela_selecao(request):
    # 1. Se não existirem categorias, o Django cria elas sozinho aqui
    cat_paes, _ = CategoriaIngrediente.objects.get_or_create(nome="Pães")
    cat_recheios, _ = CategoriaIngrediente.objects.get_or_create(nome="Recheios")

    # 2. Se a lista de itens estiver vazia, o Django cadastra os produtos sozinho
    if not Ingrediente.objects.exists():
        Ingrediente.objects.create(
            categoria=cat_paes,
            nome="Pão Francês",
            preco_adicional=1.50, # CORRIGIDO: Mudado de 'preco' para 'preco_adicional'
            imagem="ingredientes/pao_frances.jpg" 
        )
        Ingrediente.objects.create(
            categoria=cat_paes,
            nome="Pão de Queijo",
            preco_adicional=4.50, # CORRIGIDO: Mudado de 'preco' para 'preco_adicional'
            imagem="ingredientes/pao_queijo.jpg"
        )
        Ingrediente.objects.create(
            categoria=cat_recheios,
            nome="Mortadela Fatiada",
            preco_adicional=2.50, # CORRIGIDO: Mudado de 'preco' para 'preco_adicional'
            imagem="ingredientes/mortadela.jpg"
        )

    # 3. Puxa tudo o que foi criado e manda para a tela amarela do Totem
    ingredientes = Ingrediente.objects.all()
    return render(request, 'selecao.html', {'ingredientes': ingredientes})
