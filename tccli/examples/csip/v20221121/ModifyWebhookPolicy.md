**Example 1: 示例**



Input: 

```
tccli csip ModifyWebhookPolicy --cli-unfold-argument  \
    --Name policy1 \
    --Status ON \
    --NotifyItems.0.Module Alert \
    --NotifyItems.0.SubModule MALWARE_FILE \
    --NotifyItems.0.Levels HIGH \
    --AssetScope.AssetRange 1 \
    --ReceiveFormat TEXT \
    --ReceiverIDList 19 \
    --MemberId mem-xxx \
    --ID 5 \
    --MsgLanguage zh
```

Output: 
```
{
    "Response": {
        "ID": 5,
        "RequestId": "45347672-c912-4e38-a153-cb3cadf4eb53"
    }
}
```

