**Example 1: 查询服务详情**



Input: 

```
tccli apis DescribeModelService --cli-unfold-argument  \
    --InstanceID ins-a7af1980 \
    --ID mds-ea8d96c6
```

Output: 
```
{
    "Response": {
        "Data": {
            "AppID": 1300273807,
            "CreateTime": "2026-02-03T11:22:25.627Z",
            "Description": "deepseek",
            "ID": "mds-ea8d96c6",
            "InstanceID": "ins-a7af1980",
            "InvokeLimitConfig": {
                "FunnelMaxNum": 0,
                "FunnelRate": 0,
                "SlidingWindowMaxNum": 0,
                "SlidingWindowSize": 0,
                "TimeWindow": 0,
                "TimeWindowInterval": 0,
                "TokenBucketMaxNum": 0,
                "TokenBucketRate": 0,
                "Type": ""
            },
            "InvokeLimitConfigStatus": false,
            "IpBlackList": [],
            "IpBlackStatus": false,
            "IpWhiteList": [],
            "IpWhiteStatus": false,
            "LastUpdateTime": "2026-02-03T11:23:42.212Z",
            "ModelNames": [
                "deepseek-r1"
            ],
            "Name": "deepseek-r101",
            "PathMatchType": "prefix",
            "PluginConfigs": [],
            "PubPath": "/v1",
            "RelateAgentAppNum": 0,
            "Status": "normal",
            "Timeout": 10,
            "TmsConfig": {
                "Action": "",
                "BizType": "",
                "InterceptMessage": "",
                "MergeCount": 0,
                "Mode": "",
                "Scope": null
            },
            "TmsStatus": false,
            "TokenLimitConfig": {
                "LimitRequestBody": 0,
                "LimitWindows": []
            },
            "TokenLimitStatus": false,
            "Uin": "700001136234"
        },
        "RequestId": "d404956c-e692-4909-89b9-a92c2066c7bd"
    }
}
```

