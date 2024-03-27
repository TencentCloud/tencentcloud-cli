**Example 1: 删除云存某一事件**



Input: 

```
tccli iotexplorer DeleteCloudStorageEvent --cli-unfold-argument  \
    --ProductId abc \
    --DeviceName abc \
    --EventId abc \
    --StartTime 1 \
    --EndTime 1 \
    --UserId abc \
    --ChannelId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

