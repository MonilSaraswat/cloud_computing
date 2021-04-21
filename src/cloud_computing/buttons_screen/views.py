import json
import math

from django.conf import settings
from django.shortcuts import redirect

# Create your views here.
from django.views.generic import FormView
from djng.views.mixins import allow_remote_invocation, JSONResponseMixin
from rest_framework.decorators import api_view

from buttons_screen.aws_helper import upload_file_to_s3
from buttons_screen.forms import ButtonScreenForm, MetaDataScreenForm
from buttons_screen.models import UploadedImages


class MetaDataScreen(JSONResponseMixin, FormView):
    template_name = "meta-data-screen.html"
    form_class = MetaDataScreenForm

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_id = kwargs.get('image_id', None)
        if image_id:
            image = UploadedImages.objects.filter(id=image_id)
            if len(image) > 0:
                image = image[0]
                data = {'name': image.name,
                        'type': image.type,
                        'aws_path': image.aws_path,
                        'size': image.size
                        }
                form.initial['data'] = json.dumps(data)
                context = self.get_context_data(form=form)
                return self.render_to_response(context)


class ButtonScreen(JSONResponseMixin, FormView):
    template_name = "button-screen.html"
    form_class = ButtonScreenForm

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

    @allow_remote_invocation
    def list_all_images(self, request_params):
        """
        This function will list images
        :return: list of all images
        """
        uploaded_images = UploadedImages.objects.all()
        images = []
        for image in uploaded_images:
            images.append({'name': image.name,
                           'type': image.type,
                           'aws_path': image.aws_path,
                           'size': image.size,
                           'end_point': 'images/' + str(image.id) + '/',
                           })
        return {'all_items': images}


@api_view(['POST'])
def upload_file_to_aws(request):
    """
    Will upload to aws
    """
    request_data = request.data
    image = request_data.get('image', None)
    if image:
        file_data = image.file
        directory = 'images/'
        file_name = image.name
        s3_path = upload_file_to_s3(file_data=file_data,
                                    file_name=file_name,
                                    directory=directory)
        image_path = "http://" + settings.AWS_S3_CUSTOM_DOMAIN + '/' + s3_path
        file_type = image.content_type
        file_size = (image.size / 1024000)  # converting in mb
        if image_path:
            uploadedimages = UploadedImages(name=file_name,
                                            type=file_type,
                                            aws_path=image_path,
                                            size=file_size,
                                            end_point=s3_path)
            uploadedimages.save()
    return redirect('/')
