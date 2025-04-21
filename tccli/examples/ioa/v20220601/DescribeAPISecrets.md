**Example 1: 示例1**



Input: 

```
tccli ioa DescribeAPISecrets --cli-unfold-argument  \
    --Status 0 \
    --Condition.Sort.Field xx \
    --Condition.Sort.Order xx \
    --Condition.FilterGroups.0.Filters.0.Operator xx \
    --Condition.FilterGroups.0.Filters.0.Field xx \
    --Condition.FilterGroups.0.Filters.0.Values xx \
    --Condition.PageNum 0 \
    --Condition.Filters.0.Operator xx \
    --Condition.Filters.0.Field xx \
    --Condition.Filters.0.Values xx \
    --Condition.PageSize 0 \
    --Title xx
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": [
                {
                    "Status": 0,
                    "UpdateTime": "xx",
                    "Title": "xx",
                    "IsUsed": 0,
                    "SecretKey": "xx",
                    "Secret": "xx",
                    "SecretId": 0,
                    "CreateTime": "xx"
                }
            ],
            "Page": {
                "Total": 1,
                "PageNum": 1,
                "PageSize": 1,
                "PageCount": 1
            }
        },
        "RequestId": "xx"
    }
}
```

