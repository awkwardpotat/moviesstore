from django.shortcuts import render, redirect, get_object_or_404
from .models import Petition
from django.contrib.auth.decorators import login_required
from .forms import PetitionForm

# Create your views here.
#I NEED TO PUT PETITIONS ON THE HEADER IN TEMPLATE
#i think all of this should have login required

#home/default page, should be similar to movies
@login_required
def index(request):
    search_term = request.GET.get('search')
    if search_term:
        petitions = Petition.objects.filter(name__icontains=search_term)
    else:
        petitions = Petition.objects.all()
    template_data = {}
    template_data['petitions'] = petitions
    return render(request, 'petitions/index.html', {'template_data': template_data})

#shows one specific petition
@login_required
def show(request, id):
    petition = Petition.objects.get(id=id)
    #also check if user has already voted for this petition
    #user should always be authenticated but just in case
    can_vote = True
    if request.user.is_authenticated:
        can_vote = not petition.voted_users.filter(id=request.user.id).exists()
    template_data = {}
    template_data['petition'] = petition
    template_data['can_vote'] = can_vote
    return render(request, 'petitions/show.html', {'template_data': template_data})

#to page to create new petition
#used for index.html for the button to make a new petition
@login_required
def new_petition_show(request):
    #make a new form for it
    form = PetitionForm()
    return render(request, 'petitions/new_petition_show.html', {'form': form})

#used in new_petition_show.html to create the new petition
@login_required
def create_petition(request):
    if request.method == 'POST':
        form = PetitionForm(request.POST, request.FILES)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.save()
            return redirect('petitions.index')
        else:
            print("sad: ", form.errors)
            return redirect('petitions.index')
    else:
        form = PetitionForm()
        return render(request, 'petitions/new_petition_show.html', {'form': form})
    
#FUNCTION TO VOTE YES/NO HERE
@login_required
def vote(request, id):
    petition = Petition.objects.get(id=id)
    if request.method == 'POST':
        choice = request.POST.get('vote_choice')
        print("user: ", request.user)
        if choice == 'true':
            petition.voted_users.add(request.user)
            petition.yes_votes += 1
            print("yes vote")
        elif choice == 'false':
            petition.voted_users.add(request.user)
            petition.no_votes += 1
            print("no vote")
        petition.save()
        redirect('petitions.show', id)
        
    return redirect('petitions.show', id)