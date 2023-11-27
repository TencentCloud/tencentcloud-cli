**Example 1: 新建硬件设备**

批量新建硬件设备

Input: 

```
tccli mna AddHardware --cli-unfold-argument  \
    --Hardware.0.SN abc \
    --Hardware.0.LicenseChargingMode 1 \
    --Hardware.0.Description abc
```

Output: 
```
{
    "Response": {
        "Hardware": [
            {
                "SN": "abc",
                "LicenseChargingMode": 1,
                "Description": "abc",
                "HardwareId": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

