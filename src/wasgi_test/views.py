from asyncio import sleep as async_sleep
from time import sleep
from django.http import HttpResponse


def sync_hello_world(request):
    return HttpResponse("hi wrld sync")


def sync_hello_world_slow(request):
    sleep(5)
    return HttpResponse("hi wrld sync slow")


async def async_hello_world_slow(request):
    await async_sleep(5)  # in sec
    return HttpResponse("hi wrld async slow")
