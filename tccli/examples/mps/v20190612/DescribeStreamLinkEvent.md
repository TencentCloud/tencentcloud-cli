**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkEvent --cli-unfold-argument  \
    --EventId 019377034b0709dc0f3269ca3422
```

Output: 
```
{
    "Response": {
        "Info": {
            "EventId": "019377034b0709dc0f3269ca3422",
            "Status": 1,
            "Description": "live",
            "EventName": "live",
            "AttachedFlowGroup": [
                {
                    "FlowId": "6658vndj5mg0fsrjzzdfnr",
                    "Region": "ap-hongkong"
                }
            ],
            "CreateTime": "2026-08-01T10:00:00+08:00"
        },
        "RequestId": "3c140219-cfe9-4a60-af06-3ee6e0a1e5f1"
    }
}
```

