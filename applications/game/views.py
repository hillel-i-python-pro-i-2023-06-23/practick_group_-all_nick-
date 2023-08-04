from django.shortcuts import render

# from services import generate_fruits, generate_vegetables


def index(request):
    # if request.method == 'POST':
    #     num_players = int(request.POST.get('num_players'))
    #
    #     players = add_players(num_players)
    #
    #     play_game(players)

    return render(request, 'index.html')