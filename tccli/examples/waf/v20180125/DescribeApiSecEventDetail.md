**Example 1: 查询API安全事件详情**



Input: 

```
tccli waf DescribeApiSecEventDetail --cli-unfold-argument  \
    --Domain *************.testwaf.com \
    --EventId api_k********c
```

Output: 
```
{
    "Response": {
        "AttackSource": [
            {
                "AttackCount": 22,
                "AttackDetail": null,
                "BotLabel": "",
                "City": "",
                "EventCount": 12,
                "EventLevel": "300",
                "MissPassword": "",
                "MissUserName": "",
                "SrcIp": "9.******.21",
                "StartTime": 1777110120,
                "Timestamp": 1777110180
            }
        ],
        "ChangeHistory": [
            {
                "Mode": "2",
                "Remark": "",
                "Timestamp": 1777110298,
                "UserName": "wa********1**6****m"
            }
        ],
        "Description": "",
        "EventInfo": {
            "ApiName": "/anything/sens",
            "Domain": "*************.testwaf.com",
            "EventId": "api_k********c",
            "EventType": "响应敏感数据信息量(去重次数)",
            "Level": "300",
            "Method": "POST",
            "Mode": "2",
            "Source": "custom",
            "StartTime": 1777110217,
            "UpdateTime": 1777110298
        },
        "RequestId": "b402400d-ec6c-4892-af44-7acb06a8df91"
    }
}
```

