from django import forms


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.answers = kwargs.pop("answers")
        self.questions = kwargs.pop("questions")
        super(QuizForm, self).__init__(*args, *kwargs)
        choices = []
        for answer in self.answers:
            choices.append((answer, answer.answer_text))
        for number in range(3):
            field_name = f"question_{number+1}"
            self.fields[field_name].choices = choices
            self.fields[field_name].label = self.questions[number].question_text

    question_1 = forms.ChoiceField(widget=forms.RadioSelect)
    question_2 = forms.ChoiceField(widget=forms.RadioSelect)
    question_3 = forms.ChoiceField(widget=forms.RadioSelect)

