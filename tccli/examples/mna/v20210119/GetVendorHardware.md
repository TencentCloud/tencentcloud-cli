**Example 1: 厂商查看设备**

厂商查看设备

Input: 

```
tccli mna GetVendorHardware --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 11
```

Output: 
```
{
    "Response": {
        "Length": 11,
        "RequestId": "728a4c82-b31c-4b32-9cee-3ba1fdd1903c",
        "TotalPage": 2,
        "VendorHardware": [
            {
                "CreateTime": "1685591205",
                "Description": "",
                "DeviceId": "",
                "HardwareId": "cpe-5n9n3o63t2",
                "LicenseChargingMode": 2,
                "SN": "cloud-sn",
                "Status": 1
            },
            {
                "CreateTime": "1685430273",
                "Description": "Description",
                "DeviceId": "",
                "HardwareId": "cpe-3lk7lfbsyu",
                "LicenseChargingMode": 1,
                "SN": "cpe-sn",
                "Status": 1
            },
            {
                "CreateTime": "1685447830",
                "Description": "test",
                "DeviceId": "",
                "HardwareId": "cpe-aypx5a3crh",
                "LicenseChargingMode": 1,
                "SN": "cpe-sn -5",
                "Status": 1
            },
            {
                "CreateTime": "1685449404",
                "Description": "",
                "DeviceId": "",
                "HardwareId": "cpe-2ycsnymh2u",
                "LicenseChargingMode": 1,
                "SN": "cpe-sn-04",
                "Status": 1
            },
            {
                "CreateTime": "1685449404",
                "Description": "",
                "DeviceId": "",
                "HardwareId": "cpe-z6sm6srvbm",
                "LicenseChargingMode": 2,
                "SN": "cpe-sn-05",
                "Status": 1
            },
            {
                "CreateTime": "1685509926",
                "Description": "",
                "DeviceId": "",
                "HardwareId": "cpe-r6739p8h1t",
                "LicenseChargingMode": 1,
                "SN": "cpe-sn-06",
                "Status": 1
            },
            {
                "CreateTime": "1685509926",
                "Description": "",
                "DeviceId": "",
                "HardwareId": "cpe-pjugv0zyan",
                "LicenseChargingMode": 2,
                "SN": "cpe-sn-07",
                "Status": 1
            },
            {
                "ActiveTime": "1685514528",
                "CreateTime": "1685510058",
                "Description": "",
                "DeviceId": "mna-fsap0nz6lp",
                "HardwareId": "cpe-9gi3engwpb",
                "LicenseChargingMode": 1,
                "SN": "cpe-sn-08",
                "Status": 2
            },
            {
                "CreateTime": "1685514559",
                "Description": "",
                "DeviceId": "",
                "HardwareId": "cpe-n17ndxng5p",
                "LicenseChargingMode": 1,
                "SN": "cpe-sn-09",
                "Status": 1
            },
            {
                "CreateTime": "1685430552",
                "Description": "",
                "DeviceId": "",
                "HardwareId": "cpe-5hgb388vw2",
                "LicenseChargingMode": 1,
                "SN": "cpe-sn-1",
                "Status": 1
            },
            {
                "CreateTime": "1685514559",
                "Description": "",
                "DeviceId": "",
                "HardwareId": "cpe-do4t0e8uaw",
                "LicenseChargingMode": 1,
                "SN": "cpe-sn-10",
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
    --Keyword abc \
    --Status 0
```

Output: 
```
{
    "Response": {
        "VendorHardware": [
            {
                "HardwareId": "abc",
                "SN": "abc",
                "CreateTime": "abc",
                "Status": 0,
                "ActiveTime": "abc",
                "Description": "abc",
                "DeviceId": "abc",
                "LicenseChargingMode": 0,
                "LastOnlineTime": "abc"
            }
        ],
        "Length": 0,
        "TotalPage": 0,
        "RequestId": "abc"
    }
}
```

