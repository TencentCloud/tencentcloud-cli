**Example 1: 获取设备下属通道列表**



Input: 

```
tccli iotvideoindustry DescribeChannels --cli-unfold-argument  \
    --DeviceId 99576636581180000329_99576636581180000329
```

Output: 
```
{
    "Response": {
        "Channels": [
            {
                "ChannelName": "小枪机",
                "ChannelId": "99576636581180000329_34020000001320000094",
                "ChannelType": 1,
                "ChannelCode": "34020000001320000094",
                "ExtraInformation": "{\"Manufacturer\":\"Manufacturer\",\"Model\":\"Camera\"}",
                "Status": 3,
                "IsRecord": 1,
                "DeviceId": "99576636581180000329_99576636581180000329",
                "BusinessGroupId": "99576636581180000329_99576636581180000329"
            }
        ],
        "RequestId": "2d38b437-935b-4593-8e69-36e0945767e0",
        "TotalCount": 1
    }
}
```

