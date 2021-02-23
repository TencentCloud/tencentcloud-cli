**Example 1: 获取设备列表**



Input: 

```
tccli iotvideo DescribeDevices --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --ProductId PTROMP3AOB
```

Output: 
```
{
    "Response": {
        "RequestId": "9c56647c-17be-4ff7-a80c-245cabe0a42c",
        "TotalCount": 49,
        "Devices": [
            {
                "DeviceName": "siva_31337976_1",
                "Online": 0,
                "LoginTime": 1609293765,
                "DevicePsk": "k2o3rxGV0zLHBxabvpszGg==",
                "EnableState": 1,
                "ExpireTime": 1640681977
            },
            {
                "DeviceName": "siva_31337976_2",
                "Online": 0,
                "LoginTime": 1609730065,
                "DevicePsk": "0FY5jg8MFuapHipHaICb/Q==",
                "EnableState": 1,
                "ExpireTime": 1640681977
            },
            {
                "DeviceName": "siva_31337976_3",
                "Online": 3,
                "LoginTime": 0,
                "DevicePsk": "csxPuMxoS3NgoawPKtRHRA==",
                "EnableState": 1,
                "ExpireTime": 1640681977
            },
            {
                "DeviceName": "siva_31337976_4",
                "Online": 3,
                "LoginTime": 0,
                "DevicePsk": "KK1lXS/yy7QHaWBG0xPeMQ==",
                "EnableState": 1,
                "ExpireTime": 1640681977
            },
            {
                "DeviceName": "siva_31337976_5",
                "Online": 3,
                "LoginTime": 0,
                "DevicePsk": "ptrRs+mGSU2M3P8lu6ronQ==",
                "EnableState": 1,
                "ExpireTime": 1640681977
            },
            {
                "DeviceName": "siva_31337976_6",
                "Online": 3,
                "LoginTime": 0,
                "DevicePsk": "1xpMhJrnlOLjkcmVEu+foA==",
                "EnableState": 1,
                "ExpireTime": 1640681977
            },
            {
                "DeviceName": "siva_31337976_7",
                "Online": 3,
                "LoginTime": 0,
                "DevicePsk": "MSm99MKWJGk+JssfngaJNA==",
                "EnableState": 1,
                "ExpireTime": 1640681977
            },
            {
                "DeviceName": "siva_31337976_8",
                "Online": 3,
                "LoginTime": 0,
                "DevicePsk": "Jeziu8yQXvG/vPpd9jiLlg==",
                "EnableState": 1,
                "ExpireTime": 1640681977
            },
            {
                "DeviceName": "siva_31337976_9",
                "Online": 3,
                "LoginTime": 0,
                "DevicePsk": "GWnZSYzGsKrfhvXZ5CZ3IQ==",
                "EnableState": 1,
                "ExpireTime": 1640681977
            },
            {
                "DeviceName": "siva_31337857_9",
                "Online": 3,
                "LoginTime": 0,
                "DevicePsk": "2BxKJKBoqncpl8F/Q/oJxg==",
                "EnableState": 1,
                "ExpireTime": 1640681857
            }
        ]
    }
}
```

