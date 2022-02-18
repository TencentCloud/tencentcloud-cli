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
            "NickName": "真的双通道",
            "DeviceId": "99576636581320000278_99576636581320000278",
            "Status": 1,
            "ExtraInformation": "{\"Manufacturer\":\"Hikvision\",\"Model\":\"IP Camera\"}",
            "IsRecord": 0,
            "DeviceType": 2,
            "DeviceCode": "99576636581320000278",
            "GroupPath": "",
            "CreateTime": 1621581437,
            "Recordable": 0,
            "Protocol": "GB28181"
        },
        "RequestId": "75c3af48-676f-49e2-8cdd-f66e6dcdec48"
    }
}
```

