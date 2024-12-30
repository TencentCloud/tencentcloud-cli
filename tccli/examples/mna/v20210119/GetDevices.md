**Example 1: 示例**



Input: 

```
tccli mna GetDevices --cli-unfold-argument  \
    --PageSize 1 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "DeviceInfos": [
            {
                "AccessScope": 0,
                "CreateTime": "1663310188000",
                "DeviceId": "mna-w795bzezug",
                "DeviceName": "dev2233",
                "FlowTrunc": 0,
                "GroupId": "",
                "GroupName": "",
                "LastTime": "1719454676000",
                "LicensePayMode": 0,
                "Payer": 0,
                "Remark": "",
                "Sn": "",
                "Vendor": ""
            }
        ],
        "Length": 899,
        "RequestId": "8fbce821-acbb-49db-ad70-345b5d353324",
        "TotalPage": 899
    }
}
```

