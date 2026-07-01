**Example 1: ModifyEdrAlertPermanentIgnore**

永久忽略EDR多行为告警

Input: 

```
tccli csip ModifyEdrAlertPermanentIgnore --cli-unfold-argument  \
    --Targets.0.Id 10001 \
    --Targets.0.AlertId alert-abc-123 \
    --Targets.0.AppId 1234567890 \
    --Targets.0.InstanceId ins-xxx \
    --MemberId mem-68************00
```

Output: 
```
{
    "Response": {
        "IgnoredCount": 1,
        "RequestId": "8c1f7156-fc01-4905-b286-e08f4db0eec2"
    }
}
```

