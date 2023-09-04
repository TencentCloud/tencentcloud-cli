**Example 1: 变更告警状态**

成功响应

Input: 

```
tccli weilingwith ChangeAlarmStatus --cli-unfold-argument  \
    --Id 40b52dda-c596-4510-84c4-a5e1aa6ae359 \
    --Status processed \
    --ProcessTime 1693416387 \
    --ProcessType kill_warning \
    --WorkspaceId 1016 \
    --UserId 1 \
    --UserName a \
    --ApplicationToken YVySZSL1Lp5UtSJ5uJVLJYOKDEGfCCH2
```

Output: 
```
{
    "Response": {
        "RequestId": "9544b470-8b37-4aeb-b7ea-d6cb0175ada1",
        "Result": {
            "Msg": "ok"
        }
    }
}
```

