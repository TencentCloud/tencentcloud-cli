**Example 1: 请求示例**



Input: 

```
tccli mps DescribeStreamLinkEvent --cli-unfold-argument  \
    --EventId eventid
```

Output: 
```
{
    "Response": {
        "Info": {
            "EventId": "xx",
            "Status": 1,
            "Description": "xx",
            "EventName": "xx",
            "AttachedFlowGroup": [
                {
                    "FlowId": "xx",
                    "Region": "xx"
                }
            ],
            "CreateTime": "xx"
        },
        "RequestId": "xx"
    }
}
```

