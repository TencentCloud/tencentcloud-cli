**Example 1: DescribeSystemConfig**



Input: 

```
tccli ioa DescribeSystemConfig --cli-unfold-argument  \
    --Condition.PageNum 1 \
    --Condition.PageSize 10
```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "PageNum": 1,
                "PageSize": 10,
                "Total": 197,
                "PageCount": 20
            },
            "Items": [
                {
                    "ConfigValue": "0",
                    "Id": 442,
                    "ConfigName": "AutoServerAddr"
                },
                {
                    "ConfigValue": "saas",
                    "Id": 786,
                    "ConfigName": "ServerPlatform"
                },
                {
                    "ConfigValue": "1",
                    "Id": 395,
                    "ConfigName": "QMNgnPluginSwitch"
                },
                {
                    "ConfigValue": "{\"Enable\":1,\"TimeType\":1,\"Day\":1,\"Hour\":0,\"Minute\":0,\"HourEnd\":24,\"MinuteEnd\":0}",
                    "Id": 397,
                    "ConfigName": "SvrVirusUpdate"
                },
                {
                    "ConfigValue": "{\"Enable\":1,\"TimeType\":1,\"Day\":1,\"Hour\":0,\"Minute\":0,\"HourEnd\":24,\"MinuteEnd\":0}",
                    "Id": 398,
                    "ConfigName": "SvrPatchUpdate"
                },
                {
                    "ConfigValue": "{\"Type\":\"0\",\"Ip\":\"\",\"Port\":\"\",\"User\":\"\",\"Pass\":\"\"}",
                    "Id": 399,
                    "ConfigName": "SvrProxy"
                },
                {
                    "ConfigValue": "{\"Enable\":0,\"ByDay\":\"0\",\"Day\":\"\",\"Size\":\"\",\"Hour\":\"0\"}",
                    "Id": 401,
                    "ConfigName": "SysLog"
                },
                {
                    "ConfigValue": "{\"Type\":0,\"Ip\":\"127.0.0.1\",\"Port\":8111,\"User\":\"\",\"Pwd\":\"\"}",
                    "Id": 400,
                    "ConfigName": "ParentProxyConfig"
                },
                {
                    "ConfigValue": "/store/vul/",
                    "Id": 402,
                    "ConfigName": "VulConfigUrl"
                },
                {
                    "ConfigValue": "{\"Enable\":0,\"TimeType\":1,\"Day\":1,\"Hour\":0,\"Minute\":0,\"HourEnd\":24,\"MinuteEnd\":0}",
                    "Id": 396,
                    "ConfigName": "ClientPackUpdate"
                }
            ]
        },
        "RequestId": "123c48b5-0bfe-4d51-b26a-1918aca14c2d"
    }
}
```

