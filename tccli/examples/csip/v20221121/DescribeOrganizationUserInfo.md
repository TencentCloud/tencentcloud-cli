**Example 1: 查询集团账号用户列表**

查询集团账号用户列表

Input: 

```
tccli csip DescribeOrganizationUserInfo --cli-unfold-argument  \
    --MemberId abc \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc \
    --NotSupportCloud True
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "Uin": "abc",
                "NickName": "abc",
                "NodeName": "abc",
                "AssetCount": 0,
                "RiskCount": 0,
                "AttackCount": 0,
                "Role": "abc",
                "MemberId": "abc",
                "AppId": "abc",
                "JoinType": "abc",
                "CFWProtect": "abc",
                "WAFProtect": "abc",
                "CWPProtect": "abc",
                "Enable": 0,
                "CSIPProtect": "abc",
                "QuotaConsumer": 0,
                "CloudType": 0,
                "SyncFrequency": 0,
                "IsExpired": true,
                "PermissionList": [
                    "abc"
                ],
                "AuthType": 0,
                "TcMemberType": 0,
                "SubUserCount": 0,
                "JoinTypeInfo": "abc"
            }
        ],
        "JoinTypeLst": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

