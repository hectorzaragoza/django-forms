from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView
from .models import Review

# from .models import Review

# Create your views here.

# CreateView form to render form, validate a form, show errors if needed, and save data...clean and short.
class ReviewView(CreateView):
    model = Review
    fields = "__all__"
    template_name = "reviews/review.html"
    success_url = "/thank-you"

# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

    # def get(self, request):
    #     form = ReviewForm()

    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

    # def post(self, request):
    #     form = ReviewForm(request.POST)

    #     if form.is_valid():
    #         # review = Review(user_name=form.cleaned_data['user_name'], review_text=form.cleaned_data['review_text'], rating=form.cleaned_data['rating'])
    #         # review.save()
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
        
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })

# def review(request):
#     if request.method == 'POST':
        
    
#     else:
        
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This Works!"
        return context

# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    # override object_list to set your context as reviews
    context_object_name = "reviews"
    

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    