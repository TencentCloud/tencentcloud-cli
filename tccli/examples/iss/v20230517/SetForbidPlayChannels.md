**Example 1: 通道禁播使能**



Input: 

```
tccli iss SetForbidPlayChannels --cli-unfold-argument  \
    --UserId 10********02 \
    --Channels.0.ChannelId 0001a415-****-****-****-b13cfb96c778 \
    --Channels.0.Enable True \
    --Channels.1.ChannelId 00037e5f-****-****-****-f30b13a86b02 \
    --Channels.1.Enable False
```

Output: 
```
{
    "Response": {
        "RequestId": "fba7981b-d6a4-4177-b11d-e53a6110e4cd"
    }
}
```

