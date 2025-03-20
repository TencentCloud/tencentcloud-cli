**Example 1: 查询分组下设备**



Input: 

```
tccli iotvideoindustry DescribeGroupDevices --cli-unfold-argument  \
    --GroupId group-xxx
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
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "TotalCount": 1
    }
}
```

