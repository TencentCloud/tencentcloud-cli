**Example 1: 获取license**



Input: 

```
tccli ioa DescribeLicense --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "AuthNum": {
                "Platforms": [],
                "Total": 100
            },
            "Bandwidth": {
                "BandwidthMode": 1,
                "InquireNum": 2
            },
            "LicenseInfo": {
                "BeginTime": 1700466824,
                "CompanyId": "1300055726",
                "CompanyName": "nil",
                "EndTime": 1732089224,
                "LicenseKey": "",
                "LicenseVer": "",
                "ProductDesc": "高级版",
                "ProductName": "version_premium",
                "SourceType": 1,
                "Status": 1
            },
            "LogStorage": {
                "InquireNum": 5
            },
            "Module": {
                "Platforms": [
                    {
                        "Platform": 0,
                        "PlatformModules": [
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_BASE"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_SECURITY"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_CONTROL"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_NGN"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_SECURITY_REINFORCEMENT"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_WATERMASK"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_MDC_REMOTE_CONTROL"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_DLP"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_EDR"
                            }
                        ]
                    },
                    {
                        "Platform": 1,
                        "PlatformModules": []
                    },
                    {
                        "Platform": 2,
                        "PlatformModules": [
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_BASE"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_SECURITY"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_CONTROL"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_NGN"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_WATERMASK"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_DLP"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_EDR"
                            }
                        ]
                    },
                    {
                        "Platform": 4,
                        "PlatformModules": [
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_BASE"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_CONTROL"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_NGN"
                            }
                        ]
                    },
                    {
                        "Platform": 5,
                        "PlatformModules": [
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_BASE"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_CONTROL"
                            },
                            {
                                "Description": "nil",
                                "ModuleName": "MODULE_NGN"
                            }
                        ]
                    }
                ]
            },
            "NGNAuthInfo": {
                "NGNConcurrence": 50
            },
            "Platforms": [
                0,
                2,
                4,
                5
            ]
        },
        "RequestId": "6b441f71-dc14-4c45-9540-e50c3b929a1b"
    }
}
```

