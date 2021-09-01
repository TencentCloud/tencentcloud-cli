**Example 1: 获取设备下属通道**



Input: 

```
tccli iotvideoindustry DescribeIPCChannels --cli-unfold-argument  \
    --DeviceId 99576636581320000278_99576636581320000278 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "DeviceList": [
            {
                "NickName": "Camera 01",
                "DeviceId": "99576636581320000278_99576636581320000278",
                "Status": 0,
                "ExtraInformation": "{\"Manufacturer\":\"Hikvision\",\"Model\":\"IP Camera\"}",
                "DeviceType": 6,
                "IsRecord": 0,
                "DeviceCode": "99576636581320000278",
                "Recordable": 1,
                "Protocol": ""
            },
            {
                "NickName": "Camera 02",
                "DeviceId": "99576636581320000278_99576636581320000279",
                "Status": 0,
                "ExtraInformation": "{\"Model\":\"IP Camera\",\"Manufacturer\":\"Hikvision\"}",
                "DeviceType": 6,
                "IsRecord": 0,
                "DeviceCode": "99576636581320000279",
                "Recordable": 1,
                "Protocol": ""
            }
        ],
        "RequestId": "20e4eb35-5429-4b25-8e4e-d7435518f194",
        "TotalCount": 2
    }
}
```

