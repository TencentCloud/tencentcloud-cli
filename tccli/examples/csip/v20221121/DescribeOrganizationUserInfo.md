**Example 1: 查询集团账号用户列表**

查询集团账号用户列表

Input: 

```
tccli csip DescribeOrganizationUserInfo --cli-unfold-argument  \
    --MemberId mem-5b28e2010c18f07a \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Order SubUserCount \
    --Filter.By desc \
    --Filter.Filters.0.Name NickName \
    --Filter.Filters.0.Values Andy \
    --Filter.Filters.0.OperatorType 7 \
    --NotSupportCloud True
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "Uin": "100014592178",
                "AppId": "1302396000",
                "NickName": "Andy",
                "NodeName": "Root",
                "CFWProtect": "Ultimate",
                "WAFProtect": "Advanced",
                "CWPProtect": "Ultimate",
                "CSIPProtect": "Ultimate",
                "Role": "admin",
                "MemberId": "mem-68b8087a65268000",
                "JoinType": "create",
                "AssetCount": 1235,
                "RiskCount": 1599,
                "AttackCount": 1839,
                "SubUserCount": 11,
                "Enable": 1,
                "QuotaConsumer": 1,
                "CloudType": 0,
                "PermissionList": [
                    "readhost"
                ],
                "AuthType": 0,
                "SyncFrequency": 0,
                "IsExpired": false,
                "TcMemberType": 0,
                "JoinTypeInfo": "sub account"
            }
        ],
        "JoinTypeLst": [
            {
                "Text": "集团账号",
                "Value": "0"
            }
        ],
        "RequestId": "f9184c15-9721-456d-8ca0-4263967b5ead"
    }
}
```

