**Example 1: 厂商查看设备**

厂商查看设备

Input: 

```
tccli mna GetVendorHardware --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "Length": 1,
        "RequestId": "728a4c82-b31c-4b32-9cee-3ba1fdd1903c",
        "TotalPage": 2,
        "VendorHardware": [
            {
                "CreateTime": "1685591205",
                "Description": "",
                "DeviceId": "",
                "Payer": 0,
                "HardwareId": "cpe-5n9n3o63t2",
                "LicenseChargingMode": 2,
                "LicensePayMode": -1,
                "SN": "cloud-sn",
                "Status": 1
            }
        ]
    }
}
```

**Example 2: 获取厂商设备列表**

获取厂商设备列表

Input: 

```
tccli mna GetVendorHardware --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --Keyword keywords \
    --Status 0
```

Output: 
```
{
    "Response": {
        "VendorHardware": [
            {
                "HardwareId": "cpe-2ycsnymh2u",
                "SN": "cpe-sn-04",
                "CreateTime": "1685449404",
                "Status": 0,
                "Payer": 0,
                "ActiveTime": "1685449404",
                "Description": "描述",
                "DeviceId": "mna-dev1",
                "LicenseChargingMode": 0,
                "LicensePayMode": -1,
                "LastOnlineTime": "1685449404"
            }
        ],
        "Length": 1,
        "TotalPage": 1,
        "RequestId": "728a4c82-b31c-4b32-9cee-3ba1fdd1903c"
    }
}
```

