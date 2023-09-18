**Example 1: 查询集团下所有成员企业**

查询集团下所有成员企业

Input: 

```
tccli ess DescribeOrganizationGroupOrganizations --cli-unfold-argument  \
    --Operator.UserId yDxbWUyKQDx7OZUuO4zjESvEkRMHc55R \
    --Export False \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ActivatedTotal": 1,
        "ExportUrl": "",
        "JoinedTotal": 1,
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
        "RequestId": "s16753***7361364",
        "Total": 1
    }
}
```

**Example 2: 错误示例：Limit 超过了限制**

查询子企业信息的时候，Limit 传了一个大于 1000 的数值，报错信息如下

Input: 

```
tccli ess DescribeOrganizationGroupOrganizations --cli-unfold-argument  \
    --Operator.UserId yDxbWUyKQDx7OZUuO4zjESvEkRMHc55R \
    --Limit 2000 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue",
            "Message": "分页大小应该大于0小于等于1000"
        },
        "RequestId": "s12919239kjdksfj****klsdf"
    }
}
```

