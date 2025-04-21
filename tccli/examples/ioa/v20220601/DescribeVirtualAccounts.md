**Example 1: 示例1**

DescribeVirtualAccounts

Input: 

```
tccli ioa DescribeVirtualAccounts --cli-unfold-argument  \
    --VirtualGroupId 1 \
    --Condition.Filters.0.Field abc \
    --Condition.Filters.0.Operator abc \
    --Condition.Filters.0.Values abc \
    --Condition.FilterGroups.0.Filters.0.Field abc \
    --Condition.FilterGroups.0.Filters.0.Operator abc \
    --Condition.FilterGroups.0.Filters.0.Values abc \
    --Condition.Sort.Field abc \
    --Condition.Sort.Order abc \
    --Condition.PageSize 0 \
    --Condition.PageNum 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "UserName": "abc",
                    "Status": 0,
                    "Itime": "abc",
                    "AccountGroupId": 1,
                    "Source": 0,
                    "ExtraInfo": "abc",
                    "UserId": "abc",
                    "GroupName": "abc",
                    "NamePath": "abc",
                    "Utime": "abc",
                    "Id": 1,
                    "AccountId": 1
                }
            ],
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            }
        },
        "RequestId": "abc"
    }
}
```

