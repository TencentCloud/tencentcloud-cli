**Example 1: 示例1**

查询集团下所有成员企业

Input: 

```
tccli ess DescribeOrganizationGroupOrganizations --cli-unfold-argument  \
    --Operator.UserId y******************g \
    --Export False \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ActivedTotal": 1,
        "ExportUrl": "",
        "JoinedTotal": 11,
        "List": [
            {
                "AdminInfo": {
                    "Mobile": "150****7992",
                    "Name": "王*新"
                },
                "Alias": "",
                "FlowEngineEnable": true,
                "IdCardNumber": "9***************F",
                "IsMainOrganization": false,
                "JoinTime": 1673166251,
                "License": "",
                "LicenseExpireTime": 0,
                "Name": "王*新测试企业一",
                "OrganizationId": "y******************C",
                "Status": 2,
                "UpdateTime": 1673232933
            }
        ],
        "RequestId": "s16753xxx7361364",
        "Total": 1
    }
}
```

