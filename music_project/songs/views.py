import json

from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest,Http404
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from .models import Song

def list_songs(request):
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)

    songs = Song.objects.all()
    paginator = Paginator(songs, limit)
    try:
        paginated_songs = paginator.page(page)
    except PageNotAnInteger:
        return HttpResponseBadRequest('Invalid page number')
    except EmptyPage:
        return HttpResponseBadRequest('Page out of range.Page Number exists till {}'.format(paginator.num_pages))

    paginated_songs = paginator.page(page)

    songs_list = list(paginated_songs.object_list.values())
    response = {
        'total_items': paginator.count,
        'total_pages': paginator.num_pages,
        'current_page': paginated_songs.number,
        'songs': songs_list
    }
    return JsonResponse(response)

def get_song_by_title(request, title):
    try:
        song = Song.objects.get(title=title)
        return JsonResponse(data=model_to_dict(song))
    except Song.DoesNotExist:
        return JsonResponse({"error": "Song not found"}, status=404)


@csrf_exempt
def rate_song(request, song_id):
    if request.method == 'POST':
        try:
            rating = request.POST.get('rating')
            song = get_object_or_404(Song, id=song_id)
            song.rating = rating
            song.save()
            return JsonResponse({'message': 'Rating updated successfully'})
        except (ValueError, json.JSONDecodeError):
            return HttpResponseBadRequest('Invalid JSON payload')
        except Http404:
            return HttpResponseBadRequest('Invalid Song Id in Request')
        except Exception as e:
            return HttpResponseBadRequest('Internal Server Error')
    return HttpResponseBadRequest('Invalid request method')