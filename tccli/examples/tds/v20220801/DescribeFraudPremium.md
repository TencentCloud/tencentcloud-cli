**Example 1: 查询设备标识**



Input: 

```
tccli tds DescribeFraudPremium --cli-unfold-argument  \
    --DeviceToken xx
```

Output: 
```
{
    "Response": {
        "Brand": "xx",
        "SdkBuildNo": "xx",
        "AppVersion": "xx",
        "Platform": "xx",
        "SystemVersion": "xx",
        "RequestId": "xx",
        "NetworkType": "xx",
        "Model": "xx",
        "PackageName": "xx",
        "ClientIp": "xx",
        "RiskInfos": [
            {
                "Type": 201,
                "Level": 1
            }
        ],
        "HistRiskInfos": [
            {
                "Type": 201,
                "Level": 1
            }
        ],
        "Openid": "xx"
    }
}
```

