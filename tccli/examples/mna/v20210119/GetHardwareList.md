**Example 1: 硬件信息列表**

硬件信息列表

Input: 

```
tccli mna GetHardwareList --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 0 \
    --Keyword abc
```

Output: 
```
{
    "Response": {
        "HardwareInfos": [
            {
                "DeviceId": "abc",
                "DeviceName": "abc",
                "ActiveTime": "abc",
                "LastOnlineTime": "abc",
                "Description": "abc",
                "VendorDescription": "abc",
                "LicenseChargingMode": 0,
                "CreateTime": "abc",
                "SN": "abc"
            }
        ],
        "Length": 0,
        "TotalPage": 0,
        "RequestId": "abc"
    }
}
```

**Example 2: 租户查看厂商设备**

租户查看厂商设备

Input: 

```
tccli mna GetHardwareList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 11
```

Output: 
```
{
    "Response": {
        "HardwareInfos": [
            {
                "ActiveTime": "1685514528",
                "CreateTime": "1685510058",
                "Description": "",
                "DeviceId": "mna-fsap0nz6lp",
                "DeviceName": "DeviceName",
                "LicenseChargingMode": 1,
                "SN": "cpe-sn-08",
                "VendorDescription": "",
                "LastOnlineTime": "1685518319"
            },
            {
                "ActiveTime": "1685518319",
                "CreateTime": "1685518183",
                "Description": "",
                "DeviceId": "mna-yhf5rxj0ud",
                "DeviceName": "DeviceName1",
                "LicenseChargingMode": 1,
                "SN": "cpe-sn-13",
                "VendorDescription": "",
                "LastOnlineTime": "1685518319"
            }
        ],
        "Length": 2,
        "RequestId": "cad17990-449a-4961-830f-0cde5b8bd74a",
        "TotalPage": 1
    }
}
```

