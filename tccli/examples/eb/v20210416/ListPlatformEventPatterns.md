**Example 1: 查询平台产品事件匹配规则**



Input: 

```
tccli eb ListPlatformEventPatterns --cli-unfold-argument  \
    --ProductType eb_platform_test
```

Output: 
```
{
    "Response": {
        "RequestId": "584caa6b-26d8-4ba5-858d-df1182730075",
        "EventPatterns": [
            {
                "EventName": "TEST",
                "EventPattern": "{\n\t\t\t\t\t\"source\":\"platform.cloud.tencent\",\n\t\t\t\t\t\"type\":\"eb_platform_test:TEST:ALL\"\n\t\t\t\t  }"
            }
        ]
    }
}
```

