from re import sub
from board.models import Scenario, Case, Device
from board.serializers import ScenarioSerializer, CaseSerializer, DeviceSerializer
from django.shortcuts import redirect
from rest_framework.decorators import api_view #api
from rest_framework.response import Response #api
import os, subprocess 

#시나리오 
@api_view(['GET'])
def getScenario(request, app_name):
    scenario = Scenario.objects.filter(app_name = app_name, use_yn = "y")
    serialized_scenario = ScenarioSerializer(scenario, many = True)
    return  Response(serialized_scenario.data)

#케이스
@api_view(['GET'])
def getCase(request, scenario_id): 
    case = Case.objects.filter(scenario_id = scenario_id)
    serialized_case = CaseSerializer(case, many = True)
    return Response(serialized_case.data)

#디바이스
@api_view(['GET'])
def getDevice(request, device_id):
    device = Device.objects.filter(id = device_id)
    serialized_device = DeviceSerializer(device, many = True)
    return Response(serialized_device.data)


@api_view(['GET'])
def runDevice(request, device_id):
    device = Device.objects.filter(id = device_id)

    #subprocess.call("adb shell input keyevent KEYCODE_APP_SWITCH", shell=True)
    #subprocess.call("adb shell input touchscreen swipe 200 2200 200 2500", shell=True)
    cmd = 'python runs.py ' + device_id
    subprocess.call(cmd, cwd='D:/appium/appiumProject/appium/')
    
    serialized_device = DeviceSerializer(device, many = True)
    return Response(serialized_device.data)