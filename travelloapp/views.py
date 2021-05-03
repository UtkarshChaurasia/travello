from django.shortcuts import render
from . models import Destination

# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Lucknow'
    dest2.img = 'destination_2.jpg'
    dest2.desc = 'The City Of Nawabs And The Kebabs'
    dest2.price = 650
    dest2.offer = False

    dest3 = Destination()
    dest3.name = 'Hyderabad'
    dest3.img = 'destination_3.jpg'
    dest3.desc = 'First Biryani, Then Sherwani'
    dest3.price = 600
    dest3.offer = False


    dests = [dest1,dest2,dest3]

    return render(request, 'index.html',{'dests': dests})
