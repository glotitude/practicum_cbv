import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Note


class NotesView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(NotesView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        response = "\n".join(["{}".format(x, ) for x in list(Note.objects.all())])

        return HttpResponse(response)

    def post(self, request):
        body = json.loads(request.body)

        note = Note()
        note.text = body['content']

        note.save()

        return HttpResponse('Ok')

    def put(self, request):
        body = json.loads(request.body)

        note = Note.objects.filter(id=body['id']).first()
        note.text = body['content']

        note.save()

        return HttpResponse('Ok')
