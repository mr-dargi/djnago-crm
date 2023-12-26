from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .mixins import (
                      FormValidMixin,
                      CreateFieldMixin,
                      AccessMixin,
                      UpdateFieldStage1Mixin,
                      UpdateFieldStage2Mixin,
                      UpdateFieldStage3Mixin,
                      UpdateFieldStage4Mixin,
                      UpdateFieldStage5Mixin,
                      UpdateFieldStage7Mixin,
                      UpdateFieldStage8Mixin,
                      UpdateFieldStage9Mixin,
                      Customer_ListView,
                      Genral_listView,
                      Support_ListView
                    )
# from django.urls import reverse_lazy
from django.views.generic import (
                                    ListView, 
                                    DetailView, 
                                    CreateView, 
                                    UpdateView
                                  )
from .models import Project_procedure

# Create your views here.

# This view will show all the item in the project in one list
class ProjectList(LoginRequiredMixin, Genral_listView, ListView):
  template_name = "crm/index.html"


# This view will show stage one item that i describe in database model in the list
class ProjectList_stage1(LoginRequiredMixin, Customer_ListView, ListView):
  template_name = "crm/project_listView_stage_1.html"


# This view will show stage two item that i describe in database model in the list
class ProjectList_stage2(LoginRequiredMixin, Customer_ListView, ListView):
  template_name = "crm/project_listView_stage_2.html"


# This view will show stage four item that i describe in database model in the list
class ProjectList_stage3(LoginRequiredMixin, Customer_ListView, ListView):
  template_name = "crm/project_listView_stage_3.html"


# This view will show stage four item that i describe in database model in the list
class ProjectList_stage4(LoginRequiredMixin, Customer_ListView, ListView):
  template_name = "crm/project_listView_stage_4.html"


# This view will show stage four item that i describe in database model in the list
class ProjectList_stage5(LoginRequiredMixin, Customer_ListView, ListView):
  template_name = "crm/project_listView_stage_5.html"


# This view will create project that's we want it from customer
class ProjectCreate(AccessMixin, CreateFieldMixin, FormValidMixin, CreateView):
  model = Project_procedure
  success_url = reverse_lazy("crm:ProjectList-stage1")
  template_name = "crm/create_project.html"


# This view will update record of table that create with model (Project_procedure) 
# the fields are title and rfp
class ProjectUpdate_stage1(AccessMixin, UpdateFieldStage1Mixin, FormValidMixin, UpdateView):
  model = Project_procedure
  success_url = reverse_lazy("crm:ProjectList-stage1")
  template_name = "crm/project_update_stage_1.html"


# This view will update record of table that create with model (Project_procedure) 
# the fields are confirm_proposal and description_reject_proposal
class ProjectUpdate_stage2(AccessMixin, UpdateFieldStage2Mixin, FormValidMixin, UpdateView):
  model = Project_procedure
  success_url = reverse_lazy("crm:ProjectList-stage2")
  template_name = "crm/project_update_stage_2.html"


# This view will update record of table that create with model (Project_procedure) 
# the fields are contract_image
class ProjectUpdate_stage3(AccessMixin, UpdateFieldStage3Mixin, FormValidMixin, UpdateView):
  model = Project_procedure
  success_url = reverse_lazy("crm:ProjectList-stage3")
  template_name = "crm/project_update_stage_3.html"


# This view will update record of table that create with model (Project_procedure) 
# the fields are payment_receipt_image
class ProjectUpdate_stage4(AccessMixin, UpdateFieldStage4Mixin, FormValidMixin, UpdateView):
  model = Project_procedure
  success_url = reverse_lazy("crm:ProjectList-stage4")
  template_name = "crm/project_update_stage_4.html"


# This view will update record of table that create with model (Project_procedure) 
# the fields are confirm_design and description_reject_design
class ProjectUpdate_stage5(AccessMixin, UpdateFieldStage5Mixin, FormValidMixin, UpdateView):
  model = Project_procedure
  success_url = reverse_lazy("crm:ProjectList-stage5")
  template_name = "crm/project_update_stage_5.html"


class ProjectList_stage6(LoginRequiredMixin, Support_ListView, ListView):
  template_name = "crm/project_listView_stage_6.html"


class ProjectList_stage7(LoginRequiredMixin, Support_ListView, ListView):
  template_name = "crm/project_listView_stage_7.html"


class ProjectList_stage8(LoginRequiredMixin, Support_ListView, ListView):
  template_name = "crm/project_listView_stage_8.html"


class ProjectList_stage9(LoginRequiredMixin, Support_ListView, ListView):
  template_name = "crm/project_listView_stage_9.html"


class ProjectUpdate_stage7(AccessMixin, UpdateFieldStage7Mixin, FormValidMixin, UpdateView):
  model = Project_procedure
  success_url = reverse_lazy("crm:ProjectList-stage7")
  template_name = "crm/project_update_stage_7.html"


class ProjectUpdate_stage8(AccessMixin, UpdateFieldStage8Mixin, FormValidMixin, UpdateView):
  model = Project_procedure
  success_url = reverse_lazy("crm:ProjectList-stage8")
  template_name = "crm/project_update_stage_8.html"


class ProjectUpdate_stage9(AccessMixin, UpdateFieldStage9Mixin, FormValidMixin, UpdateView):
  model = Project_procedure
  success_url = reverse_lazy("crm:ProjectList-stage9")
  template_name = "crm/project_update_stage_9.html"