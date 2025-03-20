**Example 1: 获取设备下属通道**



Input: 

```
tccli iotvideoindustry DescribeIPCChannels --cli-unfold-argument  \
    --DeviceId 99576636581320000278_99576636581320000278 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "DeviceList": [
            {
                "NickName": "test4",
                "DeviceId": "99350367561320000005_99350367561320000005",
                "Status": 3,
                "ExtraInformation": "{\"DeviceModel\":\"xxx\",\"Manufacturer\":\"xxx\"}",
                "DeviceType": 2,
                "IsRecord": 0,
                "DeviceCode": "99350367561320000005",
                "Recordable": 1,
                "Protocol": "GB28181",
                "CreateTime": 342324234,
                "ChannelNum": 1,
                "VideoChannelNum": 1,
                "RTSPUrl": ""
            }
        ],
        "RequestId": "20e4eb35-5429-4b25-8e4e-d7435518f194",
        "TotalCount": 1
    }
}
```

