from django.http import JsonResponse
from django.views import View
from .models import User, Userfp
import base64
from .utils import isFingerprintMatch


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserfpSerializer, UserSerializer



class FingerprintView(View):
    def post(self, request, *args, **kwargs):
        incoming_fp = request.POST.get('fingerprint')  # incoming base64 fingerprint
        # assuming matchFp() is a function that takes two base64 fingerprints and returns a boolean
        
        # ssave()

        # print("incoming_fp")
        # print(incoming_fp)
#        score = 0
        for fp in Userfp.objects.all():
            if isFingerprintMatch(incoming_fp, fp.fingerprint):
#            if temp > score:
#                score = temp
                user = fp.userid
                finse_value = user.finse
                if finse_value > 50000:
                    return JsonResponse({'status': 405, 'licence plate': request.POST.get('licence plate'), 'error': 'High Finse Value'})

                # check for unpaid bill or other conditions here
                # if all checks pass
                return JsonResponse({'status': 200, 'licence plate': request.POST.get('licence plate')})

        # if no match found
        return JsonResponse({'status': 404, 'error': 'No match found'})


@api_view(['POST'])
def add_fingerprint(request):
    name = request.data.get('username')
    fingerprint_data = request.data.get('fingerprint')

    # Check if the user exists
    try:
        user = User.objects.get(name=name)
    except User.DoesNotExist:
        return Response({'error': 'User does not exist.'}, status=status.HTTP_404_NOT_FOUND)

    # Prepare data for the serializer
    userfp_data = {
        'userid': user.id,
        'fingerprint': fingerprint_data
    }

    # Instantiate the serializer with the data
    userfp_serializer = UserfpSerializer(data=userfp_data)

    if userfp_serializer.is_valid():
        userfp_serializer.save()
        return Response({'user_id': user.id, 'message': 'Fingerprint added successfully.'}, status=status.HTTP_201_CREATED)
    else:
        return Response(userfp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
