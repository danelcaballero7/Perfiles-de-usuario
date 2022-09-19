from django.test import TestCase
from unittest.mock import patch

from django.urls import reverse

from profiles_api import models
import tempfile
import os
from PIL import Image

@patch('uuid.uuid4')
def test_user_file_name_uuid(self, mock_uuid):
    """Probar que la imagen ha sido guardada en el lugar correcto"""
    uuid = 'test-uuid'
    mock_uuid.return_value=uuid
    file_path= models.UserProfile_image_file_path(None, 'myimage.jpg')

    exp_path= f'uploads/user/{uuid}.jpg'
    self.assertEqual(file_path, exp_path)

def image_upload_url(UserProfile_id):
    """URL de retorno para imagen subida"""
    return reverse('UserProfile:UserProfile-upload-image',args=[UserProfile_id])

class UserProfileIploadTest(TestCase):
    def setUp(self):
       pass
