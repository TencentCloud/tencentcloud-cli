**Example 1: 描述单个设备的详细信息**



Input: 

```
tccli iotvideoindustry DescribeDevice --cli-unfold-argument  \
    --DeviceId 99576636581320000278_99576636581320000278
```

Output: 
```
{
    "Response": {
        "Device": {
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
        },
        "RequestId": "75c3af48-676f-49e2-8cdd-f66e6dcdec48"
    }
}
```

