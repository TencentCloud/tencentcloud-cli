**Example 1: 查询app状态**



Input: 

```
tccli wedata GetAppStatus --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --AppKey 0820bce11774327509629d10b4c1e
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": "DEPLOY_FAILED"
        },
        "RequestId": "88ee7adc-7a0b-4b47-8e6f-c9a817609e74"
    }
}
```

