**Example 1: 修改任务**



Input: 

```
tccli workbuddyenterprise ModifyScheduledTask --cli-unfold-argument  \
    --TaskId 1001 \
    --TaskName 每日晨报v2 \
    --DeliveryTargetSet.0.Type BOT_CHANNEL \
    --DeliveryTargetSet.0.Enabled True \
    --DeliveryTargetSet.0.Options.ChannelType QQ \
    --DeliveryTargetSet.0.Options.ChannelId 1905263717 \
    --DeliveryTargetSet.0.Options.RecipientIdSet oc_xxx oc_yyy
```

Output: 
```
{
    "Response": {
        "RequestId": "3c6d138e-1234-5678-9abc-def012345678"
    }
}
```

