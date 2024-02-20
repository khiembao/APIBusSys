from .models import Destination, Bus, TripPath

def load_trip_path(params={}):
    q = TripPath.objects.filter(active=True)

    kw = params.get('kw')
    if kw:
        q = q.filter(object_icontains=kw)

    arr_des = params.get('arr_des')
    if arr_des:
        q = q.filter(arrival_destination_id=arr_des)

