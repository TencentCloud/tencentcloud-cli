**Example 1: 查询license列表**

查询用户购买的license列表以及设备绑定情况

Input: 

```
tccli trro GetDevices --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10 \
    --ProjectId abc \
    --DeviceId abc
```

Output: 
```
{
    "Response": {
        "RequestId": "468bf31b-b5f7-44c4-8663-8d9548693cf5",
        "Devices": [
            {
                "DeviceId": "xxx",
                "DeviceName": "xxx",
                "LicenseCount": 2,
                "RemainDay": 30,
                "ExpireTime": "167840945",
                "Duration": "86400",
                "MonthlyRemainTime": 66000,
                "LicenseIds": [
                    "trro-2e24a74a-67ea-1732-076d-75bf772529a",
                    "trro-2e24a74a-67ea-1732-073d-75bf772579a"
                ]
            },
            {
                "DeviceId": "xxx",
                "DeviceName": "xxx",
                "LicenseCount": 2,
                "RemainDay": 30,
                "ExpireTime": "167840945",
                "Duration": "86400",
                "MonthlyRemainTime": 66000,
                "LicenseIds": [
                    "trro-2e24a74a-67ea-1732-076d-75bf772529a",
                    "trro-2e24a74a-67ea-1732-073d-75bf772579a"
                ]
            }
        ],
        "TotalCount": 2
    }
}
```

