**Example 1: 获取硬件设备信息**



Input: 

```
tccli mna GetHardwareInfo --cli-unfold-argument  \
    --Vendor kainan \
    --SN 123321
```

Output: 
```
{
    "Response": {
        "LicensePayMode": 0,
        "Payer": 1,
        "RequestId": "e7c277b9-690f-46a3-910e-09b3aae1ee94",
        "SN": "123321",
        "Vendor": "kainan"
    }
}
```

