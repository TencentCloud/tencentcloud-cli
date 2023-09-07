**Example 1: 查询平台事件中文名称**



Input: 

```
tccli eb ListPlatformEventNames --cli-unfold-argument  \
    --ProductType eb_platform_test
```

Output: 
```
{
    "Response": {
        "RequestId": "584caa6b-26d8-4ba5-858d-df1182730075",
        "EventNames": [
            {
                "EventName": "TEST",
                "EventType": "eb_platform_test:TEST:ALL"
            }
        ]
    }
}
```

