**Example 1: 获取告警列表**



Input: 

```
tccli iotvideoindustry DescribeWarnings --cli-unfold-argument  \
    --WarnLevelArray 1 \
    --WarnModeArray 2 \
    --OrderType 1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 2,
                "DeviceId": "34020000001320000000_34020000001320000000",
                "DeviceName": "test2",
                "WarnChannel": "34020000001320000000_34020000001320000000",
                "WarnLevel": 1,
                "WarnLevelName": "一级警情",
                "WarnMode": 2,
                "WarnModeName": "设备报警",
                "WarnType": 5,
                "Del": 0,
                "CreateTime": "2021-05-25T17:56:51+08:00",
                "UpdateTime": "2021-05-25T17:56:51+08:00"
            },
            {
                "Id": 1,
                "DeviceId": "34020000001320000000_34020000001320000000",
                "DeviceName": "test2",
                "WarnChannel": "34020000001320000000_34020000001320000000",
                "WarnLevel": 1,
                "WarnLevelName": "一级警情",
                "WarnMode": 2,
                "WarnModeName": "设备报警",
                "WarnType": 5,
                "Del": 0,
                "CreateTime": "2021-05-25T16:23:59+08:00",
                "UpdateTime": "2021-05-25T16:23:59+08:00"
            }
        ],
        "RequestId": "226618be-27ec-46f4-a19e-bdb980baec92",
        "Total": 2
    }
}
```

