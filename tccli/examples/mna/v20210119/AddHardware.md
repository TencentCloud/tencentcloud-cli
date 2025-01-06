**Example 1: 新建硬件设备**

批量新建硬件设备

Input: 

```
tccli mna AddHardware --cli-unfold-argument  \
    --Hardware.0.SN AN \
    --Hardware.0.LicenseChargingMode 1 \
    --Hardware.0.Description AddHardware info
```

Output: 
```
{
    "Response": {
        "Hardware": [
            {
                "SN": "AN",
                "LicenseChargingMode": 1,
                "Description": "AddHardware描述",
                "HardwareId": "cpe-9oii2ew1z4"
            }
        ],
        "RequestId": "a1434e98-16e8-41de-9b9b-27805a9cffbf"
    }
}
```

