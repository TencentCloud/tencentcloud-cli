**Example 1: 获取设备基本信息列表**



Input: 

```
tccli mna GetDevices --cli-unfold-argument  \
    --PageSize 10 \
    --PageNumber 1 \
    --Keyword mna-xxx
```

Output: 
```
{
    "Response": {
        "DeviceInfos": [
            {
                "DeviceName": "dev",
                "Remark": "xx",
                "DeviceId": "mna-xxx",
                "LastTime": 1,
                "CreateTime": 1
            },
            {
                "DeviceName": "dev1",
                "Remark": "xx",
                "DeviceId": "mna-xxx",
                "LastTime": 1,
                "CreateTime": 1
            }
        ],
        "Length": 10,
        "TotalPage": 2,
        "RequestId": "xx"
    }
}
```

