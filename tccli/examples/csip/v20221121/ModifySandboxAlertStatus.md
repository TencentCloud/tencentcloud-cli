**Example 1: 批量更新告警状态示例**



Input: 

```
tccli csip ModifySandboxAlertStatus --cli-unfold-argument  \
    --AlertType ACL \
    --BelongAssetType HOST \
    --IDList 7001 7002 \
    --Status HANDLED
```

Output: 
```
{
    "Response": {
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

