from django import forms


class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.answers = kwargs.pop("answers")
        super(QuizForm, self).__init__(*args, *kwargs)
        choices = []
        for answer in self.answers:
            choices.append((answer, answer.answer_text))
        self.fields["choice"].choices = choices

    choice = forms.ChoiceField(widget=forms.RadioSelect)

