import requests

def setting(device_id): 
    devices = requests.get("http://211.250.72.85:8080/get/device/" + device_id).json()
    device = devices[0]
    print(device)
    desired_caps = {
        'platformName': device['device_os'],
        'platformVersion': device['platform_version'],
        'deviceName': device['device_name'],
        'app': 'D:/appium/' + device['app_file_name'],
        'autoGrantPermissions': 'true',
        "appPackage": "com.olleh.android.oc2",
        'automationName': 'Appium',
        'ignoreHiddenApiPolicyError': 'true',
        'appActivity': device['app_activity'] 
    }
    desired_caps['app_name'] = device['app_name']
    return desired_caps
