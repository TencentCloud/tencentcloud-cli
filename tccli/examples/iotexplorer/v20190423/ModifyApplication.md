**Example 1: 更新应用**

更新应用信息

Input: 

```
tccli iotexplorer ModifyApplication --cli-unfold-argument  \
    --IotAppID VJbAVRtnqQmX \
    --AppName IoT_App \
    --Description desc
```

Output: 
```
{
    "Response": {
        "Application": {
            "IotAppID": "VJbAVRtnqQmX",
            "AppName": "IoT_App",
            "ProjectId": "prj-bm28br23",
            "DevMode": 0,
            "IOSAppKey": "iwBkGVJbAVRtnqQmX",
            "IOSAppSecret": "tnehmHUfzUImcMvZgmko",
            "AndroidAppKey": "apBhdVJbAVRtnqQmX",
            "AndroidAppSecret": "JluDpMxWSTpqqEpTSMBz",
            "MiniProgramAppKey": "",
            "MiniProgramAppSecret": "",
            "Products": "[P12f5tG]",
            "Description": "产品描述信息.",
            "PushSecretID": "",
            "PushSecretKey": "",
            "PushEnvironment": "dev",
            "TPNSiOSAccessID": "",
            "TPNSiOSSecretKey": "",
            "TPNSiOSRegion": "",
            "TPNSiOSPushEnvironment": "",
            "TPNSAndroidAccessID": "",
            "TPNSAndroidSecretKey": "",
            "TPNSAndroidRegion": "",
            "SelfSmsTemplateId": 0,
            "SelfSmsAppKey": "sms",
            "SelfSmsAppId": "appid",
            "SelfSmsSign": "sign",
            "CreateTime": "2019-03-18T03:44:33Z"
        },
        "RequestId": "f92406b3-5a9a-4fe8-bc43-45e3d794bb61"
    }
}
```

