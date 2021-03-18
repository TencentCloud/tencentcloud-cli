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
                "DeviceCode": "99350367561320000005"
            },
            {
                "NickName": "nameCN22",
                "DeviceId": "99350367561320000004_99350367561320000004",
                "Status": 3,
                "ExtraInformation": "{\"DeviceModel\":\"xxx\",\"Manufacturer\":\"xxx\"}",
                "DeviceType": 2,
                "DeviceCode": "99350367561320000004"
            }
        ],
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "TotalCount": 2
    }
}
```

