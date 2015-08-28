# -*- encoding: utf-8 -*-
'''
Created on May 28, 2015

@author: pta
'''
from django.contrib.admin.options import TabularInline, ModelAdmin,\
    StackedInline
from quiz.models import CaThi, Lop, MonThi, SinhVien, QuestionGroup, Question,\
    QuestionGroup_Setting, Answer, MCQuestion, EssayQuestion, TFQuestion, Chapter_Setting,\
    DonVi, GiaoVien

from django.contrib import admin
from django.forms.models import ModelForm, ModelMultipleChoiceField
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class AnswerInLine(TabularInline):
    model = Answer
    
class SinhVienInLine(TabularInline):
    model = SinhVien;
#     fields = ('ma_sv', 'ho_ten', 'gioi_tinh', 'ngay_sinh', 'que_quan')
    fields = ('ma_sv', 'ho_ten')
    
class DSSinhVienThiInLine(TabularInline):
    model=CaThi.ds_sv_thi.through
#     fields=('ds-sv_thi.ma_sv', 'ho_ten', 'lop')
        
    
class QuestionGroup_SettingInLine(TabularInline):
    model = QuestionGroup_Setting
    fields=('question_group', 'question_type', 'mark_per_question', 'num_of_questions')

class Chapter_SettingInLine(TabularInline):
    model = Chapter_Setting
    fields=('chapter', 'num_of_questions')
    
# class CaThiAdminForm(ModelForm):
#     class Meta:
#         model = CaThi
#         exclude = [] 
#         
#     questions = ModelMultipleChoiceField(
#                 queryset=Question.objects.all().select_subclasses(),
#                 required = False,
# #                 verbose_name = "Danh sách câu hỏi",
#                 widget = FilteredSelectMultiple(
#                                                 verbose_name=u'Danh sách câu hỏi',
#                                                 is_stacked=False)
#                 )   
#     def __init__(self, *args, **kwargs):
#         super(CaThiAdminForm, self).__init__(*args, **kwargs)
#         if self.instance.pk:
#             self.fields['questions'].initial =\
#                 self.instance.question_set.all().select_subclasses()
#     
#     def save(self, commit=True):
#         cathi = super(CaThiAdminForm, self).save(commit=False)
#         cathi.save()
#         cathi.question_set = self.cleaned_data['questions']
#         self.save_m2m()
#         return cathi
    
class CaThiAdmin(ModelAdmin):
#     form = CaThiAdminForm
    model = CaThi;
    list_display = ('title', 'mon_thi', 'description')
    fields=('title', 'mon_thi', 'ngay_thi', 
            'tg_bat_dau', 'tg_ket_thuc', 'pass_mark','tao_moi_de_thi',
            'description')
    exclude=('ds_sv_thi',)
    inlines = [QuestionGroup_SettingInLine, Chapter_SettingInLine, DSSinhVienThiInLine]
    
class LopAdmin(ModelAdmin):
    model=Lop
    
    inlines = [SinhVienInLine]
    
class MonThiAdmin(ModelAdmin):
    model=MonThi
    
# class SinhVienInline(StackedInline):
#     model = SinhVien
#     can_delete = False
#     verbose_name_plural = "Sinh vien"
    
class DonViAdmin(ModelAdmin):
    model = DonVi
    
class GiaoVienAdmin(ModelAdmin):
    model = GiaoVien
    fields = ('ma_so', 'ho_ten', 'don_vi')
    list_display=('ma_so','ho_ten','don_vi')
    search_fields=('ho_ten',)
    list_filter = ('don_vi',)
    
class SinhVienAdmin(ModelAdmin):
    model = SinhVien
    
    fields = ('ma-sv', 'ho_ten')
    list_display = ('ma_sv', 'ho_ten')
    search_fields = ('ho_ten',)
    list_filter = ('lop',)

    
class QuestionGroupAdmin(ModelAdmin):
    model = QuestionGroup
     
    
class MCQuestionAdmin(ModelAdmin):
    model=MCQuestion
    
    list_display = ('id', 'mon_thi', 'content', )
    list_filter = ('mon_thi',)
    fields = ('mon_thi', 'content',
              'figure', 'question_group' )

    search_fields = ('content',)
#     filter_horizontal = ('ca_thi',)
    
    inlines = [AnswerInLine]
    
    
    
class TFQuestionAdmin(ModelAdmin    ):
    model = TFQuestion
    list_display = ('mon_thi', 'content', 'is_correct')
    fields = ('mon_thi', 'content',
              'figure', 'question_group', 'is_correct' )
    list_filter = ('mon_thi',)
    
class EssayQuestionAdmin(ModelAdmin):
    model = EssayQuestion
    list_display=('mon_thi', 'content',)
    list_filter = ('mon_thi',)
    fields = ('mon_thi', 'content',
              'figure', 'question_group', 'answer' )
    
    
admin.site.register(DonVi, DonViAdmin)
admin.site.register(GiaoVien, GiaoVienAdmin)
admin.site.register(CaThi, CaThiAdmin)
admin.site.register(Lop, LopAdmin)
admin.site.register(MonThi, MonThiAdmin)

admin.site.register(SinhVien, SinhVienAdmin)
# admin.site.unregister(User)
# admin.site.register(User, SinhVienAdmin)
admin.site.register(QuestionGroup, QuestionGroupAdmin)
admin.site.register(MCQuestion, MCQuestionAdmin)
admin.site.register(TFQuestion, TFQuestionAdmin)
admin.site.register(EssayQuestion, EssayQuestionAdmin)


    