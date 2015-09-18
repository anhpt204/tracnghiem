# -*- encoding: utf-8 -*-

'''
Created on May 28, 2015

@author: pta
'''
from django.db import models
from django.db.models.fields import CharField,\
    PositiveIntegerField, TextField, DateField, DateTimeField, BooleanField,\
    CommaSeparatedIntegerField, TimeField, IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField,\
    OneToOneField
# from model_utils.managers import InheritanceManager
from django.utils.encoding import python_2_unicode_compatible
from tracnghiem import settings
from django.contrib.auth.models import User
from django.forms.fields import ChoiceField
from random import sample
import json
from quiz import *
from smart_selects.db_fields import ChainedForeignKey
from datetime import datetime, date
import random
from django.utils import timezone

class DonVi(models.Model):
    ma_dv = CharField(verbose_name="Mã đơn vị", unique = True, max_length=5,
                      help_text="Mã đơn vị không quá 5 ký tự")
    ten_dv = CharField(verbose_name="Tên đơn vị", unique=True, max_length=200)
    
    cha_dv = ForeignKey("DonVi", verbose_name="Đơn vị cấp trên", null=True, blank=True,
                        help_text="Đơn vị cấp trên trực tiếp")
    
    class Meta:
        verbose_name = "Đơn vị"
        verbose_name_plural =   "Danh sách đơn vị"
        
    def __unicode__(self):
        if self.cha_dv:
            return u'%s - %s' %(self.ten_dv, self.cha_dv)
        else:
            return u'%s' %(self.ten_dv)
    
class DoiTuong(models.Model):
    ma_dt = CharField(unique=True, max_length=10,
                      verbose_name="Mã đối tượng")
                      
    ma_dt.help_text = "Mã không quá " + str(ma_dt.max_length)+" ký tự"
    
    ten_dt = CharField(unique=True, max_length=50,
                       verbose_name = 'Tên đối tượng')
    
    class Meta:
        verbose_name="Đối tượng"
        verbose_name_plural="Danh sách đối tượng"
        
    def __unicode__(self):
        return u'%s(%s)' %(self.ten_dt, self.ma_dt)
    
# @python_2_unicode_compatible
class MonThi(models.Model):
    ma_mon_thi = CharField(verbose_name = "Mã môn thi", unique = True, max_length=10)
    ten_mon_thi = CharField(verbose_name = "Môn thi", unique=True,max_length=200) 
    
    class Meta:
        verbose_name = "Môn thi"
        verbose_name_plural = "Danh sách môn thi"
        
    def __unicode__(self):
        return u'%s' %(self.ten_mon_thi)
     
# @python_2_unicode_compatible
class Lop(models.Model):
    ma_lop = CharField(verbose_name="Mã lớp", unique=True, max_length=5)
    ten_lop = CharField(verbose_name = "Lớp", unique=True, max_length=200)
    si_so = PositiveIntegerField(verbose_name="Sĩ số", blank=True,null=True)
    doi_tuong = ForeignKey(DoiTuong, verbose_name="Đối tượng", 
                           blank=False, null=False)

    class Meta:
        verbose_name = "Lớp"
        verbose_name_plural = "Danh sách lớp"
    
    def __unicode__(self):
        return u'%s' %(self.ten_lop)
    
    

class SinhVien(models.Model):
    user = OneToOneField(User)
    ma_sv=PositiveIntegerField(blank=False, null=False,
                               unique=True,
                               verbose_name="Mã sinh viên")
    ho_ten = CharField(blank=False, null=False,
                       max_length=50,
                       verbose_name="Họ và tên")
    lop = ForeignKey(Lop, blank=False, null=False,
                     verbose_name="Lớp")
    # tam the da, co the can them cac truong khac
    

    class Meta:
        verbose_name = "Sinh viên"
        verbose_name_plural = "Danh sách sinh viên"

    def __unicode__(self):
        return u'%s-%s' %(self.ho_ten, self.lop.ma_lop)
    
    def save(self, *args, **kwargs):
        '''
        when save a student, we also make a user who can login to make exam
        '''
