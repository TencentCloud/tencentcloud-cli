**Example 1: 示例1**



Input: 

```
tccli mna GetGroupDetail --cli-unfold-argument  \
    --GroupId xxx \
    --PageSize 10 \
    --PageNumber 1
```

Output: 
```
{
    "Response": {
        "GroupInfo": {
            "GroupId": "abc",
            "GroupName": "abc",
            "CreateTime": "abc",
            "UpdateTime": "abc",
            "Description": "abc",
            "DeviceNum": 0
        },
        "DeviceInfos": [
            {
                "DeviceId": "abc",
                "DeviceName": "abc",
                "CreateTime": "abc",
                "LastTime": "abc",
                "Remark": "abc",
                "AccessScope": 0,
                "LicensePayMode": 0,
                "Payer": 0,
                "GroupId": "abc",
                "GroupName": "abc"
            }
        ],
        "Length": 0,
        "TotalPage": 0,
        "RequestId": "abc"
    }
}
```

