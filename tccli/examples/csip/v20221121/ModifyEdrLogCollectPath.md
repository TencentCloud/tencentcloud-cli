**Example 1: 示例**



Input: 

```
tccli csip ModifyEdrLogCollectPath --cli-unfold-argument  \
    --Paths.0.Id 0 \
    --Paths.0.Path /var/log/cron* \
    --Paths.0.LogTag user_tag_cron
```

Output: 
```
{
    "Response": {
        "RequestId": "bf007005-e54e-42a8-918f-7ea72c8e8308"
    }
}
```

