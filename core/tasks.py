import requests
from celery import shared_task
from django.core.cache import cache
from django.shortcuts import get_object_or_404

from core.models import Visit


@shared_task
def get_country_from_ip(visit_pk):
    visit = get_object_or_404(Visit, pk=visit_pk)
    print(f"getting country from api | {visit.ip=}")
    try:
        r = requests.get(f"https://ipinfo.io/{visit.ip}/json")
        r.raise_for_status()
        data = r.json()
        country = data.get("country", "Unknown")
        cache.set(visit.ip, country)
    except requests.RequestException:
        country = "Unknown"
    visit.country = country
    visit.save()
