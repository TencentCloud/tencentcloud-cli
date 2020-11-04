**Example 1: CreateApi**



Input: 

```
tccli apigateway CreateApi --cli-unfold-argument  \
    --ServiceId service-ody35h5e\
    --ApiName name\
    --ApiDesc desc\
    --ApiType NORMAL\
    --AuthType NONE\
    --ServiceType MOCK\
    --ServiceTimeout 15\
    --Protocol HTTP\
    --RequestConfig.Path /test\
    --RequestConfig.Method GET\
    --EnableCORS false\
    --ApiBusinessType NORMAL\
    --ServiceMockReturnMessage mock
```

Output: 
```
{
    "Response": {
        "Result": {
            "ApiId": "api-61jyuvg6",
            "Path": "test",
            "Method": "GET",
            "CreatedTime": "2020-03-23T08:59:18Z"
        },
        "RequestId": "96026454-d916-4035-ba88-0e900214d0f6"
    }
}
```

