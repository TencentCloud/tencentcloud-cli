**Example 1: ModifyApi**

可调用此接口对已经配置的 API 接口进行编辑修改。修改后的 API 需要重新发布 API 所在的服务到对应环境方能生效

Input: 

```
tccli apigateway ModifyApi --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --ApiId api-lqd35zzq \
    --ApiName http_api \
    --RequestConfig.Path / \
    --RequestConfig.Method ANY \
    --ServiceType MOCK \
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

