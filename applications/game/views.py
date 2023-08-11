from django.shortcuts import render

# from services import generate_fruits, generate_vegetables, main


def index(request):
    # if request.method == 'POST':
    #     num_players = int(request.POST.get('num_players'))
    #
    #     players = main.add_players()
    #
    #     # play_game(players)

    return render(request, 'index.html')