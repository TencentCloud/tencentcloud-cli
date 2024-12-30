**Example 1: 示例**



Input: 

```
tccli mna GetHardwareList --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 1
```

Output: 
```
{
    "Response": {
        "HardwareInfos": [
            {
                "ActiveTime": "1686554927",
                "CreateTime": "1685673786",
                "Description": "测试00-00",
                "DeviceId": "mna-2x2tllhb18",
                "DeviceName": "test-vendor-hardware-00-00",
                "FlowTrunc": 0,
                "GroupId": "",
                "GroupName": "",
                "LicenseChargingMode": 2,
                "LicensePayMode": 0,
                "Payer": 1,
                "SN": "test-vendor-hardware-00",
                "VendorDescription": "测试00"
            }
        ],
        "Length": 107,
        "RequestId": "50f72657-2085-49fe-839f-71f3088c7f0a",
        "TotalPage": 107
    }
}
```

