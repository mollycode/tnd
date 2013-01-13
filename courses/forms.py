from django.forms import ModelForm
from models import Course

class CourseRatingForm(ModelForm):

    class Meta:
        model = Course
        fields= ("rating",)

    def save(self, commit=True):
        course = super(CourseRatingForm, self).save(commit=False)
        course.rating = (self.rating + course.rating * course.num_rating) / (course.num_rating + 1)
        course.num_rating = course.num_rating + 1

        if commit:
            user.save()
        return user