from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from hijri_converter import convert


class HijriGregorianConverterApp(App):
    def build(self):
        self.title = 'Конвертер Хиджра-Григорианский'

        layout = BoxLayout(orientation='vertical')

        self.hijri_input = TextInput(hint_text='Введите дату по Хиджре (ГГГГ-ММ-ДД)')
        self.gregorian_input = TextInput(hint_text='Введите дату по Григорианскому календарю (ГГГГ-ММ-ДД)')

        hijri_to_gregorian_btn = Button(text='Конвертировать Хиджру в Григорианский')
        gregorian_to_hijri_btn = Button(text='Конвертировать Григорианский в Хиджру')

        hijri_to_gregorian_btn.bind(on_press=self.convert_hijri_to_gregorian)
        gregorian_to_hijri_btn.bind(on_press=self.convert_gregorian_to_hijri)

        self.result_label = Label(text='Результат будет отображен здесь')

        layout.add_widget(self.hijri_input)
        layout.add_widget(hijri_to_gregorian_btn)
        layout.add_widget(self.gregorian_input)
        layout.add_widget(gregorian_to_hijri_btn)
        layout.add_widget(self.result_label)

        return layout

    def format_gregorian_date(self, date):
        days_of_week = {
            'Monday': 'Понедельник',
            'Tuesday': 'Вторник',
            'Wednesday': 'Среда',
            'Thursday': 'Четверг',
            'Friday': 'Пятница',
            'Saturday': 'Суббота',
            'Sunday': 'Воскресенье'
        }
        months = {
            'January': 'Январь',
            'February': 'Февраль',
            'March': 'Март',
            'April': 'Апрель',
            'May': 'Май',
            'June': 'Июнь',
            'July': 'Июль',
            'August': 'Август',
            'September': 'Сентябрь',
            'October': 'Октябрь',
            'November': 'Ноябрь',
            'December': 'Декабрь'
        }
        day_name = days_of_week[date.strftime('%A')]
        day = date.day
        month_name = months[date.strftime('%B')]
        year = date.year
        return f'{day_name}, {day} {month_name} {year}'

    def format_hijri_date(self, hijri_date):
        days_of_week = ['Аль-Ахад', 'Аль-Итнaйн', 'Ас-Сулaса', 'Аль-Арбиъа', 'Аль-Хамис', 'Аль-Джумуа', 'Ас-Сабт']
        months = ['Мухаррам', 'Сафар', 'Раби уль-авваль', 'Раби уль-ахир', 'Джумадa аль-уля', 'Джумадa аль-ахира',
                  'Раджаб', 'Шаабан', 'Рамадан', 'Шавваль', 'Зуль-Каъда', 'Зуль-Хиджжа']
        day_of_week = days_of_week[hijri_date.to_gregorian().weekday()]
        day = hijri_date.day
        month = months[hijri_date.month - 1]
        year = hijri_date.year
        return f'{day_of_week}, {day} {month} {year} AH'

    def convert_hijri_to_gregorian(self, instance):
        hijri_date = self.hijri_input.text
        try:
            year, month, day = map(int, hijri_date.split('-'))
            hijri_date_obj = convert.Hijri(year, month, day)
            gregorian_date = hijri_date_obj.to_gregorian()
            formatted_date = self.format_gregorian_date(gregorian_date)
            self.result_label.text = f'Григорианская дата: {formatted_date}'
        except Exception as e:
            self.result_label.text = f'Ошибка: {str(e)}'

    def convert_gregorian_to_hijri(self, instance):
        gregorian_date = self.gregorian_input.text
        try:
            year, month, day = map(int, gregorian_date.split('-'))
            gregorian_date_obj = convert.Gregorian(year, month, day)
            hijri_date = gregorian_date_obj.to_hijri()
            formatted_date = self.format_hijri_date(hijri_date)
            self.result_label.text = f'Дата по Хиджре: {formatted_date}'
        except Exception as e:
            self.result_label.text = f'Ошибка: {str(e)}'


if __name__ == '__main__':
    HijriGregorianConverterApp().run()
