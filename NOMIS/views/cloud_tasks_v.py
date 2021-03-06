"""Module with the views for queues in nomis application
"""

from django.http import HttpResponse, JsonResponse

from nomis.services.cloud_tasks import pause_queues, resume_queues
from nomis.models.report import Report
from nomis.models.tax_engine import Taxengine
from nomis.models.step import Step


def pause(request, tax_id):
    """Method to pause queues in google cloud tasks
    """
    paus = pause_queues()
    # taxengine_id = Taxengine(id=tax_id)
    step = Step.objects.get(code_name="PAUSE_QUEUES")

    if paus == 'PAUSED':
        report = "paused"
        kind = "SUCCES"
        reports = Report(taxengine_id=tax_id,
                    step_id=step.id, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=200)
    else:
        report = "error pausing"
        kind = "ERROR"
        reports = Report(taxengine_id=tax_id,
                    step_id=step.id, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=500)


def resume(request, id):
    """Method to resume queues in google cloud tasks
    """
    resum = resume_queues()
    taxengine_id = Taxengine(id=id)
    step = Step(id="11d108f70f4a4740b80b7179e7b3c426")

    if resum == 'RUNNING':
        report = "running"
        kind = "SUCCES"
        reports = Report(taxengine_id =taxengine_id,
                    step_id =step, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=200)
    else:
        report = "error running"
        kind = "ERROR"
        reports = Report(taxengine_id =taxengine_id,
                    step_id =step, message=report, kind=kind)
        reports.save()
        return HttpResponse(status=500)
