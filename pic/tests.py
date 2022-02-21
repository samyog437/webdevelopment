from atexit import register
import imp
from django.test import TestCase

from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse, resolve
from .views import *
from users.views import *

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_home(self):
        url = reverse('pic')
        self.assertEquals(resolve(url).func,pic)
    
    def test_viewpic(self):
        url = reverse('picture', args=[1])
        self.assertEquals(resolve(url).func,picture)

    def test_createpic(self):
        url = reverse('create-picture')
        self.assertEquals(resolve(url).func,createPicture)
    
    def test_updatepic(self):
        url = reverse('update-picture', args=[1])
        self.assertEquals(resolve(url).func,updatePicture)

    def test_deletepic(self):
        url = reverse('delete-picture', args=[1])
        self.assertEquals(resolve(url).func,deletePicture)
    
    def test_login(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func,loginUser)

    def test_logout(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func,logoutUser)
    
    def test_register(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func,registerUser)
    
    def test_profiles(self):
        url = reverse('profiles')
        self.assertEquals(resolve(url).func,profiles)
    
    def test_profile(self):
        url = reverse('user-profile', args=[1])
        self.assertEquals(resolve(url).func,userProfile)
    
    def test_account(self):
        url = reverse('account')
        self.assertEquals(resolve(url).func,userAccount)
    
    def test_edit_account(self):
        url = reverse('edit-account')
        self.assertEquals(resolve(url).func,editAccount)
    
    def test_adminManage(self):
        url = reverse('adminManage')
        self.assertEquals(resolve(url).func,adminManageAccount)

    def test_delete_profile(self):
        url = reverse('delete-profile', args=[1])
        self.assertEquals(resolve(url).func,adminDeleteAccount)   
    