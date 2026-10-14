**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkEvents --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "EventName": "live",
                "EventId": "0193770a00009dc0f3269ca3439",
                "CreateTime": "2026-08-01T10:00:00+08:00",
                "Description": "live_event",
                "Status": 1,
                "AttachedFlowGroup": [
                    {
                        "FlowId": "0123456789abcdef",
                        "Region": "ap-hongkong"
                    }
                ]
            }
        ],
        "PageNum": 0,
        "PageSize": 0,
        "TotalNum": 0,
        "TotalPage": 0,
        "RequestId": "3c140219-cfe9-4a60-af06-3ee6e0a1e5f1"
    }
}
```

