**Example 1: 批量激活设备**

批量激活设备

Input: 

```
tccli mna ActivateHardware --cli-unfold-argument  \
    --Hardware.0.Vendor vendor \
    --Hardware.0.SN AN \
    --Hardware.0.DeviceName name \
    --Hardware.0.Description activateHardware info \
    --Hardware.0.DataKey keys
```

Output: 
```
{
    "Response": {
        "HardwareInfo": [
            {
                "Vendor": "vendor",
                "SN": "AN",
                "DeviceName": "name",
                "Description": "activateHardware info",
                "DataKey": "keys",
                "LicensePayMode": 1,
                "AccessScope": 1
            }
        ],
        "RequestId": "edd378f7-2511-4692-a029-5ca3d22c1884"
    }
}
```