#         print self.ma_sv
        u = User.objects.filter(username=self.ma_sv)
        if len(u) == 0: 
            new_user = User.objects.create_user(username=self.ma_sv, password=self.ma_sv)
            new_user.is_staff = True
            new_user.save()
            self.user = new_user
        else:
            self.user = u[0];
        super(SinhVien, self).save(*args, **kwargs)
        
    def delete(self, using=None):
        '''
        also delete from user table
        '''
        user = User.objects.get_by_natural_key(self.ma_sv)
        User.delete(user, using)
        models.Model.delete(self, using=using)
        
class GiaoVien(models.Model):
    user = OneToOneField(User)
    
    ma_so=PositiveIntegerField(blank=False, null=False,
                               unique=True,
                               verbose_name="Mã số")
    
    ho_ten = CharField(blank=False, null=False,
                       max_length=50,
                       verbose_name="Họ và tên")
    
    don_vi = ForeignKey(DonVi, verbose_name='Đơn vị', help_text="Đơn vị quản lý trực tiếp")
    
#     lop = ForeignKey(Lop, blank=False, null=False,
#                      verbose_name="Lớp")
    # tam the da, co the can them cac truong khac
    

    class Meta:
        verbose_name = "Giáo viên"
        verbose_name_plural = "Danh sách giáo viên"

    def __unicode__(self):
        return u'%s (%s)' %(self.ho_ten, self.don_vi)
    
    def save(self, *args, **kwargs):
        '''
        when save a student, we also make a user who can login to make exam
        '''
        u = 'GV'+str(self.ma_so)
        # check if this GV already exist in user table
        users = User.objects.filter(username=u)
        # if not
        if len(users) == 0:
            # then create a new user 
            new_user = User.objects.create_user(username=u, password=self.ma_so)
            new_user.is_staff = True
            new_user.save()
            self.user = new_user
        else:
            self.user = users[0];
        super(GiaoVien, self).save(*args, **kwargs)
        
    def delete(self, using=None):
        '''
        also delete from user table
        '''
        user = User.objects.get_by_natural_key(self.ma_so)
        User.delete(user, using)
        models.Model.delete(self, using=using)
        
class Diem(models.Model):
    sinh_vien=ForeignKey(SinhVien,
                         blank=False, null=False, 
                         verbose_name="Sinh viên")
    mon_thi = ForeignKey(MonThi,
                         blank=False, null=False,
                         verbose_name="Môn thi")
    
    trang_thai_thi = CharField(max_length=20,
                               choices=TRANG_THAI_THI,
                               default='DA_THI',
                               verbose_name='Trạng thái thi')
    
    diem=CommaSeparatedIntegerField(max_length=5, blank=True, null=True,
                              verbose_name="Điểm")
    class Meta:
        unique_together = (('sinh_vien', 'mon_thi'),)
        verbose_name = "Điểm"
        verbose_name_plural = "Bảng điểm"

# @python_2_unicode_compatible
class QuestionGroup(models.Model):
    name = CharField(verbose_name="Nhóm câu hỏi", 
                     blank=False,null=False,
                     unique=True,
                     max_length=50)
    description = TextField(verbose_name = "Ghi chú", blank=True, null=True)
    
    class Meta:
        verbose_name = "Nhóm câu hỏi"
        verbose_name_plural = "Danh sách nhóm câu hỏi"

    def __unicode__(self):
        return u'%s-%s' %(self.name, self.description)

class Lop_CaThi(models.Model):
    '''
    Dinh nghia mot lop cho moi ca thi, lop_cathi co the la ket hop cua nhieu lop
    hoac mot so sinh vien. Thich hop cho viec ghep lop thi, thi lai,...
    '''
    lop = ForeignKey(Lop, 
                     verbose_name="Lớp thi")
    
#     ds_sinhvien = ChainedForeignKey(SinhVien,
#                                     chained_field='lop',
#                                     chained_model_field='lop',
#                                     show_all=True,
#                                     auto_choose=False)
    
    ds_sinhvien = ManyToManyField(SinhVien)

class CaThi(models.Model):
    '''
    Thiet lap mot ca thi, trong do co danh sach cau hoi de tu do lam
    cac de thi cho tung sinh vien
    '''
    title = CharField(verbose_name="Ca thi", max_length=200, blank=False)
    
    description=TextField(verbose_name="Ghi chú", blank=True, null=True)
    mon_thi = ForeignKey(MonThi, blank=False, null=False,
                         verbose_name="Môn thi")
