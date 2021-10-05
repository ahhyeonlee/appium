import requests

def setting(device_name): 
    devices = requests.get("http://localhost:8080/get/device/" + device_name).json()
    device = devices[0]
    desired_caps = {
        'platformName': device['device_os'],
        'platformVersion': device['platform_version'],
        'deviceName': device_name,
        'app': 'D:/appium/' + device['app_file_name'],
        'autoGrantPermissions': 'true',
        "appPackage": "com.olleh.android.oc2",
        'automationName': 'Appium',
        'ignoreHiddenApiPolicyError': 'true',
        'appActivity': device['app_activity'] 
    }
    return desired_caps
