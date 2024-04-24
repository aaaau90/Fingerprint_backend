from django.http import JsonResponse
from django.views import View
from .models import User, Userfp
import base64
from .utils import isFingerprintMatch

class FingerprintView(View):
    def post(self, request, *args, **kwargs):
        incoming_fp = request.POST.get('fingerprint')  # incoming base64 fingerprint
        # assuming matchFp() is a function that takes two base64 fingerprints and returns a boolean
        
        # ssave()

        # print("incoming_fp")
        # print(incoming_fp)
        
        for fp in Userfp.objects.all():
            if isFingerprintMatch(incoming_fp, None):
                user = fp.user
                # check for unpaid bill or other conditions here
                # if all checks pass
                return JsonResponse({'status': 200, 'licence plate': request.POST.get('licence plate')})

        # if no match found
        return JsonResponse({'status': 404, 'error': 'No match found'})