#     lop_thi = ForeignKey(Lop, blank=False, null=False,
#                          verbose_name="Lớp thi")
#     ds_thisinh = ForeignKey(Lop_CaThi, blank=False, null=False, 
#                          verbose_name="Danh sách thí sinh")
    ds_giamthi = ManyToManyField(GiaoVien, verbose_name=u'Danh sách giám thị coi thi')
    
    ds_thisinh = ManyToManyField(SinhVien, blank=False, 
                                verbose_name=u"Danh sách thí sinh")
    ds_thisinh.help_text = 'Tìm kiếm theo họ tên sinh viên hoặc mã lớp.'
    
    ngay_thi = DateField(verbose_name="Ngày thi")
    tg_bat_dau=TimeField(verbose_name="Thời gian bắt đầu")
    tg_ket_thuc=TimeField(verbose_name="Thời gian kết thúc")
    
    ds_cau_hoi = CommaSeparatedIntegerField(max_length=1024, 
                                            verbose_name="Danh sach cau hoi (ids)")
#     setting = ManyToManyField(QuestionGroup_Setting, 
#                             verbose_name="Thiết lập cấu hình ca thi")
    tao_moi_de_thi = BooleanField(blank=False, null=False,
                                  verbose_name="Tạo mới đề thi cho các sinh viên",
                                  default=True)
    
    random_order = BooleanField(blank=False, null=False,
                                verbose_name="Hiển thị câu hỏi ngẫu nhiên",
                                default=True)
    answers_at_end = BooleanField(blank=False, null=False,
                                  verbose_name="Hiển thị câu trả lời khi kết thúc",
                                  default=False)
    result_at_end = BooleanField(blank=False, null=False,
                               verbose_name="Hiển thị kết quả khi kết thúc",
                               default=True)
    exam_paper = BooleanField(blank=False, null=False,
                              verbose_name="Lưu bài thi",
                              default=True)
    single_attempt = BooleanField(blank=False, null=False,
                                  verbose_name="Mỗi người một đề thi",
                                  default=True)
    pass_mark = PositiveIntegerField(verbose_name="Điểm đạt yêu cầu")
    success_text = TextField(blank=True,
                             verbose_name="Thông báo được hiển thị nếu thí sinh vượt qua")
    fail_text = TextField(blank=True,
                          verbose_name="Thông báo được hiển thị nếu thí sinh không vượt qua")
    draft=BooleanField(verbose_name="Bản nháp", 
                       default=False)
    
    class Meta:
        verbose_name = "Ca thi"
        verbose_name_plural = "Danh sách ca thi"

    def __unicode__(self):
        return u'%s' %(self.title)
    
    def save(self, *args, **kwargs):
        # luu CaThi va Cathi_Setting
#         super(CaThi, self).save(*args, **kwargs)
#         # lay danh sach cau hoi cho ca thi
#         # lay cathi_setting
        questionGroup_settings = QuestionGroup_Setting.objects.filter(ca_thi__exact=self)
#         # cac cau hoi cua de thi
        questions = []
        for cathi_setting in questionGroup_settings:
            # lay cau hoi theo nhom va loai (type)
            qs = Question.objects.filter(mon_thi=self.mon_thi,
                                    question_type = cathi_setting.question_type,
                                    question_group = cathi_setting.question_group)
            # lay id
            q_ids = qs.values_list('id', flat=True)
            # lay ngau nhien so cau hoi
             
            questions += sample(q_ids, cathi_setting.num_of_questions)
         
        self.ds_cau_hoi = ','.join(map(str, questions)) + ","
         
        # luu CaThi-ds_cauhoi
        super(CaThi, self).save(*args, **kwargs)
        # tao de thi cho tung sinh vien
 
        # lay danh sach sinh vien cua lop
