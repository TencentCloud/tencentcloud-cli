**Example 1: 示例1**



Input: 

```
tccli mna GetGroupDetail --cli-unfold-argument  \
    --GroupId cliGrp-xf8rboasb \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "GroupInfo": {
            "GroupId": "cliGrp-xf8rboasb",
            "GroupName": "test",
            "CreateTime": "1711076263000",
            "UpdateTime": "1711076263000",
            "Description": "test",
            "DeviceNum": 0
        },
        "DeviceInfos": [
            {
                "DeviceId": "mna-detr244",
                "DeviceName": "name",
                "CreateTime": "1711076263000",
                "LastTime": "1711076263000",
                "Remark": "mark",
                "AccessScope": 0,
                "LicensePayMode": 0,
                "Payer": 0,
                "GroupId": "cliGrp-xf8rboasb",
                "GroupName": "test"
            }
        ],
        "Length": 0,
        "TotalPage": 0,
        "RequestId": "fd429f79-9914-46e7-94c3-c0695ee1c8b9"
    }
}
```

