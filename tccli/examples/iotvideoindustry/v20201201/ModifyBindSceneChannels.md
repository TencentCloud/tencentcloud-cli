**Example 1: 场景绑定/解绑通道接口**



Input: 

```
tccli iotvideoindustry ModifyBindSceneChannels --cli-unfold-argument  \
    --SceneId 11 \
    --Type 1 \
    --Channels.0.DeviceId aaaaa \
    --Channels.0.ChannelId bbbbb
```

Output: 
```
{
    "Response": {
        "RequestId": "1d7a62c9-db36-4a5f-9209-2e420883e28f"
    }
}
```