#         dsSV = SinhVien.objects.filter(lop=self.lop_thi)
        dsSV = self.ds_thisinh.all()
         
        if(self.tao_moi_de_thi == False):
            return
         
        # voi moi sinh vien, tao mot de thi
        for sv in dsSV:
            # tao de thi
            dethi = DeThi.objects.update_or_create(sinh_vien=sv,
                                                   ca_thi=self,
                                                   )[0]
            # lay ngau nhien cau hoi trong ngan hang de
            ds_cauhoi = sample(questions, len(questions))
            ds_cauhoi_answer = []
            for cauhoi_id in ds_cauhoi:
                # lay cau hoi voi id tuong ung
                q = Question.objects.get(id=cauhoi_id)
                # neu cau hoi la multichoice question thi hoan doi thu tu
                # cau tra loi
                if q.question_type == MCQUESTION:
                    # lay cac cau tra loi cua cau hoi nay
#                     q = (MCQuestion)q
                     
#                     answers = Answer.objects.filter(question=q.id)
                    q.__class__ = MCQuestion
                    answers = q.getAnswers()
                     
                    # lay id cua cac cau hoi
                    answer_ids = answers.values_list('id', flat=True)
                     
                    # dao thu tu cau tra loi
                    answer_ids = sample(answer_ids, len(answer_ids))
                     
                    # add vao mot dictionary
                    ds_cauhoi_answer.append((cauhoi_id, answer_ids))
                 
                elif q.question_type == TFQUESTION:
                    ds_cauhoi_answer.append((cauhoi_id, [1, 0]))
                 
                else:
                    ds_cauhoi_answer.append((cauhoi_id, []))
                     
            dethi.ds_cau_hoi =  json.dumps(ds_cauhoi_answer)
            dethi.save()                             
            
class QuestionGroup_Setting(models.Model):
    ca_thi = ForeignKey(CaThi, verbose_name="Ca thi")
    
    question_group = ForeignKey(QuestionGroup, 
                                verbose_name="Nhóm câu hỏi")
    
    question_type = CharField(max_length=5,
                            choices=QUESTION_TYPES,
                            default=MCQUESTION,
                            verbose_name="Loại câu hỏi")
    
    mark_per_question = PositiveIntegerField(verbose_name="Điểm cho mỗi câu hỏi", 
                                             default=1) 
    num_of_questions = PositiveIntegerField(verbose_name="số câu hỏi",
                                            default=1)
    
    class Meta:
        verbose_name = "Cấu hình ca thi"
        verbose_name_plural = "Cấu hình ca thi"
#         managed=False
        
    def __unicode__(self):
        return u'%s:%s:%s' %(self.question_group.name,
                             self.num_of_questions,
                             self.mark_per_question)

class Chapter_Setting(models.Model):
    ca_thi = ForeignKey(CaThi, verbose_name="Ca thi")
            
    chapter = PositiveIntegerField(verbose_name="Chương", 
                                             default=1,
                                             help_text="ví dụ: 1,2,...") 
    num_of_questions = PositiveIntegerField(verbose_name="số câu hỏi",
                                            default=1)
    
    class Meta:
        verbose_name = "Thiết lập số câu hỏi cho từng chương"
        verbose_name_plural = "Thiết lập số câu hỏi cho từng chương"
#         managed=False
        
    def __unicode__(self):
        return u'%s:%s' %(self.chapter,
                             self.num_of_questions)
    
            
class Question(models.Model):
    '''
    base class for all other type of questions
    shared all properties
    '''
    ca_thi = ManyToManyField(CaThi, 
                        blank=True,
                        verbose_name="Ca thi")
    mon_thi = ForeignKey(MonThi,
                         blank=False, null=False,
                         verbose_name="Môn thi")
    question_group = ForeignKey(QuestionGroup,
                                blank=False, null=False,
                                verbose_name="Nhóm câu hỏi")
    question_type = CharField(max_length=5,
                              choices=QUESTION_TYPES,
                            default=MCQUESTION,
                            verbose_name="Loại câu hỏi")
    
    chapter = PositiveIntegerField(verbose_name="Chương", default=1)
    
    figure = models.ImageField(upload_to='uploads/%Y/%m/%d',
                               blank=True,
                               null=True,
                               verbose_name=("Ảnh"))

    content = models.TextField(max_length=1000,
                               blank=False,
                               verbose_name='Câu hỏi')

#     explanation = models.TextField(max_length=2000,
#                                    blank=True,
#                                    help_text=_("Explanation to be shown "
#                                                "after the question has "
#                                                "been answered."),
#                                    verbose_name=_('Explanation'))

