**Example 1: 事件详情接口访问示例**

访问所有云产品事件的详情内容

Input: 

```
tccli eb GetEventDetails --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "EventsDetectors": [
            {
                "Id": 0,
                "ProductNameCh": "abc",
                "ProductNameEn": "abc",
                "EventTypeCh": "abc",
                "EventTypeEn": "abc",
                "HasRecovery": 0,
                "EventDescription": "abc",
                "Suggestions": "abc",
                "EventSource": "abc",
                "EventType": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

