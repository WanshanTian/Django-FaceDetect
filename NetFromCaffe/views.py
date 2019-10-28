from FaceDetect.settings import BASE_DIR
from django.shortcuts import render
from .forms import faceform
from .models import faceDet
from .facedetect import face_detect
import cv2
import os
# Create your views here.
def detect(request):
    if faceform(request.POST, request.FILES).is_valid():
        picture = faceDet(img=request.FILES['img'])
        picture.save()
        img_detected = face_detect(picture.img.path)
        cv2.imwrite(os.path.join(BASE_DIR, 'media/detected.jpg'), img_detected)
        context = {'fin': '/media/detected.jpg',
                   'picture': picture
        }
        return render(request, 'detected_img.html', context)
    else:
        form = faceform()
        context = {'form': form}
        return render(request, 'upload.html', context)
