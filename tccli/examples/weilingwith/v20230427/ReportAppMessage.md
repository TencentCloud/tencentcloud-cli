**Example 1: 单个上报消息**

成功响应

Input: 

```
tccli weilingwith ReportAppMessage --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --Profile.AppType security_monitoring \
    --ReportTs 1 \
    --Properties x-json:{"executeId": "RX_TASK"} \
    --ApplicationToken baSTzPx0vZ6LPuv2EifNa5CqRBj9hoY0
```

Output: 
```
{
    "Response": {
        "RequestId": "d542c6ba-6e4b-4d29-be9a-4e48c1c8616d",
        "Result": {
            "Msg": "ok"
        }
    }
}
```

