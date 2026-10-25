**Example 1: 示例**



Input: 

```
tccli rum ModifyTDEMFunnel --cli-unfold-argument  \
    --AppId 1****7 \
    --FunnelId 0ebd8927-7db4-46ca-a0b2-4befe75e08c8 \
    --FunnelName 进入购物车页面 \
    --Steps.0.StepName 进入首页 \
    --Steps.0.PagePattern 商城首页 \
    --Steps.0.PageMatchMode exact \
    --Description enter page \
    --Status active \
    --Source manual
```

Output: 
```
{
    "Response": {
        "Result": "{\"FunnelId\":\"0ebd8927-7db4-46ca-a0b2-4befe75e08c8\"}",
        "RequestId": "1dff6c0c-1962-4c14-9a44-5881b70b6e89"
    }
}
```

