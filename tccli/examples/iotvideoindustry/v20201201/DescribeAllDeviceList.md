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
                "DeviceId": "99870353841320000007_99870353841320000007",
                "DeviceType": 2,
                "Status": 3,
                "CreateTime": "1735791896",
                "ExtraInformation": "{\"DeviceModel\":\"9987035384132000000\",\"Manufacturer\":\"text\"}",
                "NickName": "myDevice01",
                "GroupPath": "/group-aaa/group-bbb",
                "DeviceCode": "99870353841320000007",
                "IsRecord": 0,
                "Recordable": 0,
                "Protocol": "GB/T 28181",
                "GroupId": "gro - zn3ro30w",
                "GroupName": "zn3ro30w"
            }
        ],
        "RequestId": "d3d6f466-f2c2-44df-b78b-383ba717a3d8",
        "TotalCount": 1
    }
}
```

