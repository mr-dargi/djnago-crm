from django.urls import path, include
from .views import (
                      ProjectList,
                      ProjectList_stage1,
                      ProjectList_stage2,
                      ProjectList_stage3,
                      ProjectList_stage4,
                      ProjectList_stage5,
                      ProjectCreate,
                      ProjectUpdate_stage1,
                      ProjectUpdate_stage2,
                      ProjectUpdate_stage3,
                      ProjectUpdate_stage4,
                      ProjectUpdate_stage5
                    )

app_name = "crm"
urlpatterns = [
  path("", ProjectList.as_view(), name="home"),
  path("project/list/stage1", ProjectList_stage1.as_view(), name="ProjectList-stage1"),
  path("project/list/stage2", ProjectList_stage2.as_view(), name="ProjectList-stage2"),
  path("project/list/stage3", ProjectList_stage3.as_view(), name="ProjectList-stage3"),
  path("project/list/stage4", ProjectList_stage4.as_view(), name="ProjectList-stage4"),
  path("project/list/stage5", ProjectList_stage5.as_view(), name="ProjectList-stage5"),
  path("project/create", ProjectCreate.as_view(), name="projectCreate"),
  path("project/stage1/<int:pk>", ProjectUpdate_stage1.as_view(), name="projectCreate-stage1"),
  path("project/stage2/<int:pk>", ProjectUpdate_stage2.as_view(), name="projectCreate-stage2"),
  path("project/stage3/<int:pk>", ProjectUpdate_stage3.as_view(), name="projectCreate-stage3"),
  path("project/stage4/<int:pk>", ProjectUpdate_stage4.as_view(), name="projectCreate-stage4"),
  path("project/stage5/<int:pk>", ProjectUpdate_stage5.as_view(), name="projectCreate-stage5"),
]
