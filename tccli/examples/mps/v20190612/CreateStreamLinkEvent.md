**Example 1: 请求示例**



Input: 

```
tccli mps CreateStreamLinkEvent --cli-unfold-argument  \
    --EventName event_test
```

Output: 
```
{
    "Response": {
        "Info": {
            "EventId": "019202e96d9f09dc0f325e7f7a2a",
            "Status": 1,
            "Description": "event for test live",
            "EventName": "event_test",
            "AttachedFlowGroup": [
                {
                    "FlowId": "01937702c54509dc0f3269ca341f",
                    "Region": "ap-shanghai"
                }
            ],
            "CreateTime": "2024-10-12 12:12:12"
        },
        "RequestId": "019202e96d9f09dc0f325e7f7a2a"
    }
}
```

