from django.http import HttpResponse

def testeo_inicial(request):
    return HttpResponse("Hola! Este es un mensaje de confirmación")