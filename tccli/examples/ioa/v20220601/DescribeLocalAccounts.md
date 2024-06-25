**Example 1: normal**



Input: 

```
tccli ioa DescribeLocalAccounts --cli-unfold-argument  \
    --Condition.Filters.0.Field abc \
    --Condition.Filters.0.Operator abc \
    --Condition.Filters.0.Values abc \
    --Condition.FilterGroups.0.Filters.0.Field abc \
    --Condition.FilterGroups.0.Filters.0.Operator abc \
    --Condition.FilterGroups.0.Filters.0.Values abc \
    --Condition.Sort.Field abc \
    --Condition.Sort.Order abc \
    --Condition.PageSize 0 \
    --Condition.PageNum 0 \
    --AccountGroupId 0 \
    --ShowFlag 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            },
            "Items": [
                {
                    "Id": 0,
                    "UserId": "abc",
                    "UserName": "abc",
                    "AccountId": 0,
                    "GroupId": 0,
                    "GroupName": "abc",
                    "NamePath": "abc",
                    "Source": 0,
                    "Status": 0,
                    "Itime": "abc",
                    "Utime": "abc",
                    "ExtraInfo": "abc",
                    "RiskLevel": "abc",
                    "AccountGroups": [
                        {
                            "AccountGroupId": 0
                        }
                    ],
                    "MobileBindNum": 0,
                    "PcBindNum": 0,
                    "OnlineStatus": 0,
                    "ActiveStatus": 0,
                    "LoginTime": "abc",
                    "LogoutTime": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

