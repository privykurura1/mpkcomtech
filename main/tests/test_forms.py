from django.test import TestCase
from django.core import mail
from main import form

class TestForm(TestCase):
    def test_valid_contact_us_form_sends_mail(self):
        form = forms.ContactForm({
            'name':"privy kurura",
            'message':"hi there"})
        self.assertTrue(form.is_valid())
        
        with self.assertLogs('main.forms',level='INFO') as cm:
            form.send_mail()
        
        self.assertEqual(len(mail.outbox),1)
        self.asertEqual(mail.outbox[0].subject, 'Site message')
        
        self.assertGreaterEqual(len(cm.output),1)
        
    def test_invalid_contact_us_form(self):
        form = forms.ContactForm({
            'mesage': "hi there"})
        
        self.assertFalse(form.is_valid())