# -*- encoding: utf-8 -*-
default_app_config = "quiz.apps.QuizConfig"

TFQUESTION='TF'
MCQUESTION='MC'
ESSAYQUESTION='ESSAY'

HK1 = 'HK1'
HK2 = 'HK2'

QUESTION_TYPES=(
               (TFQUESTION, 'Câu hỏi Đúng - Sai'),
               (MCQUESTION, 'Câu hỏi Multiple Choice'),
               (ESSAYQUESTION, 'Câu hỏi tự luận'),
               )

TRANG_THAI_THI=(
                ('DA_THI', 'Đã thi'),
                ('VANG_CO_LD', 'Vắng có lý do'),
                ('VANG_KO_LD', 'Vắng không lý do'),
                )

ANSWER_ORDER_OPTIONS = (
    ('CONTENT', 'Nội dung'),
    ('RANDOM', 'Ngẫu nhiên'),
    ('NONE', 'None')
)

HOC_KY = (
          (HK1, 'Học kỳ 1'),
          (HK2, 'Học kỳ 2')
          )