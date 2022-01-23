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
                "DeviceId": "99576636581320000270_99576636581320000270",
                "DeviceType": 2,
                "Status": 3,
                "ExtraInformation": "",
                "DeviceCode": "99576636581320000270",
                "Protocol": "GB28181",
                "GroupId": "group_root",
                "GroupName": "全部",
                "GroupPath": ""
            },
            {
                "DeviceId": "99576636581320000271_99576636581320000271",
                "DeviceType": 2,
                "Status": 3,
                "ExtraInformation": "",
                "DeviceCode": "99576636581320000271",
                "Protocol": "GB28181",
                "GroupId": "group_root",
                "GroupName": "全部",
                "GroupPath": ""
            },
            {
                "DeviceId": "99576636581320000272_99576636581320000272",
                "DeviceType": 2,
                "Status": 3,
                "ExtraInformation": "",
                "DeviceCode": "99576636581320000272",
                "Protocol": "GB28181",
                "GroupId": "group_root",
                "GroupName": "全部",
                "GroupPath": ""
            }
        ],
        "RequestId": "5aa3fe4f-72c3-4c77-a48d-a418addff8c9",
        "TotalCount": 3
    }
}
```

