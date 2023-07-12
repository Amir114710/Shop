from django.shortcuts import render
from django.views.generic import FormView
import ghasedakpack
from sms_send.form import SmsForm
from sms_send.models import SmsSend

sms = ghasedakpack.Ghasedak("426062d1eabeacda67797a915a44ac0d5ea8f552dba294c805d638f5796030ae")


class SmsView(FormView):
    template_name = 'sms_send/sms_send.html'
    form_class = SmsForm
    success_url = '/'
    def form_valid(self, form):
        cd = form.cleaned_data
        sms.verification({'receptor': cd['phone'] , 'type': '1','template': 'resinabeat','param1': cd['content']})
        SmsSend.objects.create(phone = cd['phone'] , content = cd['content'])
        return render(self.request , self.template_name , {'form':form})



