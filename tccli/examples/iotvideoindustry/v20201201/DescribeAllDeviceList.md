**Example 1: 获取所有设备列表**



Input: 

```
tccli iotvideoindustry DescribeAllDeviceList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Devices": [
            {
                "DeviceId": "xxxxxx",
                "Status": 3,
                "CreateTime": 1607073128,
                "ExtraInformation": "{\"DeviceModel\":\"xxx\",\"Manufacturer\":\"xxx\"}",
                "NickName": "myDevice01",
                "GroupPath": ""
            }
        ],
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "TotalCount": 1
    }
}
```

