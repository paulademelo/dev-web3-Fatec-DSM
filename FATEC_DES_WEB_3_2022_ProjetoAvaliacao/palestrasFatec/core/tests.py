from django.test import TestCase


class TestsPalestras(TestCase):
    
    def self_Test(self):
        self.index = self.client.get('form')
        self.index = self.client.get('alunos')

    def test_views(self):
        self.assertTemplateUsed(self.form, 'form.html')
        self.assertTemplateUsed(self.alunos, 'alunos.html')