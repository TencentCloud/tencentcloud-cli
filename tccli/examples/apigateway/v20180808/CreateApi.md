**Example 1: CreateApi**

CreateApi

Input: 

```
tccli apigateway CreateApi --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --ApiName name \
    --ApiDesc desc \
    --ApiType NORMAL \
    --AuthType NONE \
    --ServiceType MOCK \
    --ServiceTimeout 15 \
    --Protocol HTTP \
    --RequestConfig.Path /test \
    --RequestConfig.Method GET \
    --EnableCORS false \
    --ApiBusinessType NORMAL \
    --ServiceMockReturnMessage mock
```

Output: 
```
{
    "Response": {
        "Result": {
            "ApiId": "abc",
            "Path": "abc",
            "Method": "abc",
            "CreatedTime": "2020-09-22T00:00:00+00:00"
        },
        "RequestId": "abc"
    }
}
```

