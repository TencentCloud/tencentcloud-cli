**Example 1: 示例1**



Input: 

```
tccli ioa DescribeExpandedAccountGroupTree --cli-unfold-argument  \
    --AccountGroupId 1
```

Output: 
```
{
    "Response": {
        "Data": {
            "AccountGroups": [
                {
                    "Id": 1,
                    "Name": "",
                    "ParentId": 1,
                    "Description": "",
                    "Source": 1,
                    "NamePath": "全网账户.自建",
                    "IdPath": "1,2",
                    "IdPathArr": [
                        1
                    ],
                    "OrgId": "",
                    "ParentOrgId": "",
                    "Utime": "",
                    "Itime": "",
                    "ExtraInfo": "",
                    "IsLeaf": true,
                    "ReadOnly": true
                }
            ],
            "Accounts": [
                {
                    "Id": 1,
                    "UserId": "",
                    "UserName": "",
                    "IdPath": "1,2",
                    "IdPathArr": "1.2",
                    "OrgId": 1,
                    "OrgName": "",
                    "ExtraInfo": "",
                    "Source": 1,
                    "Status": 1,
                    "Itime": "",
                    "Utime": ""
                }
            ]
        },
        "RequestId": "81d13817-209e-4237-978e-71ec82fe2c77"
    }
}
```

