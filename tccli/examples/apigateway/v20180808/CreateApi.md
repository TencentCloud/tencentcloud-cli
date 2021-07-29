**Example 1: CreateApi**



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
        "Result": {},
        "RequestId": "d617a773-cfbd-47a7-8762-b213dcb681f0"
    }
}
```

