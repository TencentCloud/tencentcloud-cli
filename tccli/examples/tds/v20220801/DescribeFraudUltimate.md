**Example 1: 查询设备标识及风险（旗舰版）**



Input: 

```
tccli tds DescribeFraudUltimate --cli-unfold-argument  \
    --DeviceToken v2:s6kBRbiOKZp/kenOxxxxxxxxx \
    --SceneCode login \
    --UserId user1 \
    --EventTime 1666684836384 \
    --ElapsedTime 1 \
    --WeChatOpenId oEsXuszxxxxxxxxxxxxxxxx4qvEk \
    --PhoneNumber 15800000000 \
    --ClientIP 223.73.63.151 \
    --QQOpenId ECA1B7XXXXXXXXXXXXXXXXXXXX06625D
```

Output: 
```
{
    "Response": {
        "Brand": "HONOR",
        "SdkBuildNo": "75",
        "AppVersion": "1.0.0",
        "Platform": "2",
        "SystemVersion": "10",
        "RequestId": "19a13dc5-1c2c-4d0e-bd08-13534b53c8f4",
        "NetworkType": "0",
        "Model": "LLD-AL20",
        "PackageName": "a.b.c",
        "ClientIp": "223.73.63.151",
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
        "Openid": "A10254A0046CEA0448A387BF",
        "SceneRiskInfos": [
            {
                "Type": 100101,
                "Level": 1
            }
        ],
        "SuggestionLevel": 1,
        "Unionid": "BCC4AD40983ACF9CA18A55BC0A4401489833F362"
    }
}
```

