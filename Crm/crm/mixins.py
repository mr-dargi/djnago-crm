from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from .models import Project_procedure
from account.models import User

# For creating view by customer (Customer stage 1 fields)
class CreateFieldMixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser or request.user.is_customer:
      self.fields = [
        "project_title",
        "rfp"
      ]
    else:
      return redirect("crm:home")
    
    return super().dispatch(request, *args,**kwargs)

# Customer stage 1 fields
class UpdateFieldStage1Mixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser or request.user.is_customer:
      self.fields = [
        "project_title",
        "rfp"
      ]
    else:
      return redirect("crm:home")
    
    return super().dispatch(request, *args,**kwargs)

# Customer stage 2 fields
class UpdateFieldStage2Mixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser or request.user.is_customer:
      self.fields = [
        "confirm_proposal",
        "description_reject_proposal"
      ]
    else:
      return redirect("crm:home")
    
    return super().dispatch(request, *args,**kwargs)

# Customer stage 3 fields
class UpdateFieldStage3Mixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser or request.user.is_customer:
      self.fields = [
        "contract_image"
      ]
    else:
      return redirect("crm:home")
    
    return super().dispatch(request, *args,**kwargs)

# Customer stage 4 fields
class UpdateFieldStage4Mixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser or request.user.is_customer:
      self.fields = [
        "payment_receipt_image"
      ]
    else:
      return redirect("crm:home")
    
    return super().dispatch(request, *args,**kwargs)

# Customer stage 5 fields
class UpdateFieldStage5Mixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser or request.user.is_customer:
      self.fields = [
        "confirm_design",
        "description_reject_design"
      ]
    else:
      return redirect("crm:home")
    
    return super().dispatch(request, *args,**kwargs)


# Saving form in database
class FormValidMixin():
  def form_valid(self, form):
    self.object = form.save()
    self.object.user = self.request.user
    
    return super().form_valid(form)

# Genral access mixin
class AccessMixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      if request.user.is_superuser or request.user.is_customer or request.user.is_manager:
        return super().dispatch(request, *args,**kwargs)
      else:
        return redirect("crm:home")
    else:
      return redirect("account:login")


class Genral_listView():
  def get_queryset(self):
    current_user = self.request.user
    if current_user.is_superuser:
      project_procedure = Project_procedure.objects.all()
      return project_procedure
    elif current_user.is_customer:
      project_procedure = Project_procedure.objects.filter(user = current_user.id )
      return project_procedure
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["User"] = User
    return context


class Customer_ListView():
  def get_queryset(self):
    current_user = self.request.user
    if current_user.is_superuser:
      project_procedure = Project_procedure.objects.all()
      return project_procedure
    elif current_user.is_customer:
      project_procedure = Project_procedure.objects.filter(user = current_user.id )
      return project_procedure
    else:
      raise Http404("این پیج برای شما قابل مشاهده نیست")
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["User"] = User
    return context


# support section
# support stage 7 fields
class UpdateFieldStage7Mixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser or request.user.is_manager:
      self.fields = [
        "proposal"
      ]
    else:
      return redirect("crm:home")
    
    return super().dispatch(request, *args,**kwargs)


# support stage 8 fields
class UpdateFieldStage8Mixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser or request.user.is_manager:
      self.fields = [
        "contract",
        "confirm_contract",
        "description_reject_contract"
      ]
    else:
      return redirect("crm:home")
    
    return super().dispatch(request, *args,**kwargs)


# support stage 9 fields
class UpdateFieldStage9Mixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_superuser or request.user.is_manager:
      self.fields = [
        "payment",
        "confirm_payment_receipt",
        "description_reject_payment_receipt"
      ]
    else:
      return redirect("crm:home")
    
    return super().dispatch(request, *args,**kwargs)


class Support_ListView():
  def get_queryset(self):
    current_user = self.request.user
    if current_user.is_superuser:
      project_procedure = Project_procedure.objects.all()
      return project_procedure
    elif current_user.is_manager:
      project_procedure = Project_procedure.objects.filter(support = current_user.id )
      return project_procedure
    else:
      raise Http404("این پیج برای شما قابل مشاهده نیست")
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["User"] = User
    return context


class SupportAccessMixin():
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_manager or request.user.is_superuser:
      return super().dispatch(request, *args,**kwargs)
    else:
      raise Http404("You can't see this page")