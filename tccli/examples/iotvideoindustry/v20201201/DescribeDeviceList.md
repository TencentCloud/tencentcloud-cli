**Example 1: 获取设备列表**



Input: 

```
tccli iotvideoindustry DescribeDeviceList --cli-unfold-argument  \
    --Limit 10 \
    --NickName btest \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Devices": [
            {
                "NickName": "keting",
                "DeviceId": "99576636581320000270_99576636581320000270",
                "DeviceType": 2,
                "Status": 3,
                "ExtraInformation": "",
                "DeviceCode": "99576636581320000270",
                "Protocol": "GB28181",
                "GroupId": "group_root",
                "GroupName": "全部",
                "GroupPath": "",
                "Recordable": 1,
                "IsRecord": 0,
                "CreateTime": 345233456
            }
        ],
        "RequestId": "5aa3fe4f-72c3-4c77-a48d-a418addff8c9",
        "TotalCount": 1
    }
}
```

