**Example 1: 查询设备标识及风险**



Input: 

```
tccli tds DescribeFraudPremium --cli-unfold-argument  \
    --DeviceToken v3:AAAAAZ0PYUPDnfxhxxxxxxxxx
```

Output: 
```
{
    "Response": {
        "AppVersion": "1.0",
        "Brand": "google",
        "ClientIp": "183.60.88.16",
        "ExtraInfos": [
            {
                "Key": "DegradationType",
                "Value": "1"
            }
        ],
        "HistRiskInfos": [],
        "Model": "Pixel 8 Pro",
        "NetworkType": "0",
        "Openid": "07F6312A3C9A060045930BF9",
        "PackageName": "com.turingfd",
        "Platform": "2",
        "RequestId": "00d67bd2-9e80-4045-8634-f10fa144735d",
        "RiskCheckTimestamp": "1774320814544",
        "RiskInfos": [
            {
                "Level": 2,
                "Type": 401
            },
            {
                "Level": 1,
                "Type": 402
            },
            {
                "Level": 3,
                "Type": 211
            },
            {
                "Level": 1,
                "Type": 213
            },
            {
                "Level": 3,
                "Type": 217
            },
            {
                "Level": 1,
                "Type": 1001
            },
            {
                "Level": 3,
                "Type": 201
            }
        ],
        "SdkBuildNo": "209303",
        "SystemVersion": "16"
    }
}
```

