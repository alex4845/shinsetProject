from django import forms

from .models import Worktable

class WorktableForm(forms.ModelForm):
    class Meta:
        model = Worktable
        fields = ['company', 'vehicle', 'number', 'diametr', 'complex', 'balance', 'count_gruz',
                  'sn', 'ust', 'mont', 'demont', 'appworks', 'cost_appworks', 'prim'
                  ]
        labels = {'company': 'Фирма',
                  'vehicle': 'Машина(марка)',
                  'number': 'Номер',
                  'diametr': 'Размер диска',
                  'complex': 'Комплекс',
                  'balance': 'Балансировка',
                  'count_gruz': 'Кол-во клеящ. пластин',
                  'sn': 'Снятие',
                  'ust': 'Установка',
                  'mont': 'Монтаж',
                  'demont': 'Демонтаж',
                  'appworks': 'Дополнительная работа',
                  'cost_appworks': 'Стоимость доп. работы',
                  'prim': 'Примечание'

                  }