from django.shortcuts import render

from suggestions.forms import SuggestionForm

def suggestion(request):
    td = {}
    
    if request.POST:
        suggestion_form = SuggestionForm(request.POST)
        if suggestion_form.is_valid():
            if request.user:
                suggestion = suggestion_form.save(commit = False)
                suggestion.user = request.user
                suggestion.save()
            else:
                suggestion_form.save()
            return render(request, "thanks.html")
    else:
        suggestion_form = SuggestionForm()
        
    td["suggestion_form"] = suggestion_form
    
    return render(request, "suggestions.html", td)