'''
Created on Jun 8, 2015

@author: pta
'''
from django.http import HttpResponse
from django.contrib.auth.views import logout
from django.contrib.auth import authenticate, login
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from quiz.models import MonThi, CaThi, DeThi, Question, Answer, DeThiTuLuan,\
    CaThiTuLuan, NganHangDeThiTuLuan
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from datetime import date, datetime
from django.views.generic.detail import DetailView
# from numpy.distutils.from_template import template_name_re
from django.views.generic.list import ListView
import json
from quiz import ESSAYQUESTION, TFQUESTION
from django.utils.datastructures import MultiValueDictKeyError
from os.path import basename
import random

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login_user(request):
    logout(request)
    username = password = ''
    
#     ds_mothi = MonThi.objects.all();
    today = datetime.now().date()
    ds_cathi = CaThi.objects.filter(ngay_thi=today)
    template = loader.get_template('login.html')
    context = RequestContext(request, {
        'ds_cathi': ds_cathi,
    })
    
    if(request.POST):
        username = request.POST['username']
        password = request.POST['password']
        cathi_id = request.POST['cathi']
         
        user = authenticate(username=username, password=password)
         
        if user is not None:
            login(request, user)
            
            dethi = DeThi.objects.filter(sinh_vien__ma_sv=username, ca_thi=cathi_id)[0]
            return HttpResponseRedirect('/quiz/cathi/' + str(dethi.id) + '/')
         
    return HttpResponse(template.render(context))

def quiz_finish(request, pk):
    dethi = DeThi.objects.get(pk=pk)

    answers = {}
    
    if request.POST:
        questions = json.loads(dethi.ds_cau_hoi)
        for question in questions:
            q_id = str(question[0])
            try:
                answers[question[0]] = int(request.POST[q_id])
            except:
                continue
            
    dethi.user_answers = json.dumps(answers)
    
    dethi.save()
    return HttpResponse('Tinhs diem')

class CathiDetailView(DetailView):
    model = DeThi
    template_name='cathi_detail.html'
#     pk_url_kwarg = 'cathi'
    
#     def get(self, request, *args, **kwargs):
#         return DetailView.get(self, request, *args, **kwargs)


class DethiStartView(DetailView):
    model = DeThi
    template_name = 'dethi_start.html'
    
#     def get(self, request, *args, **kwargs):
#         object = DetailView.get(self, request, *args, **kwargs)
#         
#         context = self.get_context_data(object=self.object)
        
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        
                
        context['questions'] = self.object.get_ds_cau_hoi()
        
        return context
        
        
def view_pdf(request, pk):
    dt = DeThiTuLuan.objects.get(pk=pk)
    if dt:
        file_name = basename(dt.de_thi.path)
        pdf = open(dt.de_thi.path, 'r').read()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename=%s' %(file_name)
        return response
    else:
        return HttpResponse(u'No file %s' %(file_name))
    
class CaThiTuLuanView(DetailView):
    model = CaThiTuLuan
    template_name='cathituluan.html'
    
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, **kwargs)
        # neu da co de roi, thi khong sinh de moi nua
        dethi_tmp = self.object.ds_de_thi.all()
        if dethi_tmp and len(dethi_tmp)==self.object.so_de_thi:
            context['ds_de_thi'] = self.object.ds_de_thi.all()
            return context
        # lay tat ca ca thi cua cua hoc ky, cung doi tuong va mon thi
        same_cathi = CaThiTuLuan.objects.filter(nam_hoc=self.object.nam_hoc,
                                                hoc_ky=self.object.hoc_ky,
                                                doi_tuong=self.object.doi_tuong,
                                                mon_thi=self.object.mon_thi)
        de_da_thi = set()
        for ct in same_cathi:
            if ct != self.object:
                de_da_thi.update(set(ct.ds_de_thi.all()))
            
        # lay ngan hang de thi tuong ung voi doi_tuong va mon_thi
        ngan_hang = NganHangDeThiTuLuan.objects.filter(doi_tuong=self.object.doi_tuong, 
                                                          mon_thi=self.object.mon_thi)
        
        ngan_hang_dt = DeThiTuLuan.objects.filter(ngan_hang=ngan_hang[0])
        # tao danh sach de chua thi
        de_chua_thi = set(ngan_hang_dt).difference(de_da_thi)
        # lay so_de_thi
        de_thi_s = random.sample(de_chua_thi, self.object.so_de_thi)

        for de_thi in de_thi_s:
            self.object.ds_de_thi.add(de_thi)
                
        self.object.save()
        
        context['ds_de_thi'] = de_thi_s
        
        return context
    
def get_dt(request, pk):
    ca_thi = CaThiTuLuan.objects.get(pk=pk)
    
