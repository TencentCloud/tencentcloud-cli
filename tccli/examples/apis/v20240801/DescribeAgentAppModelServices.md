**Example 1: 查询应用关联的模型服务**



Input: 

```
tccli apis DescribeAgentAppModelServices --cli-unfold-argument  \
    --Limit 10 \
    --InstanceID ins-a7af1980 \
    --AgentAppIDs aga-41d42939
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
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
                    "ModelServiceVO": {
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
                        "LastUpdateTime": "2026-02-04T06:37:38.601Z",
                        "ModelNames": [
                            "deepseek-r1"
                        ],
                        "Name": "deepseek",
                        "PathMatchType": "prefix",
                        "PluginConfigs": [],
                        "PubPath": "/v1",
                        "RelateAgentAppNum": 0,
                        "Status": "disabled",
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
                    "RelateTime": "2026-02-04T07:17:10.116Z",
                    "TokenLimitConfig": {
                        "LimitRequestBody": 0,
                        "LimitWindows": []
                    },
                    "TokenLimitStatus": false
                }
            ],
            "Total": 1
        },
        "RequestId": "44bd5c9a-9da8-401e-a462-d0e6b44c5271"
    }
}
```

