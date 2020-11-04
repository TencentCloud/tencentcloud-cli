**Example 1: ModifyApi**



Input: 

```
tccli apigateway ModifyApi --cli-unfold-argument  \
    --ServiceId service-ody35h5e\
    --ApiId api-lqd35zzq\
    --ApiName xxx\
    --RequestConfig.Path /xxxx\
    --RequestConfig.Method get\
    --ServiceType MOCK\
    --ServiceMockReturnMessage test
```

Output: 
```
{
    "Response": {
        "RequestId": "6e00553a-8158-4f70-ad43-e1b046af1502"
    }
}
```

