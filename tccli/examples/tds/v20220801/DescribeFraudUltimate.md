**Example 1: 查询设备标识**



Input: 

```
tccli tds DescribeFraudUltimate --cli-unfold-argument  \
    --DeviceToken xx \
    --SceneCode login \
    --UserId xx \
    --EventTime 1666684836384 \
    --ElapsedTime 1 \
    --WeChatOpenId xx \
    --PhoneNumber xx \
    --ClientIP xx \
    --QQOpenId xx
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
        "Openid": "xx",
        "SceneRiskInfos": [
            {
                "Type": 100101,
                "Level": 1
            }
        ],
        "SuggestionLevel": 1
    }
}
```

