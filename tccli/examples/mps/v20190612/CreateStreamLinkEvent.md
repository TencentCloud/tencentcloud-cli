**Example 1: 请求示例**



Input: 

```
tccli mps CreateStreamLinkEvent --cli-unfold-argument  \
    --EventName aaa
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

