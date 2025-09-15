**Example 1: 查询固件升级任务的设备列表**



Input: 

```
tccli iotexplorer DescribeFirmwareTaskDevices --cli-unfold-argument  \
    --ProductID I6KTCZ170U \
    --FirmwareVersion t.1
```

Output: 
```
{
    "Response": {
        "Devices": [
            {
                "DeviceName": "testota01",
                "DstVersion": "t.1",
                "ErrMsg": "firmware no need update.",
                "LastProcessTime": 1599293301,
                "OriVersion": "",
                "Percent": 0,
                "Retcode": 0,
                "Status": 5,
                "TaskId": 1000698
            },
            {
                "DeviceName": "testota01",
                "DstVersion": "t.1",
                "ErrMsg": "firmware no need update.",
                "LastProcessTime": 1599293291,
                "OriVersion": "",
                "Percent": 0,
                "Retcode": 0,
                "Status": 5,
                "TaskId": 1000697
            },
            {
                "DeviceName": "testota01",
                "DstVersion": "t.1",
                "ErrMsg": "firmware no need update.",
                "LastProcessTime": 1599293161,
                "OriVersion": "",
                "Percent": 0,
                "Retcode": 0,
                "Status": 5,
                "TaskId": 1000696
            },
            {
                "DeviceName": "testota01",
                "DstVersion": "t.1",
                "ErrMsg": "firmware no need update.",
                "LastProcessTime": 1599292421,
                "OriVersion": "",
                "Percent": 0,
                "Retcode": 0,
                "Status": 5,
                "TaskId": 1000695
            },
            {
                "DeviceName": "testota01",
                "DstVersion": "t.1",
                "ErrMsg": "firmware no need update.",
                "LastProcessTime": 1599292411,
                "OriVersion": "",
                "Percent": 0,
                "Retcode": 0,
                "Status": 5,
                "TaskId": 1000694
            }
        ],
        "RequestId": "95e791e3-dfc4-47fa-9f0b-d3248a5adb55",
        "Total": 5
    }
}
```

