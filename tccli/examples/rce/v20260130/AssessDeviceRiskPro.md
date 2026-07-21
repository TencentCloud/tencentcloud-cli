**Example 1: 设备风险评估基础版示例**



Input: 

```
tccli rce AssessDeviceRiskPro --cli-unfold-argument  \
    --DeviceToken v3:**************************************************u58Tcp7u042WRcZBER/N/w== \
    --UserIp 183.*******.16
```

Output: 
```
{
    "Response": {
        "Data": {
            "Device": {
                "AppVersion": "1.0",
                "Brand": "****",
                "ClientIp": "183.*******.16",
                "DeviceId": "350C54************54E940",
                "Model": "PCK****",
                "NetworkType": "0",
                "PackageName": "com.******",
                "Platform": "2",
                "SdkBuildVersion": "90",
                "SystemVersion": "11"
            },
            "Score": {
                "RiskLabels": [
                    {
                        "Id": "101208",
                        "Reason": "Debugging Mode Enabled (Android)"
                    }
                ],
                "RiskLevel": 3
            }
        },
        "RequestId": "e86e9de7-435c-4a0a-847b-237867dacb8d"
    }
}
```

