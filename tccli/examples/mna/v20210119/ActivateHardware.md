**Example 1: 批量激活设备**

批量激活设备

Input: 

```
tccli mna ActivateHardware --cli-unfold-argument  \
    --Hardware.0.Vendor abc \
    --Hardware.0.SN abc \
    --Hardware.0.DeviceName abc \
    --Hardware.0.Description abc \
    --Hardware.0.DataKey abc
```

Output: 
```
{
    "Response": {
        "HardwareInfo": [
            {
                "Vendor": "abc",
                "SN": "abc",
                "DeviceName": "abc",
                "Description": "abc",
                "DataKey": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

