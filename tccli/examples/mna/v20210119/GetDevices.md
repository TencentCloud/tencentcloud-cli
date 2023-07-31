**Example 1: 获取设备基本信息列表**

获取设备基本信息列表

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
                "DeviceId": "abc",
                "DeviceName": "abc",
                "CreateTime": "abc",
                "LastTime": "abc",
                "Remark": "abc"
            }
        ],
        "Length": 0,
        "TotalPage": 0,
        "RequestId": "abc"
    }
}
```

