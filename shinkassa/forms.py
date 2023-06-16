from django import forms

from .models import Worktable

class WorktableForm(forms.ModelForm):

    class Meta:
        model = Worktable
        fields = ['company', 'vehicle', 'number', 'diametr', 'complex', 'balance', 'count_gruz',
                  'sn', 'ust', 'mont', 'demont', 'appworks', 'cost_appworks', 'prim'
                  ]
        labels = {'company': '__________Фирма',
                  'vehicle': 'Машина(марка)',
                  'number': '__________Номер',
                  'diametr': '_Размер диска',
                  'complex': '_____Комплекс',
                  'balance': 'Балансировка',
                  'count_gruz': 'Кол-во клеящ. пластин',
                  'sn': '________Снятие',
                  'ust': '_____Установка',
                  'mont': '_______Монтаж',
                  'demont': '_____Демонтаж',
                  'appworks': 'Дополнительная работа',
                  'cost_appworks': 'Стоимость доп. работы',
                  'prim': 'Примечание'

                  }