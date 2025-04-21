**Example 1: test**

test

Input: 

```
tccli ioa DescribeDownloadDevices --cli-unfold-argument  \
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
    --GroupId 0 \
    --OsType 0 \
    --OnlineStatus 0 \
    --ProfileField 0 \
    --ProfileValue abc \
    --QueryType 0 \
    --Status 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "DownloadURL": "abc"
        },
        "RequestId": "abc"
    }
}
```

