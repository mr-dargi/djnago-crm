from django.shortcuts import redirect


# For creating ticket by customer
class CreateFieldMixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser or request.user.is_customer:
      self.fields = [
        "subject",
        "description"
      ]
    else:
      return redirect("crm:home")
    
    return super().dispatch(request, *args,**kwargs)


# Saving form in database
class FormValidMixin():
  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.customer = self.request.user
    self.object = form.save()
    
    return super().form_valid(form)