#     objects = InheritanceManager()
    
    class Meta:
        verbose_name = "Câu hỏi"
        verbose_name_plural = "Danh sách câu hỏi"
    
    def __unicode__(self):
        return u'%s' %(self.content)
    
    def getAnswers(self):
        pass


class MCQuestion(Question):
    answer_order = CharField(
        max_length=30, null=True    , blank=True,
        choices=ANSWER_ORDER_OPTIONS,
#         help_text=_("The order in which multichoice "
#                     "answer options are displayed "
#                     "to the user"),
        verbose_name="Thứ tự hiển thị câu trả lời")
    
    def save(self, *args, **kwargs):
        self.question_type = MCQUESTION
        super(MCQuestion, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Câu hỏi loại Multiple choice"
        verbose_name_plural = "Danh sách câu hỏi loại Multiple choice"
        
    def getAnswers(self):
        return Answer.objects.filter(question=self.id)

class Answer(models.Model):
    question = ForeignKey(MCQuestion, verbose_name="Câu hỏi")

    content = CharField(max_length=1000,
                               blank=False,
#                                help_text=_("Enter the answer text that "
#                                            "you want displayed"),
                               verbose_name="Phương án trả lời")

    is_correct = BooleanField(blank=False,
                                  default=False,
                                  help_text="Phương án đúng?",
                                  verbose_name="Là phương án đúng")

    def __unicode__(self):
        return u'%s' %(self.content)

    class Meta:
        verbose_name = "Phương án trả lời"
        verbose_name_plural = "Danh sách phương án trả lời"

class EssayQuestion(Question):
    answer = TextField(blank=False, null=False,
                       verbose_name="Trả lời")
    
    def save(self, *args, **kwargs):
        self.question_type = ESSAYQUESTION
        super(EssayQuestion, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Câu hỏi tự luận"
        verbose_name_plural = "Danh sách câu hỏi tự luận"
        
class TFQuestion(Question):
    is_correct = BooleanField(blank=False,
                                  default=False,
                                  verbose_name="Là đáp án đúng?")
    
    def save(self, *args, **kwargs):
        self.question_type = TFQUESTION
        super(TFQuestion, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = "Câu hỏi Đúng/Sai"
        verbose_name_plural = "Danh sách câu hỏi Đúng/Sai"
        ordering = ['mon_thi']
        
        
class DeThi(models.Model):
    sinh_vien = ForeignKey(SinhVien,
                           blank=False,
                           null=False,
                           verbose_name="Sinh Viên")
    ca_thi = ForeignKey(CaThi,
                        blank=False, null=False,
                        verbose_name="Ca thi")
    
    ds_cau_hoi = TextField(blank=False, null=False,
                           default={}, 
                           verbose_name="Danh sach cau hoi")
    
    user_answers = TextField(blank=True, default={},
                             verbose_name ="Danh sach cau tra loi cua thi sinh")
    
    complete = BooleanField(default=False, blank=False,
                            verbose_name = "Da hoan thanh bai thi chua?")
    
    start = models.DateTimeField(auto_now_add=True,
                                 verbose_name="Bat dau luc")

    end = models.DateTimeField(null=True, blank=True, 
                               verbose_name="Ket thuc luc")

    diem = PositiveIntegerField(default=0, blank=False,
                                verbose_name="Diem thi")
    
    def get_ds_cau_hoi(self):
        ds_cau_hoi = json.loads(self.ds_cau_hoi)
        
        questions = []
        
        for cau_hoi in ds_cau_hoi:
            # get cau hoi
            q = Question.objects.get(id=cau_hoi[0])

            # get cau tra loi            
            if q.question_type == ESSAYQUESTION:
                questions.append((q, []))
            elif q.question_type == TFQUESTION:
                questions.append((q,[True, False]))
            else:
                # get mc answers
                answers = Answer.objects.filter(question__exact=q.id)
                questions.append((q, answers))
                
        return questions
    
class NganHangDeThiTuLuan(models.Model):
    ma_so = CharField(max_length=20, unique=False, blank=True, null=True,
                    verbose_name="Mã bộ đề")
    
    doi_tuong = ForeignKey(DoiTuong,
                           blank=False, null=False,
                           verbose_name="Đối tượng thi")
    
    mon_thi = ForeignKey(MonThi,
                         blank=False, null=False,
                         verbose_name="Môn thi")
    ngay_tao = models.DateField('Ngày tạo', default=timezone.now)
    
    class Meta:
        verbose_name='Bộ đề thi tự luận'
        verbose_name_plural="Bộ đề thi tự luận"
    
    def __unicode__(self):
        return u'%s(%s)' %(self.mon_thi, self.doi_tuong)
    
    
    def save(self, *args, **kwargs):
        self.ma_so = '%s.%s.%s.%s.%s' %(self.doi_tuong.ma_dt, self.mon_thi.ma_mon_thi,
                                        self.ngay_tao.day, self.ngay_tao.month, self.ngay_tao.year)
        
        super(NganHangDeThiTuLuan, self).save(*args, **kwargs)
        # ma = ma doi tuong.ma mon.ngay.thang.nam
    
class DeThiTuLuan(models.Model):
    '''
    The hien cho 1 de thi tu luan
    '''
    ngan_hang = models.ForeignKey(NganHangDeThiTuLuan,
                                  verbose_name="Ngân hàng")
    
    ma_de_thi = models.CharField(max_length=10, #unique=True,
                                 verbose_name="Mã đề thi")
    
    de_thi = models.FileField(upload_to='uploads/essay/%Y/%m/%d',
                               blank=True,
                               null=True,
                               verbose_name=("Đề thi"))
    dap_an = models.FileField(upload_to='uploads/essay/%Y/%m/%d',
                               blank=True,
                               null=True,
                               verbose_name=("Đáp án"))
    class Meta:
        verbose_name="Đề thi tự luận"
        verbose_name_plural="Danh sách đề thi tự luận"
        
    def __unicode__(self):
        return u'%s (%s)' %(self.ma_de_thi, self.ngan_hang)
    
class CaThiTuLuan(models.Model):
    ten_ca_thi = CharField(max_length=100,
                           verbose_name="Tiêu đề ca thi")
    
    nam_hoc = CharField(max_length=9,
                        verbose_name="Năm học",
                        help_text="Nhập năm học theo định dạng XXXX-XXXX. Ví dụ 2015-2016")
    
    hoc_ky = CharField(max_length=3,
                              choices=HOC_KY,
                            default=HK1,
                            verbose_name="Học kỳ")

    doi_tuong = ForeignKey(DoiTuong,
                           verbose_name="Đối tượng")
    
    mon_thi = ForeignKey(MonThi,
                         verbose_name = "Môn thi")
    
    lop = ForeignKey(Lop,
                     verbose_name = "Lớp")

    ngay_thi = DateField(verbose_name="Ngày thi")
#     
    giam_thi = ManyToManyField(GiaoVien, blank=False, 
                              verbose_name=u'Danh sách giám thị coi thi')

#     giam_thi = ManyToManyField(GiaoVien, blank=False,
#                                 verbose_name = u'GT')
    
    so_de_thi = PositiveIntegerField(verbose_name = "Số đề thi",
                                     default=1,
                                     help_text = u"Số đề thi là số nguyên dương, lớn hơn 0")
    ds_de_thi = ManyToManyField(DeThiTuLuan, blank=True,
                                verbose_name = u'DT')

    class Meta:
        verbose_name = u"Kế hoạch thi - bốc đề"
        verbose_name_plural = u"Kế hoạch thi - bốc đề"

    def __unicode__(self):
        return u'%s-%s-%s' %(self.doi_tuong, self.mon_thi, self.lop)
    
#     def save(self, *args, **kwargs):
#         # lay ngan hang de thi tuong ung voi doi_tuong va mon_thi
#         ngan_hang_dt = NganHangDeThiTuLuan.objects.filter(doi_tuong=self.doi_tuong, 
#                                                           mon_thi=self.mon_thi)
#         # lay so_de_thi
#         de_thi_s = random.sample(ngan_hang_dt, self.so_de_thi)
#         for de_thi in de_thi_s:
#             self.ds_de_thi.add(de_thi)
#         super(CaThiTuLuan, self).save(*args, **kwargs)