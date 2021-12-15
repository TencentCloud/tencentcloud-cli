**Example 1: 获取场景绑定设备列表**



Input: 

```
tccli iotvideoindustry DescribeBindSceneDevices --cli-unfold-argument  \
    --SceneId 5 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "DeviceId": "99576636581320000327_99576636581320000327",
                "ChannelId": "99576636581320000327_99576636581320000327"
            },
            {
                "DeviceId": "99576636581320000328_99576636581320000328",
                "ChannelId": "99576636581320000328_99576636581320000328"
            }
        ],
        "RequestId": "1d7a62c9-db36-4a5f-9209-2e420883e28f",
        "Total": 2
    }
}
```

