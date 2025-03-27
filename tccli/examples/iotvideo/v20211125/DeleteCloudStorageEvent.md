**Example 1: 删除云存某一事件**



Input: 

```
tccli iotvideo DeleteCloudStorageEvent --cli-unfold-argument  \
    --ProductId product \
    --DeviceName dev \
    --EventId event \
    --StartTime 1 \
    --EndTime 1 \
    --UserId user \
    --ChannelId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "id"
    }
}
```

