from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, NeighbourHood, Post, Business

# Create your tests here.
class  ProfileTestClass(TestCase):
  def setUp(self):
    user = User.objects.create(name='maz')
    self.test = Profile(Bio='Nice',user=user)
    
  def test_instance(self):
    self.assertTrue(isinstance(self.test,Profile))


class NeighbourHoodTestClass(TestCase):
  def setUp(self):
    user = User.objects.create(username='test',password = 'hood')
    self.test = NeighbourHood(name='ff',location='Muthaiga')
  
  def test_instance(self):
    self.assertTrue(isinstance(self.test,NeighbourHood))  

  def test_save(self):
    self.test.save_neighbourhood()
    saved = NeighbourHood.objects.all()
    self.assertTrue(len(saved)>0)
    
    
  def test_delete(self):
    self.test.save_neighbourhood()
    self.test.delete_neighbourhood()
    deleted = NeighbourHood.objects.all()
    self.assertTrue(len(deleted)== 0) 
    
    
  def test_find_by_id(self):
    self.test.save_neighbourhood()
    self.test_1=NeighbourHood(name='ff',location='muthaiga')  

    
    
class  ProfileTestClass(TestCase):
  def setUp(self):
    user = User.objects.create(name='ff')
    neighbourhood = NeighbourHood.objects.create(name='ff',location='muthaiga')
    self.test = Profile(Bio='nice',user=user,neighbourhood=neighbourhood)
    
  def test_instance(self):
    self.assertTrue(isinstance(self.test,Profile))
        