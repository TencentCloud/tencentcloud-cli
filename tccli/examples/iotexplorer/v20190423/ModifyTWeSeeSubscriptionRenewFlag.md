**Example 1: 设置不通知且手动续费**



Input: 

```
tccli iotexplorer ModifyTWeSeeSubscriptionRenewFlag --cli-unfold-argument  \
    --ProductId 4AHMY9X89Y \
    --DeviceName dev002 \
    --ServiceType VID_COMP \
    --RenewFlag DISABLE_NOTIFY_AND_MANUAL_RENEW \
    --ChannelId 0
```

Output: 
```
{
    "Response": {
        "RequestId": "95256487-cfff-4661-a7d7-b30887731dd2"
    }
}
```

