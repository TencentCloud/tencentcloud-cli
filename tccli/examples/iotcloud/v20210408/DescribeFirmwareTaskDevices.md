**Example 1: 查询固件升级任务的设备列表**



Input: 

```
tccli iotcloud DescribeFirmwareTaskDevices --cli-unfold-argument  \
    --ProductId O4CCMMZE3A \
    --FirmwareVersion 1.0
```

Output: 
```
{
    "Response": {
        "Total": 0,
        "Devices": [
            {
                "DeviceName": "123",
                "LastProcessTime": 1597141763,
                "Status": 5,
                "ErrMsg": "",
                "DstVersion": "1.0",
                "Retcode": 0,
                "Percent": 0,
                "OriVersion": "0.1"
            },
            {
                "OriVersion": "0.1",
                "DeviceName": "abc",
                "LastProcessTime": 1597140525,
                "Status": 0,
                "ErrMsg": "",
                "DstVersion": "1.0",
                "Retcode": 0,
                "Percent": 0
            },
            {
                "LastProcessTime": 1597141811,
                "Status": 6,
                "ErrMsg": "",
                "DstVersion": "1.0",
                "Retcode": 0,
                "Percent": 0,
                "OriVersion": "0.1",
                "DeviceName": "123"
            }
        ],
        "RequestId": "968ac21f-815f-4f32-852f-c0729c40e724"
    }
}
```

